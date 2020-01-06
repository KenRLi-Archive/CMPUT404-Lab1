import requests

# print("requests version: %s" % requests.__version__)

# r = requests.get('http://www.google.com')

# print("Status code: %s" % r.status_code)
# print("URL Content: %s" % r.text)

r = requests.get('https://raw.githubusercontent.com/KenRLi/CMPUT404-Lab1/master/script.py')

# print("Status code: %s" % r.status_code)
print("GitHub Content:\n---\n%s\n---" % r.text)
