import requests
from bs4 import BeautifulSoup
import re
import csv
import time

# csvヘッダー
HEADER = ["num", "name", "address", "area", "genre", "coordinates"]
num = 1

# csvに保存
with open("agochi.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for i in range(1):
        url = "https://agochi.jp/introduce/a" + str(num) + "/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # 店舗情報を取得
        name = soup.h2.string
        soup_table = soup.table
        address = soup.table.select("p:nth-child(1)")
        area = soup.select("a.cat-area")[0]["href"]
        genre = soup.select("a.cat-genre")[0]["href"]

        # 埋め込みGoogleマップから緯度経度を取得
        ifarme_src = soup.find("iframe").get("src")
        iframe_page = requests.get(ifarme_src).text
        coordinates = re.search(
            r"\d{2}\.\d{4,20}\,\d{3}\.\d{4,20}", iframe_page
        ).group()

        row = [num, name, address, area, genre, coordinates]
        writer.writerow(row)
        num += 1
