from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/ttt/connect', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/ttt/play', consumers.ChatConsumer.as_asgi()),
]