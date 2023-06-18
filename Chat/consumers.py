from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatRoomsConsumer(WebsocketConsumer):
    """ List rooms consumer """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.room_group_name = None

    def connect(self):
        self.room_group_name = 'Rooms'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass


class ChatRoomConsumer(WebsocketConsumer):
    """ Room consumer """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.room_group_name = None

    def connect(self):
        room_id = self.scope['url_route']['kwargs']['roomId']
        self.room_group_name = f'Room-{room_id}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass
