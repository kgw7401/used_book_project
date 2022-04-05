import os
import requests
import json


def used_book_info(TTBKey):
    
    book_lists = []

    for i in range(10):
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType=ItemNewAll&SearchTarget=Used&SubSearchTarget=Book&MaxResults=50&start={i}&output=js&Version=20131101&OptResult=usedList"
        res = requests.get(url)
        items = json.loads(res.text)['item']

        for item in items:
            book_dict = {}
            book_dict['itemId'] = item['itemId']
            book_dict['title'] = item['title'][5:]
            book_dict['author'] = item['author'].split(',')[0].split('(')[0]
            book_dict['categoryName_large'] = item['categoryName'].split('>')[2] if len(item['categoryName'].split('>')) > 2 else "UNKNOWN"
            book_dict['categoryName_small'] = item['categoryName'].split('>')[3] if len(item['categoryName'].split('>')) > 3 else "UNKNOWN"
            book_dict['customerReviewRank'] = item['customerReviewRank']
            book_dict['priceSales'] = item['priceSales']
            book_dict['priceStandard'] = item['priceStandard']
            book_dict['pubDate'] = item['pubDate']
            book_dict['publisher'] = item['publisher']
            book_dict['aladinUsed_itemCount'] = int(item['subInfo']['usedList']['aladinUsed']['itemCount'])
            book_dict['userUsed_itemCount'] = int(item['subInfo']['usedList']['userUsed']['itemCount'])
            book_dict['userUsed_minPrice'] = item['subInfo']['usedList']['userUsed']['minPrice']

            book_lists.append(book_dict)
        print(f"{i}번째 배치 완료!")
    length = len(book_lists)
    print(f"총 {length}개의 데이터가 추출되었습니다.")
    return book_lists