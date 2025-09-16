
import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

django_application = get_asgi_application()
from core.routing import websockets_urlpatterns
from core.middleware import JWTAuthMiddleware
application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    "websocket": JWTAuthMiddleware(
        AuthMiddlewareStack(
            URLRouter(websockets_urlpatterns)
        )
    )
})
