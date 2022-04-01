import os
import requests
import json

TTBKey = os.getenv("TTBKey")


def used_book_info(TTBKey):
    book_lists = []

    for i in range(5):
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType=ItemNewAll&SearchTarget=Used&SubSearchTarget=Book&MaxResults=50&start={i}&output=js&Version=20131101&OptResult=usedList"
        res = requests.get(url)
        print(res.status_code)
        items = json.loads(res.text)["item"]

        for item in items:
            book_dict = {}

            book_dict["title"] = item["title"][5:]
            book_dict["author"] = item["author"].split(",")[0].split()[0]
            book_dict["categoryName_large"] = item["categoryName"].split(">")[2]
            book_dict["categoryName_small"] = item["categoryName"].split(">")[3]
            book_dict["customerReviewRank"] = item["customerReviewRank"]
            book_dict["priceSales"] = item["priceSales"]
            book_dict["priceStandard"] = item["priceStandard"]
            book_dict["pubDate"] = item["pubDate"]
            book_dict["publisher"] = item["publisher"]
            book_dict["aladinUsed_itemCount"] = item["subInfo"]["usedList"]["aladinUsed"]["itemCount"]
            book_dict["aladinUsed_itemCount"] = item["subInfo"]["usedList"]["userUsed"]["itemCount"]
            book_dict["userUsed_minPrice"] = item["subInfo"]["usedList"]["userUsed"]["minPrice"]

            book_lists.append(book_dict)
    return book_lists


if __name__ == "__main__":
    book_lists = used_book_info(TTBKey)
