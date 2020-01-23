from urllib.request import urlopen
from decouple import config
import json
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



video = 'YPMARa8Ex58'
URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}'.format(video, config('GOOGLEAPIKEY'))
response = urlopen(URL).read().decode('utf-8')
res_dict = json.loads(response)
# print(response)
PATH = 'zzzz.json'
with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
    json.dump(res_dict, file, indent="\t", ensure_ascii=False)
# # response = urlopen(URL).read().decode('utfs8')
# # # response_to_json = json.loads(urlopen(URL).read().decode('utf8'))
# # print(type(response))
# # print(response)