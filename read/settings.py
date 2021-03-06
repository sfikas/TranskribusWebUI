"""
Django settings for read project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wqu(q!hn%1we=&48qm@qigap_(t#+hq1ljxda-3w+k)#uh!&j0'

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
    'bootstrap3',
    'library',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'read.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
    		"library.context_processors.language_form_context_processor",
            ],
	    'libraries' : {
		'library_tags': 'library.templatetags',
	    },
        },
    },
]

WSGI_APPLICATION = 'read.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

LANGUAGE_CODE = 'en'
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
	('bg', _('Bulgarian')),
	('hr', _('Croatian')),
	('cs', _('Czech')),
	('da', _('Danish')),
	('nl', _('Dutch')),
	('en', _('English')),
	('et', _('Estonian')),
	('fi', _('Finnish')),
	('fr', _('French')),
	('de', _('German')),
	('el', _('Greek')),
	('hu', _('Hungarian')),
	('ga', _('Irish')),
	('it', _('Italian')),
	('lv', _('Latvian')),
	('lt', _('Lithuanian')),
#	('mt', _('Maltese')), NO MALTESE IN DJANGO
	('pl', _('Polish')),
	('pt', _('Portuguese')),
	('ro', _('Romanian')),
	('sk', _('Slovak')),
	('sl', _('Slovenian')),
	('es', _('Spanish')),
	('sv', _('Swedish')),
];

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

#TODO for when use is heavier use memcached
#Enable cache
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}
#and cache session
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# This assumes per app view for these... may promote this sttuff to their own app...??
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'

### Auth backend that logs in to transkribus.eu and extends the django.contrib.auth.User
AUTHENTICATION_BACKENDS = [
    'library.backends.TranskribusBackend',
#    'django.contrib.auth.backends.ModelBackend',
]

### parameters for services
#transkribus rest service
TRP_URL = 'https://transkribus.eu/TrpServer/rest/'

#### offline fallbacks for dev on train
OFFLINE = False
ADMIN_LOGIN = 'admin'
ADMIN_PASSWORD = 'norsun'
TEST_USER_JSON = '{"trpUserLogin": {"userId": "65", "userName": "rory.mcnicholl@gmail.com", "email": "rory.mcnicholl@gmail.com", "affiliation": "None", "firstname": "Rory", "lastname": "McNicholl", "gender": "male", "isActive": "1", "isAdmin": "false", "created": {"nanos": "0"}, "loginTime": "2016-04-18T09:05:45.152+02:00", "userAgent": "python-requests/2.9.1", "ip": "213.205.251.21"}'

TEST_USER_XML = '<trpUserLogin><userId>65</userId><userName>rory.mcnicholl@gmail.com</userName><email>rory.mcnicholl@gmail.com</email><affiliation>None</affiliation><firstname>Snory</firstname><lastname>McNicholl</lastname><gender>male</gender><isActive>1</isActive><isAdmin>false</isAdmin><created><nanos>0</nanos></created><loginTime>2016-04-18T19:59:25.356+02:00</loginTime><sessionId>0B93CDB4DB05EF4993E86421369F825F</sessionId><userAgent>python-requests/2.9.1</userAgent><ip>213.205.251.21</ip></trpUserLogin>'

TEST_COLLECTIONS_JSON = '[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX","role":"Transcriber"},{"colId":4,"colName":"Transkribus Cloud","defaultForApp":"ALL","role":"Transcriber"}]'

TEST_COLLECTION_JSON = '[{"docId":331,"title":"Bentham Test 1","author":"Jeremy Bentham","uploadTimestamp":1425300460373,"uploader":"ucl","uploaderId":49,"nrOfPages":47,"language":"Spanish","status":0,"fimgStoreColl":"TrpDoc_DEA_331","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":332,"title":"Bentham Test 2","author":"Jeremy Bentham","uploadTimestamp":1425300463323,"uploader":"ucl","uploaderId":49,"nrOfPages":53,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_332","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":333,"title":"Bentham Test 3","uploadTimestamp":1425300466367,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"German","status":0,"fimgStoreColl":"TrpDoc_DEA_333","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":334,"title":"Bentham Test 4","uploadTimestamp":1425300469322,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_334","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":335,"title":"Bentham Test 5","uploadTimestamp":1425302178563,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_335","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":336,"title":"Bentham Test 6","uploadTimestamp":1425302181428,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_336","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":337,"title":"Bentham Test 7","uploadTimestamp":1425302184387,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_337","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},{"docId":338,"title":"Bentham Test 8","uploadTimestamp":1425302187442,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_338","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}}]'

TEST_FULL_DOC_XML = '<trpDoc><md><docId>4949</docId><title>IMAGES</title><uploadTimestamp>1461833612964</uploadTimestamp><uploader>rory.mcnicholl@gmail.com</uploader><uploaderId>65</uploaderId><nrOfPages>4</nrOfPages><status>0</status><fimgStoreColl>TrpDoc_DEA_4949</fimgStoreColl><createdFromTimestamp>0</createdFromTimestamp><createdToTimestamp>0</createdToTimestamp><collectionList><colList><colId>2305</colId><colName>WebUITestCollection</colName><description>created by rory.mcnicholl@gmail.com</description></colList></collectionList></md><pageList><pages><pageId>150822</pageId><docId>4949</docId><pageNr>1</pageNr><key>AYRSUTRYDXCOLVUTDIVBLGAG</key><url>https://dbis-thure.uibk.ac.at/f/Get?id=AYRSUTRYDXCOLVUTDIVBLGAG&amp;fileType=view</url><thumbUrl>https://dbis-thure.uibk.ac.at/f/Get?id=AYRSUTRYDXCOLVUTDIVBLGAG&amp;fileType=thumb</thumbUrl><imgFileName>096_002_001.jpg</imgFileName><tsList><transcripts><tsId>216733</tsId><parentTsId>-1</parentTsId><key>NSZISDRQJVVWUJUQJRQBWQPZ</key><pageId>150822</pageId><docId>4949</docId><pageNr>1</pageNr><url>https://dbis-thure.uibk.ac.at/f/Get?id=NSZISDRQJVVWUJUQJRQBWQPZ</url><status>NEW</status><userName>rory.mcnicholl@gmail.com</userName><userId>65</userId><timestamp>1461833612964</timestamp><md5Sum></md5Sum></transcripts></tsList></pages><pages><pageId>150823</pageId><docId>4949</docId><pageNr>2</pageNr><key>FMQEVHZHLMRSNRTPGUMEHLQH</key><url>https://dbis-thure.uibk.ac.at/f/Get?id=FMQEVHZHLMRSNRTPGUMEHLQH&amp;fileType=view</url><thumbUrl>https://dbis-thure.uibk.ac.at/f/Get?id=FMQEVHZHLMRSNRTPGUMEHLQH&amp;fileType=thumb</thumbUrl><imgFileName>096_002_002.jpg</imgFileName><tsList><transcripts><tsId>216734</tsId><parentTsId>-1</parentTsId><key>UNYBRRLEYVBABRZLSAHELDLX</key><pageId>150823</pageId><docId>4949</docId><pageNr>2</pageNr><url>https://dbis-thure.uibk.ac.at/f/Get?id=UNYBRRLEYVBABRZLSAHELDLX</url><status>NEW</status><userName>rory.mcnicholl@gmail.com</userName><userId>65</userId><timestamp>1461833612964</timestamp><md5Sum></md5Sum></transcripts></tsList></pages><pages><pageId>150824</pageId><docId>4949</docId><pageNr>3</pageNr><key>FNGETAKAWQJRDWPUGXIYVIAE</key><url>https://dbis-thure.uibk.ac.at/f/Get?id=FNGETAKAWQJRDWPUGXIYVIAE&amp;fileType=view</url><thumbUrl>https://dbis-thure.uibk.ac.at/f/Get?id=FNGETAKAWQJRDWPUGXIYVIAE&amp;fileType=thumb</thumbUrl><imgFileName>096_002_003.jpg</imgFileName><tsList><transcripts><tsId>216735</tsId><parentTsId>-1</parentTsId><key>NMWCNNFDPCJPPCTJZWXFKSMZ</key><pageId>150824</pageId><docId>4949</docId><pageNr>3</pageNr><url>https://dbis-thure.uibk.ac.at/f/Get?id=NMWCNNFDPCJPPCTJZWXFKSMZ</url><status>NEW</status><userName>rory.mcnicholl@gmail.com</userName><userId>65</userId><timestamp>1461833612964</timestamp><md5Sum></md5Sum></transcripts></tsList></pages><pages><pageId>150825</pageId><docId>4949</docId><pageNr>4</pageNr><key>GEACFLYSDMALUEYAPNDAJWJH</key><url>https://dbis-thure.uibk.ac.at/f/Get?id=GEACFLYSDMALUEYAPNDAJWJH&amp;fileType=view</url><thumbUrl>https://dbis-thure.uibk.ac.at/f/Get?id=GEACFLYSDMALUEYAPNDAJWJH&amp;fileType=thumb</thumbUrl><imgFileName>096_002_004.jpg</imgFileName><tsList><transcripts><tsId>216736</tsId><parentTsId>-1</parentTsId><key>NHLSHSCKNCDRXKJFOPBCXEVW</key><pageId>150825</pageId><docId>4949</docId><pageNr>4</pageNr><url>https://dbis-thure.uibk.ac.at/f/Get?id=NHLSHSCKNCDRXKJFOPBCXEVW</url><status>NEW</status><userName>rory.mcnicholl@gmail.com</userName><userId>65</userId><timestamp>1461833612964</timestamp><md5Sum></md5Sum></transcripts></tsList></pages></pageList><collection><colId>2305</colId><colName>WebUITestCollection</colName><description>created by rory.mcnicholl@gmail.com</description></collection></trpDoc>'

TEST_FULL_DOC_JSON = '{"md":{"docId":338,"title":"Bentham Test 8","uploadTimestamp":1425302187442,"uploader":"ucl","uploaderId":49,"nrOfPages":100,"language":"Unknown","status":0,"fimgStoreColl":"TrpDoc_DEA_338","createdFromTimestamp":0,"createdToTimestamp":0,"collectionList":{"colList":[{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},{"colId":1890,"colName":"D2.4","description":"created by upvlc"}]}},"pageList":{"pages":[{"pageId":5911,"docId":338,"pageNr":1,"key":"ZGOYFRRQNNEIGCRJZUDOBBHN","url":"https://dbis-thure.uibk.ac.at/f/Get?id=ZGOYFRRQNNEIGCRJZUDOBBHN&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=ZGOYFRRQNNEIGCRJZUDOBBHN&fileType=thumb","imgFileName":"112_030_001.jpg","tsList":{"transcripts":[]}},{"pageId":5912,"docId":338,"pageNr":2,"key":"YJBEOEOCLTJUJKTALSLGCBTM","url":"https://dbis-thure.uibk.ac.at/f/Get?id=YJBEOEOCLTJUJKTALSLGCBTM&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=YJBEOEOCLTJUJKTALSLGCBTM&fileType=thumb","imgFileName":"112_032_001.jpg","tsList":{"transcripts":[]}},{"pageId":5913,"docId":338,"pageNr":3,"key":"BMKYBWBTIKOXZCHOVDHVLUZV","url":"https://dbis-thure.uibk.ac.at/f/Get?id=BMKYBWBTIKOXZCHOVDHVLUZV&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=BMKYBWBTIKOXZCHOVDHVLUZV&fileType=thumb","imgFileName":"112_037_001.jpg","tsList":{"transcripts":[]}},{"pageId":5914,"docId":338,"pageNr":4,"key":"ILHHUMSTGCJFTZKVGDUSGWMB","url":"https://dbis-thure.uibk.ac.at/f/Get?id=ILHHUMSTGCJFTZKVGDUSGWMB&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=ILHHUMSTGCJFTZKVGDUSGWMB&fileType=thumb","imgFileName":"112_040_001.jpg","tsList":{"transcripts":[]}},{"pageId":5915,"docId":338,"pageNr":5,"key":"DDDFCQPBHAORRXTJLNZBSLVR","url":"https://dbis-thure.uibk.ac.at/f/Get?id=DDDFCQPBHAORRXTJLNZBSLVR&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=DDDFCQPBHAORRXTJLNZBSLVR&fileType=thumb","imgFileName":"112_041_001.jpg","tsList":{"transcripts":[]}},{"pageId":5916,"docId":338,"pageNr":6,"key":"FVPNGCAOQTKPPNYFHEUALHKE","url":"https://dbis-thure.uibk.ac.at/f/Get?id=FVPNGCAOQTKPPNYFHEUALHKE&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=FVPNGCAOQTKPPNYFHEUALHKE&fileType=thumb","imgFileName":"112_042_001.jpg","tsList":{"transcripts":[]}},{"pageId":5917,"docId":338,"pageNr":7,"key":"HPFEAPMEXYEVCFYBQFIAUXMJ","url":"https://dbis-thure.uibk.ac.at/f/Get?id=HPFEAPMEXYEVCFYBQFIAUXMJ&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=HPFEAPMEXYEVCFYBQFIAUXMJ&fileType=thumb","imgFileName":"112_055_001.jpg","tsList":{"transcripts":[]}},{"pageId":5918,"docId":338,"pageNr":8,"key":"ERAUYNZOZPSMPVWACOCVKBAZ","url":"https://dbis-thure.uibk.ac.at/f/Get?id=ERAUYNZOZPSMPVWACOCVKBAZ&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=ERAUYNZOZPSMPVWACOCVKBAZ&fileType=thumb","imgFileName":"112_091_001.jpg","tsList":{"transcripts":[]}},{"pageId":6010,"docId":338,"pageNr":100,"key":"HLIFONKWWASVLKZWUXUQQWQX","url":"https://dbis-thure.uibk.ac.at/f/Get?id=HLIFONKWWASVLKZWUXUQQWQX&fileType=view","thumbUrl":"https://dbis-thure.uibk.ac.at/f/Get?id=HLIFONKWWASVLKZWUXUQQWQX&fileType=thumb","imgFileName":"114_291_001.jpg","tsList":{"transcripts":[]}}]},"collection":{"colId":3,"colName":"Bentham","description":"Bentham documents for TSX","defaultForApp":"TSX"},"edDeclList":[]}'

TEST_PAGE_JSON = '[]'
TEST_TRANSCRIPT=''
