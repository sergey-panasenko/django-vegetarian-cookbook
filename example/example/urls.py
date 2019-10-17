"""
Django Vegetarian Cookbook, Copyright © 2018 Sergey Panasenko.
Contacts: <sergey.panasenko@gmail.com>
License: https://opensource.org/licenses/AGPL-3.0
"""

from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('vegetarian_cookbook.urls'), name='recipes'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
