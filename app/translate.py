import json
import requests
from flask_babel import _
from app import app
import urllib.parse

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    api_key = app.config['MS_TRANSLATOR_KEY']
    text = urllib.parse.quote(text)
    r = requests.get('https://translation.googleapis.com/language/translate/v2?source={}&target={}&key={}&q={}'.format(
                         source_language, dest_language, api_key, text))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    ans = json.loads(r.content.decode('utf-8-sig'))
    return ans.get('data').get('translations')[0].get('translatedText')