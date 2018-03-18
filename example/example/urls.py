# Django Vegetarian Cookbook, Copyright © 2018 Sergey Panasenko. Contacts: <sergey.panasenko@gmail.com>
# License: https://opensource.org/licenses/AGPL-3.0

from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('', include('vegetarian_cookbook.urls')),
    path('admin/', admin.site.urls),
]
