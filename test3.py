from urllib.request import urlopen
from decouple import config


channelID = 'UCUpJs89fSBXNolQGOYKn0YQ'


URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=10'.format(config('GOOGLEAPIKEY'), channelID)
response = urlopen(URL).read().decode('utf8')
# headers = {'Content-Type': 'charset=utf-8'}

# response = requests.get(URL).text


print(type(response))
print(response)