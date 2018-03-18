# Django Vegetarian Cookbook, Copyright © 2018 Sergey Panasenko. Contacts: <sergey.panasenko@gmail.com>
# License: https://opensource.org/licenses/AGPL-3.0

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField
from .translit import transliterate

class Unit(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('unit name'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=_('unit')
        verbose_name_plural=_('units')

class Ingredient(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('ingredient name'))
    image = models.ImageField(upload_to='images', blank=True, verbose_name=_('image'))
    description = HTMLField(blank=True, verbose_name=_('description'))
    #~ water = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('water'))
    energy = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('energy'))
    protein = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('protein'))
    carbohydrate = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('carbohydrate'))
    fat = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('fat'))
    #~ fiber = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('fiber'))
    #~ sugar = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True, verbose_name=_('sugar'))
    thumbnail = ImageSpecField(source='image',
          processors=[ResizeToFill(150, 150)],
          format='JPEG',
          options={'quality': 90})
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=_('ingredient')
        verbose_name_plural=_('ingredients')

class IngredientUnit(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, verbose_name=_('ingredient'))
    unit = models.ForeignKey(Unit, default=1, on_delete=models.PROTECT, verbose_name=_('unit'))
    ratio = models.DecimalField(default=1, max_digits=10, decimal_places=4, verbose_name=_('ratio'))
    def __str__(self):
        return self.ingredient.name + '/' + self.unit.name
    class Meta:
        verbose_name=_('additional unit')
        verbose_name_plural=_('additional units')

class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('categoty name'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=_('category')
        verbose_name_plural=_('categories')

class Tag(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('tag name'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=_('tag')
        verbose_name_plural=_('tags')

class Recipe(models.Model):
    STATUS_CHOICES = (
        (u'P', _('published')),
        (u'd', _('draft')),
        (u'i', _('idea')),
    )
    title = models.CharField(max_length=250, verbose_name=_('title'))
    url = models.CharField(max_length=250, default='', unique=True, blank=True, verbose_name=_('recipe url'))
    status = models.CharField(max_length=2, default=u'i', choices=STATUS_CHOICES, verbose_name=_('status'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    description = HTMLField(blank=True, verbose_name=_('description'))
    time = models.IntegerField(default=0, null=True, blank=True, verbose_name=_('time'))
    weight = models.IntegerField(default=0, blank=True, verbose_name=_('weight'))
    image = models.ImageField(null=True, blank=True, upload_to='images', verbose_name=_('image'))
    thumbnail = ImageSpecField(source='image',
          processors=[ResizeToFill(150, 150)],
          format='JPEG',
          options={'quality': 90})
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_('tags'), help_text=_('tags'))
    def __str__(self):
        return self.title
    def recipe_tags(self):
        return ", ".join([t.name for t in self.tags.all()])
    recipe_tags.short_description = _('tags')
    def recipe_ingredients(self):
        ingredients = []
        for i in self.recipeingredient_set.all():
            ingredients.append(i.ingredient.name)
        return ', '.join(ingredients[0:3])
    def fix_url(self):
        self.url = transliterate(self.title)
    recipe_ingredients.short_description = _('ingredients')
    def has_roughly(self):
        hr = False
        for i in self.recipeingredient_set.all():
            if (i.roughly):
                hr = True
        return hr
    has_roughly.short_description = _('Has roughly')
    class Meta:
        verbose_name=_('recipe')
        verbose_name_plural=_('recipes')


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name=_('recipe'))
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name=_('ingredient'))
    weight = models.IntegerField(default=0, null=True, blank=True, verbose_name=_('weight in gram'))
    quantity = models.DecimalField(max_digits=7, decimal_places=4, default=0, verbose_name=_('quantity on additional unit'))
    unit = models.ForeignKey(Unit, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('additional unit'))
    roughly = models.BooleanField(default=False, verbose_name=_('roughly'))
    def __str__(self):
        return self.ingredient.name
    class Meta:
        verbose_name=_('ingredient')
        verbose_name_plural=_('ingredients')

class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name=_('recipe'))
    image = models.ImageField(upload_to='images', verbose_name=_('image'))
    thumbnail = ImageSpecField(source='image',
          processors=[ResizeToFill(150, 150)],
          format='JPEG',
          options={'quality': 90})
    title = models.CharField(max_length=250, blank=True, verbose_name=_('title'))
    class Meta:
        verbose_name=_('image')
        verbose_name_plural=_('images')


