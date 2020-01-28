from urllib.request import urlopen
from decouple import config
# import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



video = 'YPMARa8Ex58'
URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}'.format(video, config('GOOGLEAPIKEY'))
res1 = urlopen(URL).read().decode('utf-8')
print(type(res1))
print(res1)
# response = urlopen(URL).read().decode('utf8')
# # response_to_json = json.loads(urlopen(URL).read().decode('utf8'))
# print(type(response))
# print(response)