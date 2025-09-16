from django.urls import re_path
from .consumers import TestingConsumer,ChatConsumer

websockets_urlpatterns = [
    re_path(r"ws/test/$" , TestingConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]