# Django Vegetarian Cookbook, Copyright © 2018 Sergey Panasenko. Contacts: <sergey.panasenko@gmail.com>
# License: https://opensource.org/licenses/AGPL-3.0

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse
from imagekit.admin import AdminThumbnail
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline, AjaxSelectAdminStackedInline
from django.core.exceptions import ValidationError
from functools import partial

from .models import Unit, Ingredient, IngredientUnit, Category, Tag, Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeIngredientInlineForm

admin.site.site_header = _('My recipes')

admin.site.register(Category)


class UnitAdmin(AjaxSelectAdmin):
    pass

admin.site.register(Unit,UnitAdmin)

class TagAdmin(AjaxSelectAdmin):
    pass

admin.site.register(Tag,TagAdmin)

class IngredientUnitInline(AjaxSelectAdminTabularInline):
    model = IngredientUnit
    extra = 0

class IngredientAdmin(AjaxSelectAdmin):
    inlines = [
        IngredientUnitInline,
    ]

admin.site.register(Ingredient, IngredientAdmin)


class RecipeIngredientInline(AjaxSelectAdminTabularInline):
    model = RecipeIngredient
    form = RecipeIngredientInlineForm
    fields = ('ingredient', 'weight', 'or_col', 'quantity', 'unit', 'roughly')
    readonly_fields = ('or_col',)
    def or_col(self, obj):
        return _('OR')
    or_col.short_description = ''


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(AjaxSelectAdmin):
    exclude = ('url',)
    fields = ('generate_url', 'title', 'status', 'category', 'time', 'weight', 'image', 'tags', 'description')
    inlines = [
        RecipeIngredientInline,
        RecipeImageInline
    ]
    form = make_ajax_form(Recipe, {'tags': 'Tag'})
    readonly_fields = ('generate_url',)
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    admin_thumbnail.short_description = _('Thumbnail')
    def save_formset(self, request, form, formset, change):
        if formset.model == RecipeIngredient:
            for form in formset.forms:
                instance = form.instance
                if instance.quantity > 0 and instance.unit:
                    ingredient_unit = IngredientUnit.objects.get(unit=instance.unit, ingredient=instance.ingredient)
                    instance.weight = int(instance.quantity * ingredient_unit.ratio)
        formset.save()
    def save_model(self, request, obj, form, change):
        obj.fix_url();
        obj.save()
    def generate_url(self, obj):
        if not obj.url:
            return '???'
        return format_html('<a href="{}" target="_blank">{}</a>', reverse('recipes_recipe', args=(obj.url,)), reverse('recipes_recipe', args=(obj.url,)))
    generate_url.short_description = _('Url')

admin.site.register(
    Recipe,
    RecipeAdmin,
    list_display = ('admin_thumbnail', 'title', 'status', 'has_roughly', 'category', 'recipe_tags', 'recipe_ingredients'),
    list_display_links = ['title'],
    search_fields = ['title'],
    list_filter = ['category', 'tags', 'recipeingredient__ingredient__name'],
)
