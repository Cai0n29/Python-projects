from urllib.request import urlopen, Request
url = 'https://en.wikipedia.org/wiki/Egypt'
request = Request(url)
response = urlopen(request)
html = response.read()
print(response)
print(html)