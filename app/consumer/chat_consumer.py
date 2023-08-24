async def receive(self, text_data):
    sender = self.scope['user'].username
    message = text_data.strip()

    # Register the message in the database.
    chat_room = ChatRoom.objects.get(id=self.room_id)
    message = Message.objects.create(room=chat_room, sender=self.scope['user'], content=message)

    # Broadcast message to a room group
    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'send_message',
            'message': f'{sender}: {message.content}'
        }
    )