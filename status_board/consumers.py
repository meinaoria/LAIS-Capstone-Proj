import json
import asyncio # Built-in python lib that allows for async code
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

# class elevatorConsumer(AsyncConsumer):
#    async def websocket_connect(self, event):
#         # When socket connects
#         print("Connected", event)
#
#         await self.channel_layer.group_add(
#             'elevatorBroadcaster',
#             self.channel_name
#         )
#
#         await self.send({
#             "type": "websocket.accept"
#         })
#
#    async def websocket_receive(self, event):
#        # When message is received from websocket
#        print("Received", event)
#        data = event.get("text", None)  # Get the data from the event called "text" and default to None if there isn"t any
#        if data is not None:
#            loaded_dict_data = json.loads(data)
#            elevatorID = loaded_dict_data.get('elevatorID')
#            elevatorStatus = loaded_dict_data.get('elevatorStatus')
#            fromCon = 'elevator'
#            response = {
#                "elevatorID": elevatorID,
#                'elevatorStat': elevatorStatus,
#                'fromCon': fromCon,
#            }
#            # Broadcasts message
#            await self.channel_layer.group_send(
#                "elevatorBroadcaster",
#                {
#                    "type": "elevatorBroadcaster_message",
#                    "text": json.dumps(response)
#                }
#            )
#
#    async def elevatorBroadcaster_message(self, event):
#        # Sends actual message
#        await self.send({
#            "type": "websocket.send",
#            "text": event['text']
#        })
#
#    async def websocket_disconnect(self, event):
#        # When socket disconnects
#        print("Disconnected", event)
#        raise StopConsumer

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
           if (loaded_dict_data.get('from') == 'bridge'):
               bridgeTableID = loaded_dict_data.get('bridgeTableID')
               bridgeStatus = loaded_dict_data.get('bridgeStat')
               fromCon = 'bridgeTable'
               response = {
                   "bridgeTableID": bridgeTableID,
                   'bridgeStat': bridgeStatus,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'pca'):
               bridgeTableID = loaded_dict_data.get('bridgeTableID')
               pcaStat = loaded_dict_data.get('pcaStat')
               fromCon = 'pcaTable'
               response = {
                   "bridgeTableID": bridgeTableID,
                   'pcaStat': pcaStat,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'gpu'):
               bridgeTableID = loaded_dict_data.get('bridgeTableID')
               gpuStat = loaded_dict_data.get('gpuStat')
               fromCon = 'gpuTable'
               response = {
                   "bridgeTableID": bridgeTableID,
                   'gpuStat': gpuStat,
                   'fromCon': fromCon,
               }
           elif(loaded_dict_data.get('from') == 'mes'):
                    msgID = loaded_dict_data.get('mesID')
                    msg = loaded_dict_data.get('msg')
                    fromCon = 'msg'
                    response= {
                        'msgID':msgID,
                        'msg':msg,
                        'fromCon': fromCon,
                    }  
           elif (loaded_dict_data.get('from') == 'elev'):
               elevatorID = loaded_dict_data.get('elevatorID')
               elevatorStatus = loaded_dict_data.get('elevatorStat')
               fromCon = 'elevator'
               response = {
                   "elevatorID": elevatorID,
                   'elevatorStat': elevatorStatus,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'esc'):
               escalatorID = loaded_dict_data.get('escalatorID')
               escalatorStatus = loaded_dict_data.get('escalatorStatus')
               fromCon = 'escalator'
               response = {
                   "escalatorID": escalatorID,
                   'escalatorStat': escalatorStatus,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'domIntBag'):
               domIntBagId = loaded_dict_data.get('domIntBaggageID')
               domIntBagStat = loaded_dict_data.get('domIntBaggageStat')
               fromCon = 'domIntBag'
               response = {
                   "domIntBagId": domIntBagId,
                   'domIntBagStat': domIntBagStat,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'tbBag'):
               tbBagID = loaded_dict_data.get('tbBagID')
               tbBagStatus = loaded_dict_data.get('tbBagStat')
               fromCon = 'tbBag'
               response = {
                   "tbBagID": tbBagID,
                   'tbBagStat': tbBagStatus,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'domIntOversize'):
               domIntOversizeID = loaded_dict_data.get('domIntOversizeID')
               domIntOversizeStat = loaded_dict_data.get('domIntOversizeStat')
               fromCon = 'domIntOversize'
               response = {
                   "domIntOversizeID": domIntOversizeID,
                   'domIntOversizeStat': domIntOversizeStat,
                   'fromCon': fromCon,
               }
           elif (loaded_dict_data.get('from') == 'tbOversize'):
               tbOversizeID = loaded_dict_data.get('tbOversizeID')
               tbOversizeStat = loaded_dict_data.get('tbOversizeStat')
               fromCon = 'tbOversize'
               response = {
                   "tbOversizeID": tbOversizeID,
                   'tbOversizeStatus': tbOversizeStat,
                   'fromCon': fromCon,
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







