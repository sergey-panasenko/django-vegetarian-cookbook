"""
Django Vegetarian Cookbook, Copyright © 2018 Sergey Panasenko.
Contacts: <sergey.panasenko@gmail.com>
License: https://opensource.org/licenses/AGPL-3.0
"""
from django import template
from vegetarian_cookbook import appsettings
from vegetarian_cookbook.models import Category

register = template.Library()


@register.inclusion_tag('vegetarian_cookbook/templatetags/categories_list.html')
def categories_list(a_class):
    """ show categories list """
    categories = Category.objects.all()
    return {'categories': categories, 'a_class': a_class}


@register.inclusion_tag(
    'vegetarian_cookbook/templatetags/categories_icons.html')
def categories_icons(a_class):
    """ show categories list as icons """
    categories = Category.objects.all()
    return {'categories': categories, 'a_class': a_class}


@register.inclusion_tag(
    'vegetarian_cookbook/templatetags/ingredients_list.html')
def ingredients_list(number_of_displayed, ingredients):
    """ list of recipe ingredients """
    lenght = len(ingredients)
    more = lenght > number_of_displayed
    return {
        'ingredients':
            ingredients[0:number_of_displayed - 1] if more else ingredients,
        'more': lenght - number_of_displayed + 1 if more else 0,
        'empty_row': range(0 if more else number_of_displayed - lenght)
    }


@register.inclusion_tag('vegetarian_cookbook/templatetags/range_slider.html')
def range_slider(**kwargs):
    """ show slider for search """
    return kwargs


@register.inclusion_tag('vegetarian_cookbook/templatetags/paginator.html')
def paginator(data):
    """ show page numbers links """
    return {'data': data}


@register.inclusion_tag(
    'vegetarian_cookbook/templatetags/recipe_energy_nutrients.html')
def recipe_energy_nutrients(size, show_legend, recipe):
    """ show recipe energy and nutrients """
    supernumber = 158
    energy = getattr(recipe, 'energy', 0)
    protein = getattr(recipe, 'protein', 0)
    fat = getattr(recipe, 'fat', 0)
    carbohydrate = getattr(recipe, 'carbohydrate', 0)
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


@register.inclusion_tag(
    'vegetarian_cookbook/templatetags/recipe_cooking_time.html')
def recipe_cooking_time(time):
    """ show coocing time """
    hours = 0
    minutes = time
    if time >= 60:
        hours = int((time - time % 60) / 60)
        minutes = time % 60
    return {
        'hours': hours,
        'minutes': minutes,
    }


@register.filter
def human_float(value, decimal=False):
    """ format float for human """
    if not decimal:
        return ('%f' % value).rstrip('0').rstrip('.')
    number = pow(10, int(decimal))
    if int(value * number) == int(value) * number:
        return int(round(value))
    return ("%0." + str(decimal) + 'f') % value


@register.simple_tag
def plural_form(value, number):
    """ plural form for units """
    if not value.plural:
        return value.name
    try:
        nplurals = appsettings.NPLURALS
        plural = appsettings.PLURAL
        plurals_array = value.plural.split(',')
        if nplurals == 2:
            return value.name if number == 1 else value.plural
        if int(number * 100) != int(number) * 100:
            return plurals_array[0]  # ??? only for ru?
        number = int(number)
        key = plural(number)
        return plurals_array[key-1]
    except TypeError:
        return value.name if number == 1 else value.plural
