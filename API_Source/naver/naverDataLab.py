import os
import sys
import urllib.request
from decouple import config
import json
from pprint import pprint

client_id = config("NAVER_DATALAB_CLIENT_ID")
client_secret = config("NAVER_DATALAB_CLIENT_SECRET")

url = "https://openapi.naver.com/v1/datalab/search";

startDate = '2019-01-01'
endDate = '2019-12-31'
timeUnit = 'week'
keyword = '피지컬갤러리'

body = {
    "startDate": startDate,
    "endDate": endDate,
    "timeUnit": timeUnit,
    "keywordGroups": [
            {
                "groupName": keyword, 
                "keywords": [
                        keyword
                    ]
            }
        ]
}

body = str(body).replace("'", '\"')


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read().decode('utf-8')
    data = json.loads(response_body).get('results')[0].get('data') 
    data = {'data': data} 
    insert_data = json.dumps(data) # insert_data를 DB data에 담는다.
    print(len(insert_data))
else:
    print("Error Code:" + rescode)