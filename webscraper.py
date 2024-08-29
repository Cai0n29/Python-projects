import streamlit as st

from bs4 import BeautifulSoup
import requests

st.title('Website Scraper 🌐')

url = st.text_input("Kindly input the website's url")
data = ''
if url == '':
    st.write('')
else:
    st.write('What do you want to get from the website?')

    data = st.text_input('title, text, structured HTML, URLs')
    request = requests.get(url)
    html_doc = request.text
    s = BeautifulSoup(html_doc)
    
if url == '' and data == '':
    st.write('Kidly enter a link ')
else:
    st.header('RESULTS')
    if data == 'title':
        st.write(s.title)
    elif data == 'text':
        st.write(s.get_text())
    elif data == 'URLs':
        for links in s.find_all('a'):
            st.write(links.get('href'))
    elif data == 'structured HTML':
        st.write(s.prettify())

