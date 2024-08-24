import json
from channels.generic.websocket import WebsocketConsumer
import random

class RouletteConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_name = text_data_json.get('userName')
        index = text_data_json.get('index')

        if user_name is not None and index is not None:
            # ランダムな武器を選択（例として固定のデータを使用）
            weapons = [
                {"name": "スプラシューター", "image_path": "images/1.jpg"},
                {"name": "N-ZAP85", "image_path": "images/2.jpg"},
                {"name": "ノヴァブラスター", "image_path": "images/3.jpg"},
            ]
            selected_weapon = random.choice(weapons)

            self.send(text_data=json.dumps({
                'userName': user_name,
                'index': index,
                'image_name': selected_weapon['name'],
                'image_path': selected_weapon['image_path']
            }))
        else:
            self.send(text_data=json.dumps({
                'error': 'Invalid data received'
            }))