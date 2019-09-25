from channels.routing import route
from myapp.consumers import ws_add,ws_remove,ws_message

channel_routing = [
    route("websocket.receive", ws_message),
    route("websocket.connect",ws_add),
    route("websocket.disconnect",ws_remove),
]
