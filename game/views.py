import random
from django.shortcuts import render

def index(request):
    # 環境変数からWebSocketのURLを取得
    websocket_url = os.getenv('WEBSOCKET_URL')
    
    # 環境変数が設定されていない場合のデフォルト値を設定
    if not websocket_url:
        protocol = 'wss://' if request.is_secure() else 'ws://'
        websocket_url = protocol + request.get_host() + '/ws/roulette/'
    
    return render(request, 'game/index.html', {'websocket_url': websocket_url})

def spin(request):
    images = [
        {'path': 'images/1.jpg', 'name': 'スプラシューター'},
        {'path': 'images/2.jpg', 'name': 'N-ZAP89'},
        {'path': 'images/3.jpg', 'name': 'ノヴァブラスター'}
    ]
    
    
    selected_image = random.choice(images)  # ランダムに画像を選ぶ
    return render(request, 'game/spin.html', {'selected_image': selected_image})