#!/usr/bin/python 2.7

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "http://php.net/manual/en/indexes.functions.php"
    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html)
    li_s = soup.find_all("li")
    lines = soup.find_all("a", {"class": "index"})

    with open('functions.txt', 'w') as f:
        for line in lines:
            f.write(line.text + "\n")