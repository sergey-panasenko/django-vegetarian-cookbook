from django import template
from django.utils.translation import gettext as _
from vegetarian_cookbook.models import Category
register = template.Library()

@register.inclusion_tag('vegetarian_cookbook/templatetags/categories_list.html')
def categories_list(a_class):
    categories = Category.objects.all()
    return {'categories': categories, 'a_class': a_class}

@register.inclusion_tag('vegetarian_cookbook/templatetags/categories_icons.html')
def categories_icons(a_class):
    categories = Category.objects.all()
    return {'categories': categories, 'a_class': a_class}

@register.inclusion_tag('vegetarian_cookbook/templatetags/ingredients_list.html')
def ingredients_list(number_of_displayed, ingredients):
    if len(ingredients) <= number_of_displayed:
        return {'ingredients': ingredients, 'more': 0}
    return {'ingredients': ingredients[0:number_of_displayed - 1], 'more': len(ingredients) - number_of_displayed + 1}

@register.inclusion_tag('vegetarian_cookbook/templatetags/recipe_energy_nutrients.html')
def recipe_energy_nutrients(size, show_legend, energy, protein, fat, carbohydrate):
    supernumber = 158
    if not energy:
        energy = 0
    if not protein:
        protein = 0
    if not fat:
        fat = 0
    if not carbohydrate:
        carbohydrate = 0
    return {
        'size': size,
        'show_legend': show_legend,
        'energy': energy,
        'protein': protein,
        'fat': fat,
        'carbohydrate': carbohydrate,
        'a1': -90,
        'a2': -90 + int(protein * 360 / 100),
        'a3': -90 + int(protein * 360 / 100) + int(fat * 360 / 100),
        'v1': int(protein * supernumber / 100),
        'v2': int(fat * supernumber / 100),
        'v3': int(carbohydrate * supernumber / 100),
        'n': supernumber,
    }
