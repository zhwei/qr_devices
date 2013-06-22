from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qr.views.home', name='home'),
    # url(r'^qr/', include('qr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/',include('tinymce.urls')),

    # device
    url(r'^d/', include('qr.devices.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
