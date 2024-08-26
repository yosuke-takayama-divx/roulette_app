import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-*#t_e!44+h72w8@iuzt4(1s%zzt_!2eyfvyvwu0=2olzq^7ee*'  # Keep this secret in production
DEBUG = True

ALLOWED_HOSTS = [
    'test-splroulette001-7c4e722641b8.herokuapp.com',
    '127.0.0.1',
    'localhost',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'corsheaders',  # CORSヘッダーを使用するアプリを追加
    'game'
]

# CORSの設定
CORS_ALLOWED_ORIGINS = [
    "https://test-splroulette001-7c4e722641b8.herokuapp.com",  # HerokuのURLを明記
    "http://127.0.0.1:8000",  # ローカル開発用
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORSミドルウェアを最初に追加
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Channelsの設定
ASGI_APPLICATION = 'spl_roulette.asgi.application'  # プロジェクトのasgi.pyへのパス

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [(os.environ.get('REDIS_URL', '127.0.0.1'), 6379)],
#         },
#     },
# }
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.environ.get('REDIS_URL', 'redis://localhost:6379'))],
        },
    },
}

ROOT_URLCONF = 'spl_roulette.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'spl_roulette.wsgi.application'

# Database
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL')
#     )
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spl',  # データベース名
        'USER': 'postgres',  # 作成したユーザー名
        'PASSWORD': 'pass',  # 作成したユーザーのパスワード
        'HOST': 'localhost',  # ホスト名
        'PORT': '5432',  # ポート番号
    }
}



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
