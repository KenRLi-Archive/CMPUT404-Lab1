# CMPUT 404 - Lab 1
# Ken Li

import requests

# Question 2 & 3
print("> requests version: %s" % requests.__version__)

# cURL - Step 5
print("\n\n> cURL - Step 5")
r = requests.get('http://www.google.com')
print("Status code: %s" % r.status_code)
print("URL Content: %s" % r.text)

# cURL - Step 10
print("\n\n> cURL - Step 10")
r = requests.get('https://raw.githubusercontent.com/KenRLi/CMPUT404-Lab1/master/script.py')
print("Status code: %s" % r.status_code)
print("GitHub Content:\n---\n%s---" % r.text)