import requests
url = 'http://www.omdbapi.com/?apikey=aad18307&t=hackers'



r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key + ' :', value)
    
    
