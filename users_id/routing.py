import channels.generic.websocket
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/',consumers.MyConsumer.as_asgi()),
    re_path(r'ws/id/',consumers.SecondConsumer.as_asgi()),
]