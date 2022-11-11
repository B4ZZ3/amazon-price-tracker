"""A prize tracker to check the prize of amazon products"""

import requests
import re

from lxml import etree as et
from bs4 import BeautifulSoup

urls = ["https://www.amazon.de/Logitech-Z906-3D-Stereo-Lautsprecher-5-1-Dolby-Surround-Sound-Fernseher-Wohnzimmereinrichtungen-Schwarz/dp/B004PGM9KY/",
        "https://www.amazon.de/Logitech-Wireless-Presenter-Cordless-Timer/dp/B002L3TSLQ/",
        "https://www.amazon.de/Rode-Studioqualit%C3%A4t-USB-Kondensatormikrofon-Tischstativ-Popschutz/dp/B00KQPGRRE/",
        "https://www.amazon.de/Elgato-Wave-Mic-Arm-Kabelkan%C3%A4len/dp/B09737ZXMK"]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}

for url in urls:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    productTitle = soup.find_all(id="productTitle")[0].text
    productTitle = re.split(', | -', productTitle)
    productTitle = productTitle[0]
    
    price = soup.find_all(class_="a-offscreen")[0].text
    print(productTitle,": ", price)
