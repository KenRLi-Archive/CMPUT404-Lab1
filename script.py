import requests

print("requests version: %s" % requests.__version__)

r = requests.get('http://www.google.com')

print("Status code: %s" % r.status_code)
print("URL Content: %s" % r.text)