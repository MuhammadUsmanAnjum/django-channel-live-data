from django.urls import path
from .consumer import MySyncConsumer


ws_urlpatterns = [
    path('ws/live-data/', MySyncConsumer.as_asgi())
]