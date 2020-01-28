from urllib.request import urlopen
from decouple import config
import json
import sys
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

video = 'q0rT5RW46Ag'
URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}'.format(video, config('GOOGLEAPIKEY'))
response = urlopen(URL).read().decode('utf-8')
res_dict = json.loads(response)


########## youtube 카테고리 분류를 알아보자
print(res_dict.get('items')[0].get('snippet').get('categoryId'))



##### json 출력 로직
# PATH = 'zzzz.json'
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
#     json.dump(res_dict, file, indent="\t", ensure_ascii=False)