
import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.scope["session"]["channel_name"] = self.channel_name
        self.scope["session"].save()
        self.accept()

    def disconnect(self, close_code):
        pass

    def chat_message(self, event_data):
        self.send(json.dumps(event_data))
        
