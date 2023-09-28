from channels.consumer import SyncConsumer, StopConsumer
from asgiref.sync import async_to_sync
from .models import Record
from channels.layers import get_channel_layer
import json

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("channel layer -->", self.channel_layer)
        print("channel name -->", self.channel_name)
        async_to_sync(self.channel_layer.group_add)("prog", self.channel_name)
        self.send({
            "type": "websocket.accept"
        })


    def websocket_disconnect(self, event):
        print("channel layer -->", self.channel_layer)
        print("channel name -->", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)("prog", self.channel_name)
        raise StopConsumer()


    def websocket_receive(self, event):
        
        async_to_sync(self.channel_layer.group_send)("prog", {
            'type': 'chat.message',
            'message': event['text']
        })
    

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
        

    
def model_post_save_handler(sender, instance, **kwargs):
    rec = {"name":instance.name, "balance":instance.balance}
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "prog",
        {
            "type": "chat.message",
            "message": json.dumps(rec)
        }),
   

