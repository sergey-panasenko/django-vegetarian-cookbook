##############################
Django Vegetarian Cookbook
##############################


Django application for the publication of vegetarian culinary recipes with the calculation of energy and nutrients.

********
Features
********

* manage ingridients, include ingridient nutrients and energy
* manage additional meashures
* manage recipes
* recipe category
* recipe tag
* show recipe
* calculate recipe energy

************
Requirements
************
- Python 3
- Django==2.0
- django-ajax-selects==1.7.0
- django-imagekit==4.0.2
- django-tinymce==2.7.0


************
Requirements
************
- Python 3
- Django==2.0
- django-ajax-selects==1.7.0
- django-imagekit==4.0.2
- django-tinymce==2.7.0

************
Installation
************

pip install django-vegetarian-cookbook

add apps in settings.py

    INSTALLED_APPS = [
        ...
        'vegetarian_cookbook',
        'bootstrap4',
        'imagekit',
        'tinymce',
        'ajax_select',
    ]

add url in urls.py

    from django.conf.urls import include

    urlpatterns = [
        path('', include('vegetarian_cookbook.urls')),
        path('admin/', admin.site.urls),
    ]

more info see in example app

https://github.com/sergey-panasenko/django-vegetarian-cookbook
