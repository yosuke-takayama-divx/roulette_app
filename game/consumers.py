import json
from channels.generic.websocket import AsyncWebsocketConsumer
import random

class RouletteConsumer(AsyncWebsocketConsumer):
    # 接続処理
    async def connect(self):
        self.group_name = 'roulette_group'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print(f"Client connected. Channel name: {self.channel_name}")  # チャンネル名をログに出力

    # 切断処理
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    # メッセージ受信処理
    async def receive(self, text_data):
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

            # 選ばれた武器情報をコンソールに出力
            print(f'{user_name}が選んだ武器: {selected_weapon["name"]}')

            # 選ばれた武器をグループに送信
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat_message',
                    'userName': user_name,
                    'index': index,
                    'image_name': selected_weapon['name'],
                    'image_path': selected_weapon['image_path']
                }
            )
        else:
            # 無効なデータを受け取った場合のエラーメッセージ
            error_message = 'Invalid data received'
            print(error_message)
            await self.send(text_data=json.dumps({
                'error': error_message
            }))

    async def chat_message(self, event):
        # グループからのメッセージをクライアントに送信
        await self.send(text_data=json.dumps({
            'userName': event['userName'],
            'index': event['index'],
            'image_name': event['image_name'],
            'image_path': event['image_path']
        }))