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
* search recipes by many parameters

************
Requirements
************
- Python 3
- Django==2.0
- django-ajax-selects==1.7.0
- -e git://github.com:sergey-panasenko/django-ajaximage.git#egg=ajaximage
- django-appconf==1.0.2
- django-bootstrap4==0.0.6
- django-imagekit==4.0.2
- django-tinymce==2.7.0
- olefile==0.45.1
- pilkit==2.0
- Pillow==5.1.0
- pytz==2018.4
- six==1.11.0
- whitenoise==3.3.1

************
Installation
************

pip install django-vegetarian-cookbook

add apps in settings.py

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'vegetarian_cookbook',
        'bootstrap4',
        'ajaximage',
        'imagekit',
        'tinymce',
        'ajax_select',
    ]

add url in urls.py

.. code-block:: python

    from django.conf.urls import include

    urlpatterns = [
        path('', include('vegetarian_cookbook.urls')),
        path('admin/', admin.site.urls),
    ]

more info see in example app

https://github.com/sergey-panasenko/django-vegetarian-cookbook
