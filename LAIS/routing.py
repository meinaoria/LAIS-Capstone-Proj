from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from status_board.consumers import bridgeTableConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"$", bridgeTableConsumer),
                    url(r"^update/bridge/(?P<bridgeTableID>[\w.@+-]+)/$", bridgeTableConsumer),

                ]
            )
        )
    )
})