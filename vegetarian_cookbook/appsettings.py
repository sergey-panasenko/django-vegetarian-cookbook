from django.conf import settings
from django.utils.translation import gettext as _

try:
    recipes_in_list = settings.RECIPES_IN_LIST
except:
    recipes_in_list = 6

try:
    ingredients_in_list = settings.INGREDIENTS_IN_LIST
except:
    ingredients_in_list = 20

try:
    seo_description = settings.SEO_DESCRIPTION
except:
    seo_description = _('The best proven vegetarian recipes with calculation of calories and nutrients.')

try:
    seo_keywords = settings.SEO_KEYWORDS
except:
    seo_keywords = _('recipe, culinary, cookbook, vegetarian food, vegan, raw food, raw diet, vegetarianism, diet, healthy food,')
