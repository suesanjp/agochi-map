import requests
from bs4 import BeautifulSoup
import re
import time
import json

num = 1
shop_list = []

for i in range(3):
    url = "https://agochi.jp/introduce/a" + str(num) + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # 店舗情報を取得
    name = soup.h2.string

    area = soup.select("a.cat-area")[0]["title"]
    genre = soup.select("a.cat-genre")[0]["title"]

    soup_table = soup.table
    address = soup_table.select_one("tr:nth-child(1) > td > p ").text
    tel = soup_table.select_one("tr:nth-child(2) > td > p").text
    business_hours = soup_table.select_one("tr:nth-child(3) > td > p").text
    holiday = soup_table.select_one("tr:nth-child(4) > td > p").text

    # 埋め込みGoogleマップから緯度経度を取得
    ifarme_src = soup.find("iframe").get("src")
    iframe_page = requests.get(ifarme_src).text
    coordinates = re.search(r"\d{2}\.\d{4,20}\,\d{3}\.\d{4,20}", iframe_page).group()

    # 辞書に追加
    shop_data = {}
    shop_data["name"] = name
    shop_data["area"] = area
    shop_data["genre"] = genre
    shop_data["address"] = address
    shop_data["tel"] = tel
    shop_data["business_hours"] = business_hours
    shop_data["holiday"] = holiday
    shop_data["coordinates"] = coordinates
    shop_list.append(shop_data)

    num += 1
    time.sleep(0.5)

# リストをJSONファイルへ出力
with open("mydata.json", mode="wt", encoding="utf-8") as file:
    json.dump(shop_list, file, ensure_ascii=False, indent=2)
