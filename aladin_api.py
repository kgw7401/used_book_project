import os
import requests
import json

TTBKey = os.getenv('TTBKey')


for i in range(5):
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType=ItemNewAll&SearchTarget=Used&SubSearchTarget=Book&MaxResults=50&start={i}&output=js&Version=20131101&OptResult=usedList"
    res = requests.get(url)
    print(res.status_code)
    item = json.loads(res.text)['item']
    print(item['title'])