from django import template
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from vegetarian_cookbook import appsettings
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
    lenght = len(ingredients)
    more = lenght > number_of_displayed
    return {
        'ingredients': ingredients[0:number_of_displayed - 1] if more else ingredients,
        'more': lenght - number_of_displayed + 1 if more else 0,
        'empty_row': range(0 if more else number_of_displayed - lenght)
    }

@register.inclusion_tag('vegetarian_cookbook/templatetags/range_slider.html')
def range_slider(**kwargs):
    return kwargs

@register.inclusion_tag('vegetarian_cookbook/templatetags/paginator.html')
def paginator(data):
    return {'data':data}


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

@register.inclusion_tag('vegetarian_cookbook/templatetags/recipe_cooking_time.html')
def recipe_cooking_time(time):
    hours = 0
    minutes = time
    angle = int(round(time * 6))
    if time >= 60:
        hours = int((time - time % 60) / 60)
        minutes = time % 60
        angle = int(round(time / 2))
    return {
        'hours': hours,
        'minutes': minutes,
        'angle': angle
    }

@register.filter
def human_float(value, decimal = False):
    if decimal == False:
        return ('%f' % value).rstrip('0').rstrip('.')
    n = pow(10, int(decimal))
    if int(value * n) == int(value) * n:
        return int(round(value))
    else:
        return ("%0." + str(decimal) + 'f') % value


@register.simple_tag
def plural_form(value, n):
    if not value.plural:
        return value.name
    try:
        nplurals = appsettings.NPLURALS
        plural = appsettings.PLURAL
        plurals_array = value.plural.split(',')
        if nplurals == 2:
            return value.name if n == 1 else value.plural
        if int(n * 100) != int(n) *100:
            return plurals_array[0]  #??? only for ru?
        n = int(n)
        plural = plural.replace('\bn\b', str(n))
        key = eval(plural)
        return plurals_array[key-1]

    except Exception:
        return value.name if n == 1 else value.plural



