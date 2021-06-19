DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbcq2mijooa3uv',
        'USER': 'xftfpxnthpanmw',
        'PASSWORD': '54eeda97939a37f93ec23b6630afd3730f5cd7af0a0802f69dfcb6f4ebd6e844',
        'HOST': 'ec2-54-155-226-153.eu-west-1.compute.amazonaws.com',
        'PORT': '5432'
    }
}

CLOUDINARY_STORAGE = {
  "CLOUD_NAME" : "hanseltech",
  "API_KEY" : "783254515677129",
  "API_SECRET" : "bSup9GMZSXgFhkPlP47e7M3fGR4"
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


MAX_ATTEMPTS = 1
BACKGROUND_TASK_RUN_ASYNC = True

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}