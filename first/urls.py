from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import home_page
from publications.views import publications

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home"),

    url(r'^publications/$', publications, name="publications"),
    url(r'accounts/', include('accounts.urls')),

    url(r'^redactor/', include('redactor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
