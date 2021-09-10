import requests
from bs4 import BeautifulSoup
import re
import csv
import time

# csvヘッダー
HEADER = [
    "num",
    "name",
    "area",
    "genre",
    "address",
    "tel",
    "business_hours",
    "holiday",
    "coordinates",
]
num = 1

# csvに保存
with open("agochi.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for i in range(10):
        url = "https://agochi.jp/introduce/a" + str(num) + "/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # 店舗情報を取得
        name = soup.h2.string
        area = soup.select("a.cat-area")[0]["href"]
        genre = soup.select("a.cat-genre")[0]["href"]

        soup_table = soup.table
        address = soup_table.select_one("tr:nth-child(1) > td > p ").text
        tel = soup_table.select_one("tr:nth-child(2) > td > p").text
        business_hours = soup_table.select_one("tr:nth-child(3) > td > p").text
        holiday = soup_table.select_one("tr:nth-child(4) > td > p").text

        # 埋め込みGoogleマップから緯度経度を取得
        ifarme_src = soup.find("iframe").get("src")
        iframe_page = requests.get(ifarme_src).text
        coordinates = re.search(
            r"\d{2}\.\d{4,20}\,\d{3}\.\d{4,20}", iframe_page
        ).group()

        row = [
            num,
            name,
            area,
            genre,
            address,
            tel,
            business_hours,
            holiday,
            coordinates,
        ]
        writer.writerow(row)
        num += 1
        time.sleep(0.5)
