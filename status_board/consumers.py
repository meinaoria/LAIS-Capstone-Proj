import json
import asyncio # Built-in python lib that allows for async code
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class bridgeTableConsumer(AsyncConsumer):
   async def websocket_connect(self, event):
        # When socket connects
        print("Connected", event)

        await self.channel_layer.group_add(
            'broadcaster',
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

   async def websocket_receive(self, event):
       # When message is received from websocket
       print("Received", event)
       data = event.get("text", None)  # Get the data from the event called "text" and default to None if there isn"t any
       if data is not None:
           loaded_dict_data = json.loads(data)
           bridgeTableID = loaded_dict_data.get('bridgeTable_ID')
           #bridgeStatus = loaded_dict_data.get(yes)

           response = {
               "bridgeTableID": bridgeTableID,
             #  "new_bridgeStatus": bridgeStatus
           }
           # Broadcasts message
           await self.channel_layer.group_send(
               "broadcaster",
               {
                   "type": "broadcast_message",
                   "text": json.dumps(response)
               }
           )

   async def broadcast_message(self, event):
       # Sends actual message
       await self.send({
           "type": "websocket.send",
           "text": event['text']
       })

   async def websocket_disconnect(self, event):
       # When socket disconnects
       print("Disconnected", event)
       raise StopConsumer

#Elevator Consumer
class bridgeTableConsumer(AsyncConsumer):
   async def websocket_connect(self, event):
        # When socket connects
        print("Connected", event)

        await self.channel_layer.group_add(
            'broadcaster',
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

   async def websocket_receive(self, event):
       # When message is received from websocket
       print("Received", event)
       data = event.get("text", None)  # Get the data from the event called "text" and default to None if there isn"t any
       if data is not None:
           loaded_dict_data = json.loads(data)
           bridgeTableID = loaded_dict_data.get('bridgeTableID')
           bridgeStatus = loaded_dict_data.get('bridgeStat')
           pcaStatus = loaded_dict_data.get('pcaStat')
           gpuStatus = loaded_dict_data.get('gpuStat')

           response = {
               "bridgeTableID": bridgeTableID,
               'bridgeStat': bridgeStatus,
               'pcaStat': pcaStatus,
               'gpuStat': gpuStatus,
           }
           # Broadcasts message
           await self.channel_layer.group_send(
               "broadcaster",
               {
                   "type": "broadcast_message",
                   "text": json.dumps(response)
               }
           )

   async def broadcast_message(self, event):
       # Sends actual message
       await self.send({
           "type": "websocket.send",
           "text": event['text']
       })

   async def websocket_disconnect(self, event):
       # When socket disconnects
       print("Disconnected", event)
       raise StopConsumer







