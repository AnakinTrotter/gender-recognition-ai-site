import requests

r = requests.get('http://gender-recognition-ai.herokuapp.com/ping-test', 'This request does nothing.')
print(r.text)