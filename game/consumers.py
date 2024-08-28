import json
from channels.generic.websocket import WebsocketConsumer
import random

class RouletteConsumer(WebsocketConsumer):
    connected_users = {}  # 接続されているユーザーの情報を保持する辞書

    def connect(self):
        print("Connect method called")  # デバッグ用
        self.accept()
        print(f"Client connected. Channel name: {self.channel_name}")  # チャンネル名をログに出力
        # 他の接続処理...

    def disconnect(self, close_code):
        print("Client disconnected.")  # デバッグ用
        # ユーザーが切断された時の処理

    def receive(self, text_data):
        print("Receive method called")  # デバッグ用
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

            # ユーザー情報を接続ユーザー辞書に追加
            self.connected_users[index] = user_name

            # 選ばれた武器を送信
            self.send(text_data=json.dumps({
                'userName': user_name,
                'index': index,
                'image_name': selected_weapon['name'],
                'image_path': selected_weapon['image_path']
            }))
        else:
            # 無効なデータを受け取った場合のエラーメッセージ
            error_message = 'Invalid data received'
            print(error_message)
            self.send(text_data=json.dumps({
                'error': error_message
            }))