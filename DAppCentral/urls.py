"""DAppCentral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

from DAppCentral.settings import common

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html'),
        name='core_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='core_logout'),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
    path('sotadmin/', include('sotadmin.urls')),
    path('', views.index, name="index"),
] + static(common.STATIC_URL, document_root=common.STATIC_ROOT)
