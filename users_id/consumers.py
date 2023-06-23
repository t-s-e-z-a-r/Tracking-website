from channels.generic.websocket import WebsocketConsumer
from django.db import connection
import json
from asgiref.sync import async_to_sync

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "global1"
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()
        
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update1',
                'message': 'fsafsf'
            }
        )
    def update1(self, event):
        results = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users_id_user_url")
            rows = cursor.fetchall()
        for row in rows:
            User_pk = row[0]
            ID_User = row[1]
            result = {
                "User_pk": User_pk,
                'ID_User': ID_User,
            }
            results.append(result)
        self.send(text_data=json.dumps(results))


class SecondConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "global2"
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()
        
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update2',
                'message': message
            }
        )
    def update2(self, event):
        message = event['message']
        results = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users_id_url")
            rows = cursor.fetchall()
            results = [row[1] for row in rows if int(row[2]) == int(message)]
            cursor.execute(f"SELECT * FROM users_id_user_url")
            rows = cursor.fetchall()
            User_id = None
            for row in rows:
                if int(row[0]) == int(message):
                    User_id = row[1]
                    break


        self.send(text_data=json.dumps({
            'type': 'Update',
            'message': results,
            'id': User_id,
        }))
    def send_request(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            "type": 'send_request'
        }))