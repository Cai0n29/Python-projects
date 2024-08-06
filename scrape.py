#Importing the packages 
from bs4 import BeautifulSoup
import requests

# The URL
url = 'https://www.python.org/~guido/'
#Using the get request to get request and package a response
r = requests.get(url)

# Extracts the response 
html_doc = r.text

#Create a BeautifulSoup object from the HTML
s = BeautifulSoup(html_doc)

# Printing the structured html using the method prettify
pretty_soup = s.prettify()
print(pretty_soup)
#Getting the text in the HTML
print(s.get_text())

# Getting the title
print(s.title)

# Getting the url in the html the 'a'
for links in s.find_all('a'):
    print(links.get('href'))