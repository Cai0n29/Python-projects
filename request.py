import requests
url = "http://www.datacamp.com/teach/documentation"
r = requests.get(url)
text = r.text
print(text)