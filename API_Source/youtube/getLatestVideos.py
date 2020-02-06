from urllib.request import urlopen
from decouple import config
import json


# channeID로 최신 동영상 가져오기


channelID = 'UCUpJs89fSBXNolQGOYKn0YQ'
KEY = config('GOOGLEAPIKEY')
maxResult = 10 # 가져올 동영상의 수  
order = 'date'
URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order={}&maxResults={}'.format(KEY, channelID, order, maxResult)
response = urlopen(URL).read().decode('utf8')
# headers = {'Content-Type': 'charset=utf-8'}
# response = requests.get(URL).text
PATH = 'latestVideoTest.json'
with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
    json.dump(json.loads(response), file, indent="\t", ensure_ascii=False)
# print(response)
