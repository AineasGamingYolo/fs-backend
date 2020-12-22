import django, sys, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'index.settings.development')
django.setup()

import requests
from django.conf import settings


API_ENDPOINT = "https://heytheremanwithoutawife.pythonanywhere.com/checker/"


data = {'public_key': settings.PUBLIC_KEY,
        'private_key': settings.PRIVATE_KEY,
        'web_domain': settings.WEB_DOMAIN}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text
api_url = r.text
print(api_url)