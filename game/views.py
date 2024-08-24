import random
from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def spin(request):
    images = [
        {'path': 'images/1.jpg', 'name': 'スプラシューター'},
        {'path': 'images/2.jpg', 'name': 'N-ZAP89'},
        {'path': 'images/3.jpg', 'name': 'ノヴァブラスター'}
    ]
    
    
    selected_image = random.choice(images)  # ランダムに画像を選ぶ
    return render(request, 'game/spin.html', {'selected_image': selected_image})