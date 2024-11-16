"""
Django settings for shop project.

Generated by 'djangocms' command using django CMS 4.1.2 and Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of Django settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

For the list of django CMS settings and their values, see
https://docs.django-cms.org/en/release-4.1.x/reference/configuration.html
"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from oscar.defaults import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import environ

env = environ.Env()
env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-0eh6bi(v$wrvxy!o!(ma+#ydupk6+9ap7(94-1c$mgktn)s2_l'
SECRET_KEY = env("SECRET_KEY", default='django-insecure-a3nr&5=rj!l%vfzw1h1ge(4&xsofn_^i_o(xf$5#m7r&o=tczx')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = []
DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=[])

# Application definition


INSTALLED_APPS = [
    'shop.apps.user',
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'dynamic_preferences',
    'dynamic_preferences.users.apps.UserPreferencesConfig',
    'djmoney',
    'localflavor',
    'formtools',
     # CMS base apps
    'cms',
    'menus',
    'django.forms',
    'djangocms_text_ckeditor',
    'djangocms_alias',
    'djangocms_versioning',

    'sekizai',
    'treebeard',
    'parler',

    #allauth apps
    'allauth',
    'allauth.account',

    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'filer',
    'easy_thumbnails',
    'djangocms_frontend',
    'djangocms_frontend.contrib.accordion',
    'djangocms_frontend.contrib.alert',
    'djangocms_frontend.contrib.badge',
    'djangocms_frontend.contrib.card',
    'djangocms_frontend.contrib.carousel',
    'djangocms_frontend.contrib.collapse',
    'djangocms_frontend.contrib.content',
    'djangocms_frontend.contrib.grid',
    'djangocms_frontend.contrib.icon',
    'djangocms_frontend.contrib.image',
    'djangocms_frontend.contrib.jumbotron',
    'djangocms_frontend.contrib.link',
    'djangocms_frontend.contrib.listgroup',
    'djangocms_frontend.contrib.media',
    'djangocms_frontend.contrib.navigation',
    'djangocms_frontend.contrib.tabs',
    'djangocms_frontend.contrib.utilities',
    # django-cms apps
    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    #'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    #'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    #'oscar_elasticsearch.search.apps.OscarElasticSearchConfig',
    'widget_tweaks',
    'haystack',
    #'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
    'compressor',
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_messages',
    'corsheaders',
    #'image_uploader_widget',
    #'pinax.referrals',
    #'pinax.invitations',
    #'account',
    'shop.apps.main',
    'shop.apps.wishlist',
    'shop.apps.catalogue.apps.CatalogueConfig',
    'shop.apps.partner.apps.PartnerConfig',
    'shop.apps.seller.apps.SellerConfig',
    'shop.apps.registration.apps.RegistrationConfig',
    #'shop.apps.invitation',
    'shop.apps.themezite69bs5',
    'shop.apps.otp.apps.OtpConfig',
    'shop.apps.membership.apps.MembershipConfig',
    'shop.apps.invitation.apps.InvitationConfig',
    'djangocms_form_builder',
]

if DEBUG:
    INSTALLED_APPS.insert(7, 'whitenoise.runserver_nostatic')

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'shop.apps.main.middleware.DynamicSiteMiddleware',
    'shop.apps.main.middleware.Zite69Middleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pinax.referrals.middleware.SessionJumpingMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

INSTALLED_APPS += env("INSTALLED_APPS", default=[])

AUTH_USER_MODEL = 'user.User'

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = [
    "127.0.0.1",
    ]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _req: DEBUG
}

ROOT_URLCONF = 'shop.urls'

default_loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
]

cached_loaders = [('django.template.loaders.cached.Loader', default_loaders)]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "shop", "templates"),
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'shop.apps.wishlist.context_processors.wishlists',
                'shop.apps.main.context_processors.settings',
                'oscar.core.context_processors.metadata',
                'dynamic_preferences.processors.global_preferences',
                'dealer.contrib.django.context_processor',
            ],
            'loaders': default_loaders if DEBUG else cached_loaders
        },
    },
]

#FORM_RENDERER = "django.forms.renderers.Jinja2DivFormRenderer"
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

WSGI_APPLICATION = 'shop.wsgi.application'

AUTHENTICATION_BACKENDS = (
    #'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'shop.apps.otp.auth.OtpBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/zite69',
        'ADMIN_URL': 'http://127.0.0.1:8393/solr/admin/cores',
        'INCLUDE_SPELLING': True,
    },
}
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3')
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ("en", _("English")),
    ("ml", _("Malayalam")),
    ("kn", _("Kannada")),
    ("ta", _("Tamil")),
    ("te", _("Telugu")),
    ("hi", _("Hindi"))
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = env("STATIC_ROOT", default="")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# This is a django CMS 4 template

CMS_CONFIRM_VERSION4 = True

# django CMS requires the site framework
# https://docs.django-cms.org/en/release-4.1.x/how_to/multi-site.html

SITE_ID = 1

SELLER_SITE_ID = 2
DEFAULT_SITE_ID = 1

#SELLER_DOMAIN = env("SELLER_DOMAIN", default="seller.local")
#DEFAULT_DOMAIN = env("DEFAULT_DOMAIN", default="localhost")
SESSION_COOKIE_DOMAIN = env("ROOT_DOMAIN", default=".zite69.com")

# A base template is part of this setup
# https://docs.django-cms.org/en/release-4.1.x/reference/configuration.html#cms-templates

CMS_TEMPLATES = (
    #("cms/home.html", _("Home")),
    ("cms/live_soon.html", _("Livesoon")),
    ("cms/landing.html", _("Landing")),
    ("cms/career.html", _("Career")),
    ("cms/mentor.html", _("Mentor")),
    ("cms/seller_home.html", _("Seller Home")),
    ("cms/generic.html", _("Generic")),
)

# Enable permissions
# https://docs.django-cms.org/en/release-4.1.x/topics/permissions.html

CMS_PERMISSION = True

# Allow admin sidebar to open admin URLs

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Enable inline editing with djangocms-text-ckeditor
# https://github.com/django-cms/djangocms-text-ckeditor#inline-editing-feature

TEXT_INLINE_EDITING = True

# Add project-wide static files directory
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-dirs

STATICFILES_DIRS = [
    BASE_DIR / "shop" / "static",
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


# Add project-wide static files directory
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root

MEDIA_URL = "media/"
#MEDIA_ROOT = str(BASE_DIR.parent / "media")
MEDIA_ROOT = env("MEDIA_ROOT", default=BASE_DIR.parent)

#OSCAR_HOMEPAGE = ''

#CMS_APPHOOKS = (
#    'cms.apphook_pool',
    # Add your apphook here
    #'shop.apps.main.cms_apphook_pool',
#)

WHATSAPP_NUMBER = '+918547299569'

LIVE = env("LIVE", default=False)
OSCAR_SHOP_NAME = "ZITE69"
OSCAR_SHOP_TAGLINE = "Super Social Marketplace"

OSCAR_DEFAULT_CURRENCY = 'INR'

#LOGGING = env.json("LOGGING", default={})
LOGGING_ENV = env.json("LOGGING", default={})

RAZORPAY_TEST = env("RAZORPAY_TEST", default=True)

if RAZORPAY_TEST:
    RAZORPAY_KEY = env("RAZORPAY_TEST_KEY")
    RAZORPAY_SECRET = env("RAZORPAY_TEST_SECRET")
else:
    RAZORPAY_KEY = env("RAZORPAY_KEY")
    RAZORPAY_SECRET = env("RAZORPAY_SECRET")

PHONENUMBER_DEFAULT_REGION = 'IN'
PHONENUMBER_DB_FORMAT = "RFC3966"
PHONENUMBER_DEFAULT_FORMAT = "RFC3966"

# Elasticsearch Configuration
#OSCAR_PRODUCT_SEARCH_HANDLER = "oscar_elasticsearch.search.search_handlers.ProductSearchHandler"
OSCAR_ELASTICSEARCH_FACETS = [
    {
        "name": "price",
        "label": "Price",
        "type": "range",
        "formatter": "oscar_elasticsearch.search.format.currency",
        "ranges": [
            25,
            100,
            500,
            1000
        ]
    },
    {
        "name": "attrs.gewicht",
        "label": "Gewicht",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.googleshopping",
        "label": "Google product",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.size",
        "label": "Maat",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.height",
        "label": "Hoogte",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.zult",
        "label": "Datum",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.stroomverbruik",
        "label": "Stroomverbruik",
        "type": "term",
        "ranges": []
    },
    {
        "name": "attrs.bijzonderheden",
        "label": "Bijzonderheden",
        "type": "term",
        "ranges": []
    }
]

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "oscar_elasticsearch.search.backend",
        "URLS": ["http://127.0.0.1:9200"],
        "INDEX": "zite69",
        "TIMEOUT": 120,
        "OPTIONS": {},
        "INDEX_SETTINGS": {},
        "ATOMIC_REBUILD": True,
        "AUTO_UPDATE": True,
    }
}

HAYSTACK_CONNECTIONS = {"default": {}}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

DJANGOCMS_FRONTEND_THEME = "shop.apps.themezite69bs5"
#DJANGOCMS_FRONTEND_FRAMEWORK = "shop.apps.themezite69bs5"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime}: {levelname} [{name}.{module}.{funcName}:{lineno}] {process:d} {thread:d} {message}',
            'style': '{'
        },
        'simple': {
            'format': '{levelname} [{name}.{module}.{funcName}:{lineno}] {message}',
            'style': '{'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            "include_html": True,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'root': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'oscar.checkout': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'WARNING',
        },
        'shop.apps.main': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'shop': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'shop.apps.otp': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'shop.apps.user': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'shop.apps.registration': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'shop.apps.seller': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

SHOW_REVISION = env("SHOW_REVISION", default=True)

CACHES_ENV = env.json("CACHES", default={})

if CACHES_ENV:
    CACHES = {}
    CACHES['default'] = CACHES_ENV

#allauth settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

#Dynamic preferences
DYNAMIC_PREFERENCES = {

    # a python attribute that will be added to model instances with preferences
    # override this if the default collide with one of your models attributes/fields
    'MANAGER_ATTRIBUTE': 'preferences',

    # The python module in which registered preferences will be searched within each app
    'REGISTRY_MODULE': 'dynamic_preferences_registry',

    # Allow quick editing of preferences directly in admin list view
    # WARNING: enabling this feature can cause data corruption if multiple users
    # use the same list view at the same time, see https://code.djangoproject.com/ticket/11313
    'ADMIN_ENABLE_CHANGELIST_FORM': False,

    # Customize how you can access preferences from managers. The default is to
    # separate sections and keys with two underscores. This is probably not a settings you'll
    # want to change, but it's here just in case
    'SECTION_KEY_SEPARATOR': '__',

    # Use this to disable auto registration of the GlobalPreferenceModel.
    # This can be useful to register your own model in the global_preferences_registry.
    'ENABLE_GLOBAL_MODEL_AUTO_REGISTRATION': True,

    # Use this to disable caching of preference. This can be useful to debug things
    'ENABLE_CACHE': True,

    # Use this to select which chache should be used to cache preferences. Defaults to default.
    'CACHE_NAME': 'default',

    # Use this to disable checking preferences names. This can be useful to debug things
    'VALIDATE_NAMES': True,
}
PORT = env("PORT", default=8000)

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS", default=[])
if not CORS_ALLOWED_ORIGINS:
   for host in ALLOWED_HOSTS:
       CORS_ALLOWED_ORIGINS.append(f"http://{host}:{PORT}")

CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS", default=False)
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", default=[])

DEALER_TYPE = "git"

WIZARD_STEP = env("WIZARD_STEP", default="")

from email.utils import parseaddr
ADMINS_ENV = env("ADMINS", default="")
ADMINS = tuple(parseaddr(email) for email in ADMINS_ENV.split(","))

MANAGERS_ENV = env("MANAGERS", default="")
MANAGERS = tuple(parseaddr(email) for email in MANAGERS_ENV.split(","))

SERVER_EMAIL = env("SYSTEM_EMAIL_ADDRESS")
DEFAULT_FROM_EMAIL = env("SYSTEM_EMAIL_ADDRESS")
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX")
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST = env("EMAIL_HOST", default="email-smtp.ap-south-1.amazonaws.com")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)

SMS_AUTH_KEY = env("SMS_AUTH_KEY", default="")
SMS_AUTH_TOKEN = env("SMS_AUTH_TOKEN", default="")
SMS_SENDER_ID = env("SMS_SENDER_ID", default="")
SMS_LOGIN_OTP_TEMPLATE = env("SMS_LOGIN_OTP_TEMPLATE", default="Your OTP to login is {otp}")
SMS_VALIDATE_PHONE_OTP = env("SMS_VALIDATE_PHONE_OTP", default="Your ZITE69 account verification OTP code is {otp}. Code is valid for 10 minutes only, one time use. Please DO NOT share this OTP with anyone-ZITE69.com")
SMS_LIVE=env("SMS_LIVE", default=False)

USE_HTTPS=env("USE_HTTPS", default=False)
IP_ADDRESS_META_FIELD=env("IP_ADDRESS_META_FIELD", default="REMOTE_ADDR")

ZITE69_MAIN_SELLER = env("ZITE69_MAIN_SELLER", default="Zite69 Main Seller")
ZITE69_MAIN_SELLER_ID = env("ZITE69_MAIN_SELLER_ID", default=1)
ZITE69_MAIN_USER_ID = env("ZITE69_MAIN_USER_ID", default=1)
ZITE69_MAIN_USERNAME = env("ZITE69_MAIN_USERNAME", default="system")

ZITE69_MAIN_DOMAIN = env("ZITE69_MAIN_DOMAIN", default="www.zite69.com")
ZITE69_SELLER_DOMAIN = env("ZITE69_SELLER_DOMAIN", default="seller.zite69.com")

if ZITE69_MAIN_DOMAIN not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(ZITE69_MAIN_DOMAIN)

if ZITE69_SELLER_DOMAIN not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(ZITE69_SELLER_DOMAIN)

PLAUSIBLE_TAG = env.str("PLAUSIBLE_TAG", default="", multiline=True)

if DEBUG == False:
    #Setup production logging
    LOGGING['handlers']['file'] = {
            'level': env("LOG_LEVEL", default="WARNING"),
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': env("LOG_FILE", default="logs/all.log")
    }
    for module in LOGGING_ENV.keys():
        LOGGING['loggers'][module]['handlers'] = ['file']
        LOGGING['loggers'][module]['level'] = LOGGING_ENV.get(module, "WARNING")

    #Setup production email
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
    EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
    MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"
