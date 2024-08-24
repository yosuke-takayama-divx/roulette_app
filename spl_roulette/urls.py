# urls.py

from django.contrib import admin
from django.urls import path
from game import views
from django.conf import settings
from django.conf.urls.static import static
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from game import consumers  # 追加: consumersをインポート

# HTTPリクエストのURLパターン
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('spin/', views.spin, name='spin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# ASGI websocketの設定を行います
websocket_urlpatterns = [
    path('ws/roulette/', consumers.RouletteConsumer.as_asgi()),
]

# ASGIアプリケーションを設定する場合は、別のファイル（asgi.py）で定義する必要があります。
