import json
import asyncio # Built-in python lib that allows for async code
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer

class ElevatorConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		# When socket connects
		print("Connected", event)
		print("Connected to Elevator socket")
		# This is needed to broadcast to group of users. Not just one on one
		await self.channel_layer.group_add(
			"broadcaster",
			self.channel_name
		)

		await self.send({
			"type": "websocket.accept"
		})

	# When msg is received from websocket
	async def websocket_receive(self, event):
		# When msg is received from websocket
		# This is what happens when socket.send happens from JS
		data = event.get("text", None) # Get the data from the even called "text" and default to None if there isn"t any
		if data is not None:
			loaded_dict_data = json.loads(data) # Load data into dict for better manipulation
			elevator_id = loaded_dict_data.get("elevator")
			current_status = loaded_dict_data.get("current_status")
			print("Elevator ID: ", elevator_id)
			print("Elevator status: ", current_status)
			new_status = None
			if current_status == "2": 
				new_status = 3
			elif current_status == "1":
				new_status = 2
			else:
				new_status = 1

			response = {
				"elevator_id": elevator_id,
				"new_status": new_status
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






# Implement later
class EscalatorConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		# When socket connects
		print("Connected", event)
		await self.send({
			"type": "websocket.accept"
		})

	async def websocket_receive(self, event):
		# When msg is received from websocket
		print("Receive", event) # This is what happens when socket.send happens from JS

	async def websocket_disconnect(self, event):
		# When socket disconnects
		print("Disconnected", event)


class BaggageBeltConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		# When socket connects
		print("Connected", event)
		await self.send({
			"type": "websocket.accept"
		})

	async def websocket_receive(self, event):
		# When msg is received from websocket
		print("Receive", event) # This is what happens when socket.send happens from JS

	async def websocket_disconnect(self, event):
		# When socket disconnects
		print("Disconnected", event)