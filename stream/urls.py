from django.urls import path, register_converter
from django.views.decorators.cache import cache_page
from . import views, url_converters

register_converter(url_converters.Username, 'wacek')

urlpatterns = [
    path('mixer/<wacek:username>/', views.mixer, name='stream.mixer'),
    path('twitch/<str:username>/', views.twitch, name='stream.twitch'),
    path('live/', cache_page(60 * 1)(views.stream_api), name='stream.live'),
    path('live/esport', cache_page(60 * 10)(views.esport_stream_api), name='stream.live.esport'),
    path('<str:username>/', views.streamer, name='stream.streamer'),
    path('', views.index, name='stream.index'),
]
