from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

from .models import SiteProfile


admin.site.unregister(Site)


class SiteProfileInline(admin.StackedInline):
    model = SiteProfile
    min_num = 1
    max_num = 1


@admin.register(Site)
class NSNDSiteAdmin(SiteAdmin):
    inlines = (SiteProfileInline,)
