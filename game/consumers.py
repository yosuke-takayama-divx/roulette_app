import json
from channels.generic.websocket import AsyncWebsocketConsumer
import random

class RouletteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'roulette_group'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print(f"Client connected. Channel name: {self.channel_name}")  # チャンネル名をログに出力

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print("Client disconnected.")  # デバッグ用

    async def receive(self, text_data):
        print("Receive method called")  # デバッグ用
        text_data_json = json.loads(text_data)
        user_name = text_data_json.get('userName')
        index = text_data_json.get('index')

        if user_name is not None and index is not None:
            # ランダムな武器を選択（例として固定のデータを使用）
            weapons = [
                {"name": "ボールドマーカー", "image_path": "images/1.jpeg"},
                {"name": "ボールドマーカーネオ", "image_path": "images/2.jpeg"},
                {"name": "わかばシューター", "image_path": "images/3.jpeg"},
                {"name": "もみじシューター", "image_path": "images/4.jpeg"},
                {"name": "シャープマーカー", "image_path": "images/5.jpeg"},
                {"name": "シャープマーカーネオ", "image_path": "images/6.jpeg"},
                {"name": "プロモデラーMG", "image_path": "images/7.jpeg"},
                {"name": "プロモデラーRG", "image_path": "images/8.jpeg"},
                {"name": "スプラシューター", "image_path": "images/9.jpeg"},
                {"name": "スプラシューターコラボ", "image_path": "images/10.jpeg"},
                {"name": ".52ガロン", "image_path": "images/11.jpeg"},
                {"name": ".52ガロンデコ", "image_path": "images/12.jpeg"},
                {"name": "N-ZAP85", "image_path": "images/13.jpeg"},
                {"name": "N-ZAP89", "image_path": "images/14.jpeg"},
                {"name": "プライムシューター", "image_path": "images/15.jpeg"},
                {"name": "プライムシューターコラボ", "image_path": "images/16.jpeg"},
                {"name": ".96ガロン", "image_path": "images/17.jpeg"},
                {"name": ".96ガロンデコ", "image_path": "images/18.jpeg"},
                {"name": "ジェットスイーパー", "image_path": "images/19.jpeg"},
                {"name": "ジェットスイーパーカスタム", "image_path": "images/20.jpeg"},
                {"name": "スペースシューター", "image_path": "images/21.jpeg"},
                {"name": "スペースシューターコラボ", "image_path": "images/22.jpeg"},
                {"name": "L3リールガン", "image_path": "images/23.jpeg"},
                {"name": "L3リールガンD", "image_path": "images/24.jpeg"},
                {"name": "H3リールガン", "image_path": "images/25.jpeg"},
                {"name": "H3リールガンD", "image_path": "images/26.jpeg"},
                {"name": "ボトルガイザー", "image_path": "images/27.jpeg"},
                {"name": "ボトルガイザーフォイル", "image_path": "images/28.jpeg"},
                {"name": "カーボンローラー", "image_path": "images/29.jpeg"},
                {"name": "カーボンローラーデコ", "image_path": "images/30.jpeg"},
                {"name": "スプラローラー", "image_path": "images/31.jpeg"},
                {"name": "スプラローラーコラボ", "image_path": "images/32.jpeg"},
                {"name": "ダイナモローラー", "image_path": "images/33.jpeg"},
                {"name": "ダイナモローラーテスラ", "image_path": "images/34.jpeg"},
                {"name": "ヴァリアブルローラー", "image_path": "images/35.jpeg"},
                {"name": "ヴァリアブルローラーフォイル", "image_path": "images/36.jpeg"},
                {"name": "ワイドローラー", "image_path": "images/37.jpeg"},
                {"name": "ワイドローラーコラボ", "image_path": "images/38.jpeg"},
                {"name": "スクイックリン", "image_path": "images/39.jpeg"},
                {"name": "スクイックリンβ", "image_path": "images/40.jpeg"},
                {"name": "スプラチャージャー", "image_path": "images/41.jpeg"},
                {"name": "スプラチャージャーコラボ", "image_path": "images/42.jpeg"},
                {"name": "スプラスコープ", "image_path": "images/43.jpeg"},
                {"name": "スプラスコープコラボ", "image_path": "images/44.jpeg"},
                {"name": "リッター4K", "image_path": "images/45.jpeg"},
                {"name": "リッター4Kカスタム", "image_path": "images/46.jpeg"},
                {"name": "4Kスコープ", "image_path": "images/47.jpeg"},
                {"name": "4Kスコープカスタム", "image_path": "images/48.jpeg"},
                {"name": "14式竹筒銃・甲", "image_path": "images/49.jpeg"},
                {"name": "14式竹筒銃・乙", "image_path": "images/50.jpeg"},
                {"name": "ソイチューバー", "image_path": "images/51.jpeg"},
                {"name": "ソイチューバーカスタム", "image_path": "images/52.jpeg"},
                {"name": "R-PEN/5H", "image_path": "images/53.jpeg"},
                {"name": "R-PEN/5B", "image_path": "images/54.jpeg"},
                {"name": "バケットスロッシャー", "image_path": "images/55.jpeg"},
                {"name": "バケットスロッシャーデコ", "image_path": "images/56.jpeg"},
                {"name": "ヒッセン", "image_path": "images/57.jpeg"},
                {"name": "ヒッセン・ヒュー", "image_path": "images/58.jpeg"},
                {"name": "スクリュースロッシャー", "image_path": "images/59.jpeg"},
                {"name": "スクリュースロッシャーネオ", "image_path": "images/60.jpeg"},
                {"name": "オーバーフロッシャー", "image_path": "images/61.jpeg"},
                {"name": "オーバーフロッシャーデコ", "image_path": "images/62.jpeg"},
                {"name": "エクスプロッシャー", "image_path": "images/63.jpeg"},
                {"name": "エクスプロッシャーカスタム", "image_path": "images/64.jpeg"},
                {"name": "モップリン", "image_path": "images/65.jpeg"},
                {"name": "モップリンD", "image_path": "images/66.jpeg"},
                {"name": "スプラスピナー", "image_path": "images/67.jpeg"},
                {"name": "スプラスピナーコラボ", "image_path": "images/68.jpeg"},
                {"name": "バレルスピナー", "image_path": "images/69.jpeg"},
                {"name": "バレルスピナーデコ", "image_path": "images/70.jpeg"},
                {"name": "ハイドラント", "image_path": "images/71.jpeg"},
                {"name": "ハイドラントカスタム", "image_path": "images/72.jpeg"},
                {"name": "クーゲルシュライバー", "image_path": "images/73.jpeg"},
                {"name": "クーゲルシュライバー・ヒュー", "image_path": "images/74.jpeg"},
                {"name": "ノーチラス47", "image_path": "images/75.jpeg"},
                {"name": "ノーチラス79", "image_path": "images/76.jpeg"},
                {"name": "イグザミナー", "image_path": "images/77.jpeg"},
                {"name": "イグザミナー・ヒュー", "image_path": "images/78.jpeg"},
                {"name": "スパッタリー", "image_path": "images/79.jpeg"},
                {"name": "スパッタリー・ヒュー", "image_path": "images/80.jpeg"},
                {"name": "スプラマニューバー", "image_path": "images/81.jpeg"},
                {"name": "スプラマニューバーコラボ", "image_path": "images/82.jpeg"},
                {"name": "ケルビン525", "image_path": "images/83.jpeg"},
                {"name": "ケルビン525デコ", "image_path": "images/84.jpeg"},
                {"name": "デュアルスイーパー", "image_path": "images/85.jpeg"},
                {"name": "デュアルスイーパーカスタム", "image_path": "images/86.jpeg"},
                {"name": "クアッドホッパーブラック", "image_path": "images/87.jpeg"},
                {"name": "クアッドホッパーホワイト", "image_path": "images/88.jpeg"},
                {"name": "ガエンFF", "image_path": "images/89.jpeg"},
                {"name": "ガエンFFカスタム", "image_path": "images/90.jpeg"},
                {"name": "パラシェルター", "image_path": "images/91.jpeg"},
                {"name": "パラシェルターソレーラ", "image_path": "images/92.jpeg"},
                {"name": "キャンピングシェルター", "image_path": "images/93.jpeg"},
                {"name": "キャンピングシェルターソレーラ", "image_path": "images/94.jpeg"},
                {"name": "スパイガジェット", "image_path": "images/95.jpeg"},
                {"name": "スパイガジェットソレーラ", "image_path": "images/96.jpeg"},
                {"name": "24式張替傘・甲", "image_path": "images/97.jpeg"},
                {"name": "24式張替傘・乙", "image_path": "images/98.jpeg"},
                {"name": "ノヴァブラスター", "image_path": "images/99.jpeg"},
                {"name": "ノヴァブラスターネオ", "image_path": "images/100.jpeg"},
                {"name": "ホットブラスター", "image_path": "images/101.jpeg"},
                {"name": "ホットブラスターカスタム", "image_path": "images/102.jpeg"},
                {"name": "ロングブラスター", "image_path": "images/103.jpeg"},
                {"name": "ロングブラスターカスタム", "image_path": "images/104.jpeg"},
                {"name": "クラッシュブラスター", "image_path": "images/105.jpeg"},
                {"name": "クラッシュブラスターネオ", "image_path": "images/106.jpeg"},
                {"name": "ラピッドブラスター", "image_path": "images/107.jpeg"},
                {"name": "ラピッドブラスターデコ", "image_path": "images/108.jpeg"},
                {"name": "Rブラスターエリート", "image_path": "images/109.jpeg"},
                {"name": "Rブラスターエリートデコ", "image_path": "images/110.jpeg"},
                {"name": "S-BLAST92", "image_path": "images/111.jpeg"},
                {"name": "S-BLAST91", "image_path": "images/112.jpeg"},
                {"name": "パブロ", "image_path": "images/113.jpeg"},
                {"name": "パブロ・ヒュー", "image_path": "images/114.jpeg"},
                {"name": "ホクサイ", "image_path": "images/115.jpeg"},
                {"name": "ホクサイ・ヒュー", "image_path": "images/116.jpeg"},
                {"name": "フィンセント", "image_path": "images/117.jpeg"},
                {"name": "フィンセント・ヒュー", "image_path": "images/118.jpeg"},
                {"name": "トライストリンガー", "image_path": "images/119.jpeg"},
                {"name": "トライストリンガーコラボ", "image_path": "images/120.jpeg"},
                {"name": "LACT-450", "image_path": "images/121.jpeg"},
                {"name": "LACT-450デコ", "image_path": "images/122.jpeg"},
                {"name": "フルイドV", "image_path": "images/123.jpeg"},
                {"name": "フルイドVカスタム", "image_path": "images/124.jpeg"},
                {"name": "ジムワイパー", "image_path": "images/125.jpeg"},
                {"name": "ジムワイパー・ヒュー", "image_path": "images/126.jpeg"},
                {"name": "ドライブワイパー", "image_path": "images/127.jpeg"},
                {"name": "ドライブワイパーデコ", "image_path": "images/128.jpeg"},
                {"name": "デンタルワイパーミント", "image_path": "images/129.jpeg"},
                {"name": "デンタルワイパースミ", "image_path": "images/130.jpeg"},
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