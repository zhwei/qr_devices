from django.conf.urls import patterns, include, url
from views import DetailDevice



urlpatterns =  patterns('qr.devices.views',

            url(r'^(?P<pk>\d+)$', DetailDevice.as_view()),

            url(r'^c/(?P<id>\d+)$','get_qr_code', name="get_qr_code"),
            )
# url(r'^(?P<pk>\d+)$',DetailView.as_view(
#     model=Post,
#     template_name = "blog.html"))
