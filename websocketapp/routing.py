from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    path("ws/",consumers.StudentConsumer.as_asgi()),
    # re_path(r"ws/$",consumers.StudentConsumer.as_asgi())
]