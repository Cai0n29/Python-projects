

from bs4 import BeautifulSoup
import requests

print('Website Scraper 🌐')
print("Kindly input the website's url")

url = input()

print('What do you want to get from the website?')
print('title, text, structured HTML, URLs')

data = input()
request = requests.get(url)
html_doc = request.text
s = BeautifulSoup(html_doc)

if data == 'title':
    print(s.title)
elif data == 'text':
    print(s.get_text())
elif data == 'URLs':
    for links in s.find_all('a'):
        print(links.get('href'))
elif data == 'structured HTML':
    print(s.prettify())

