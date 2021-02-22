"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from django.urls import reverse_lazy  # reverse url을 초기화 이후로 미뤄주는 함수!
import os
from os.path import normpath, join
import sys
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# secrets.json의 경로
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRETS_PATH = os.path.join(ROOT_DIR, 'secrets.json')
# json파일을 파이썬 객체로 변환
secrets = json.loads(open(SECRETS_PATH).read())

# json파일은 dict로 변환되므로, .items()를 호출해 나온 key와 value를 사용해
# settings모듈에 동적으로 할당
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    
    'channels',

    'myApp',
    'user',
    'place',
    'chat',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


# '''
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             os.path.join(BASE_DIR, 'config'),
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# '''

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '15.164.11.168', '3.36.2.44'] # ALLOWED_HOST = [*]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'config', 'templates'), os.path.join(BASE_DIR, 'user', 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'config', 'static'),
# ]

# STATICFILES_DIRS = (
#     normpath(join(BASE_DIR, 'config')),
#     normpath(join(BASE_DIR, 'static')),
# )


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = normpath(join(BASE_DIR, 'static'))

STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Login


LOGIN_URL = '/accounts/login/'  # 기본값
LOGOUT_URL = '/accounts/logout/'  # 기본값
LOGIN_REDIRECT_URL = reverse_lazy('myApp:main_list')  # 반드시 정의할 것!
LOGOUT_REDIRECT_URL = reverse_lazy('myApp:main_list')


# # AUTH : Socil login
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# SITE_ID = 4
# LOGIN_REDIRECT_URL = '/'


# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     },
#     'naver': {
#         'SCOPE': [
#             'profile',
#             'email',
#             'nickname',
#             'id',
#             'profile_image'

#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     },
#     # 'kakao': {
#     #     'SCOPE': [
#     #         'email',
#     #         # 'profileImageUrl',  // HTTPS만 지원


#     #     ],
#     #     'AUTH_PARAMS': {
#     #         'access_type': 'online',
#     #     }
#     # }
# }


# # ACCOUNT_SIGNUP_FORM_CLASS = 'myApp.forms.ProfileForm'
# # SOCIALACCOUNT_FORMS = {'signup': 'myApp.forms.ProfileForm'}
# # ACCOUNT_FORMS = {'signup': 'myApp.forms.ProfileForm'}


# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = "email"
# SOCIALACCOUNT_AUTO_SIGNUP = True

# # SOCIALACCOUNT_FORMS = {'signup': 'accounts.forms.MySocialCustomSignupForm'}
# # ACOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.MySocialCustomSignupForm'


SESSION_COOKIE_SECURE = False


########### CUSTOM USER #############
AUTH_USER_MODEL = 'user.User'

########### all-auth #############
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 3
LOGIN_REDIRECT_URL = '/'

# LOGIN_REDIRECT_URL = 'home'

# user email instead of username for authentification

# email
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True  # email mandatory


# username
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_USERNAME = False
ACCOUNT_USERNAME_VALIDATORS = None

SOCIALACCOUNT_AUTO_SIGNUP = True  # get additional information for signup


# TODO: 회원가입 폼 클래스를 지정하고 해당 클래스는 def signup(self, request, user) 메소드를 반드시 구현해야 한다.
# ACCOUNT_SIGNUP_FORM_CLASS = accounts.forms.SignupForm

ACCOUNT_FORMS = {'signup': 'user.forms.MyCustomSignupForm', }

# SOCIALACCOUNT_FORMS = {'signup': 'user.forms.MyCustomSocialSignupForm', }

# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300


######### PROVIDER ########
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'naver': {
        'SCOPE': [
            'profile',
            'email',
            'nickname',
            'id',
            'profile_image'

        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    # 'kakao': {
    #     'SCOPE': [
    #         'email',
    #         # 'profileImageUrl',  // HTTPS만 지원


    #     ],
    #     'AUTH_PARAMS': {
    #         'access_type': 'online',
    #     }
    # }
}




# SOCIALACCOUNT_ADAPTER = "user.adapter.MyCustomSocialAccountAdapter"


# WEBCHAT
# Channels
ASGI_APPLICATION = 'config.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = (
    'localhost:8000',
    '127.0.0.1:8000',
)

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
      '127.0.0.1:8000',
)

CORS_ALLOW_HEADERS = (
    'access-control-allow-credentials',
    'access-control-allow-origin',
    'access-control-request-method',
    'access-control-request-headers',
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'connection',
    'content-type',
    'dnt',
    'credentials',
    'host',
    'origin',
    'user-agent',
    'X-CSRFToken',
    'csrftoken',
    'x-requested-with',
)
