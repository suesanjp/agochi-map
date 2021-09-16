import requests
from bs4 import BeautifulSoup
import re
import time
import json

num = 1
list = []
dict = {}

for i in range(2):
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

    # Todo １つのリストの中にそれぞれ辞書が入るようにする
    dict["name"] = name
    dict["area"] = area
    dict["genre"] = genre
    dict["address"] = address
    dict["tel"] = tel
    dict["business_hours"] = business_hours
    dict["holiday"] = holiday
    dict["coordinates"] = coordinates
    list.append(dict)

    # リストをJSONファイルへ出力
    with open("mydata.json", mode="wt", encoding="utf-8") as file:
        json.dump(list, file, ensure_ascii=False, indent=2)

    num += 1
    time.sleep(0.5)
