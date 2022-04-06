import os
import requests
import json
import psycopg2
from dotenv import load_dotenv


def used_book_info(TTBKey):

    book_lists = []

    for i in range(1, 11):
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType=ItemNewAll&SearchTarget=Used&SubSearchTarget=Book&MaxResults=50&start={i}&output=js&Version=20131101&OptResult=usedList"
        res = requests.get(url)
        items = json.loads(res.text)['item']

        for item in items:
            book_dict = {}
            book_dict['itemid'] = item['itemId']
            book_dict['title'] = item['title'][5:]
            book_dict['author'] = item['author'].split(',')[0].split('(')[0]
            book_dict['categoryname_large'] = item['categoryName'].split('>')[2] if len(item['categoryName'].split('>')) > 2 else "UNKNOWN"
            book_dict['categoryname_small'] = item['categoryName'].split('>')[3] if len(item['categoryName'].split('>')) > 3 else "UNKNOWN"
            book_dict['customer_review_rank'] = item['customerReviewRank']
            book_dict['pricesales'] = item['priceSales']
            book_dict['pricestandard'] = item['priceStandard']
            book_dict['pubdate'] = item['pubDate']
            book_dict['publisher'] = item['publisher']
            book_dict['aladinused_itemcount'] = int(item['subInfo']['usedList']['aladinUsed']['itemCount'])
            book_dict['userused_itemcount'] = int(item['subInfo']['usedList']['userUsed']['itemCount'])
            book_dict['userused_minprice'] = item['subInfo']['usedList']['userUsed']['minPrice']

            book_lists.append(book_dict)
        print(f"{i}번째 배치 완료!")
    length = len(book_lists)
    print(f"총 {length}개의 데이터가 추출되었습니다.")
    return book_lists


def insert_row(cursor, data):
    col = ', '.join(data)
    place_holders = ', '.join(['%s']*len(data))
    key_holders = ', '.join([k+'=%s' for k in data.keys()])
    que = 'INSERT INTO used_book ({}) VALUES ({}) ON CONFLICT (itemid) DO UPDATE SET {}'.format(col, place_holders, key_holders)
    cursor.execute(que, list(data.values())*2)

def main():
    load_dotenv()
    TTBKey = os.environ.get("TTBKey")
    book_lists = used_book_info(TTBKey)

    host = os.environ.get('host')
    port = os.environ.get('port')
    user = os.environ.get('user')
    database = os.environ.get('database')
    password = os.environ.get('password')

    conn = psycopg2.connect(host=host, user=user, password=password,
                        dbname=database, port=port)
    cursor = conn.cursor()

    print("DB에 저장중...")

    for book_info in book_lists:
        insert_row(cursor, book_info)
        conn.commit()
    cursor.close()
    conn.close()

    print("저장 완료!")


if __name__ == "__main__":
    main()