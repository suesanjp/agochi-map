import requests
from bs4 import BeautifulSoup
import re
import time

num = 1

for i in range(5):
    url = "https://agochi.jp/introduce/a" + str(num) + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # 店舗情報を取得
    name = soup.h2.string


    soup_table = soup.table
    address = soup_table.select_one("tr:nth-child(1) > td > p ").text
    tel = soup_table.select_one("tr:nth-child(2) > td > p").text
    business_hours = soup_table.select_one("tr:nth-child(3) > td > p").text
    holiday = soup_table.select_one("tr:nth-child(4) > td > p").text

    # 埋め込みGoogleマップから緯度経度を取得
    ifarme_src = soup.find("iframe").get("src")
    iframe_page = requests.get(ifarme_src).text
    coordinates = re.search(r"\d{2}\.\d{4,20}\,\d{3}\.\d{4,20}", iframe_page).group()


    num += 1
    time.sleep(0.5)
