import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from Chat.consumers import ChatRoomsConsumer, ChatRoomConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebChatBackend.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter([
                    re_path(r'ws/rooms/', ChatRoomsConsumer.as_asgi()),
                    re_path(r'ws/room/(?P<roomId>\w+)/$',
                            ChatRoomConsumer.as_asgi()),
                ])
            )
        ),
    }
)
