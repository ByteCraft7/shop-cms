"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.apps import apps
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, resolve
from django.views.i18n import JavaScriptCatalog
from django.views.generic import TemplateView
from shop.apps.main.views import home
from debug_toolbar.toolbar import debug_toolbar_urls
from django.http import Http404, HttpResponseRedirect
from django.conf.urls import (handler404, handler500, handler403)
from django.contrib.sitemaps.views import sitemap
from shop.apps.main.sitemaps import SITEMAPS
from shop.apps.webinar.views import CreateRegistrationView
from django.views.generic import TemplateView

handler404 = 'shop.apps.main.views.not_found'
handler500 = 'shop.apps.main.views.server_error'
handler403 = 'shop.apps.main.views.unauthorized'

urlpatterns = i18n_patterns(
    path('sitemap.xml', sitemap, { "sitemaps": SITEMAPS }, name="django.contrib.sitemaps.views.sitemap"),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('select2/', include('django_select2.urls')),
    path('filer/', include('filer.urls')),
    path('accounts/', include('allauth.urls')),
    path('messages/', include('django_messages.urls')),
    path('careers/', TemplateView.as_view(template_name='main/career.html'), name="careers"),
    path('otp/', include((apps.get_app_config('otp').urls[0], 'otp'), namespace='otp')),
    path('membership/', include((apps.get_app_config('membership').urls[0], 'membership'), namespace='membership')),
    path('webinar/', CreateRegistrationView.as_view(), name='webinar'),
    path('webinar/thanks/', TemplateView.as_view(template_name='webinarthanks.html'), name='webinarthanks'),
    path('', include(apps.get_app_config('main').urls[0])),
    path('', include('djangocms_forms.urls')),
    path('', include('cms.urls')),
    path('volt/', include('admin_volt.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = debug_toolbar_urls() + urlpatterns
