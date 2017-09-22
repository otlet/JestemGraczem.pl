from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^cooperation/$', views.cooperation, name='service.cooperation'),
    url(r'^$', cache_page(60 * 1)(views.index), name='index'),
]
