"""NSND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from functools import partial

from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView
from django.views.defaults import page_not_found, server_error

from .core import views



sitemaps = {}

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/home.html"), name="home"),
    path("pripojit-podpis/", TemplateView.as_view(template_name="core/sign.html"), name="sign"),
    path("argumentar/", views.FAQ.as_view(), name="faq"),
    path("argumentar/fotka/<slug>/", views.FAQImage.as_view(), name="faq-image"),
    path("admin/", admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path("404/", partial(page_not_found, exception=None)),
        path("500/", server_error),
    ]
