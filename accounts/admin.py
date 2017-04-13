from django.contrib import admin

from accounts.models import User, SiteGlobalConfig

from solo.admin import SingletonModelAdmin


admin.site.register(User)
admin.site.register(SiteGlobalConfig, SingletonModelAdmin)
