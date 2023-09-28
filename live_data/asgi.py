import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from myapp.routing import ws_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'live_data.settings')

application = get_asgi_application()
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(ws_urlpatterns)
    # Just HTTP for now. (We can add other protocols later.)
})