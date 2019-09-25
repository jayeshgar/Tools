from channels.routing import route
from apollo.consumers import ws_message,ws_add,ws_remove
channel_routing = [
    route("websocket.receive", ws_message),
    route("websocket.connect",ws_add),
    route("websocket.disconnect",ws_remove),

]
