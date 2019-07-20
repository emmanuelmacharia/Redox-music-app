"""
Definition of urls for MusicProjects.
"""

from datetime import datetime
from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import  static

import music.forms
import music.views


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^', include('music.urls')), 
    url(r'^music/', include('music.urls')),
    url(r'ralbums/', include('music.urls')),
    url(r'rsongs/', include('music.urls')),
    #url(r'^index', include('music.urls')),
    #url(r'^contact$', music.views.contact, name='contact'),
    #url(r'^about', music.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'music/login.html',
    #        'authentication_form': music.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings. STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)