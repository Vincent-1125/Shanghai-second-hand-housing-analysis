from pyquery import PyQuery as pq
import json
import requests
import pandas as pd
import time
import random

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


def get_a_page(i, district):
    url = f'https://sh.ke.com/ershoufang/{district}/pg{i}sf1/'
    result = requests.get(url)
    print(result.status_code)


def get_a_page1(i, district):
    headers = {
        'user-agent': random.choice(USER_AGENTS)}
    url = f'https://sh.ke.com/ershoufang/{district}/pg{i}sf1/'
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        pass
    else:
        print('stop', sep='')
        return

    doc = pq(result.text)
    ul = doc('.sellListContent')
    divs = ul.children('.clear .info.clear').items()  #
    count = 0

    title = [];    place = [];    msg = [];    price = [];    per_meter = []
    for div in divs:
        title.append(div.children('.title a').text())
        place.append(div.children('.address .flood .positionInfo a').text())
        msg.append(div.children('.address .houseInfo').text())
        price.append(div.children('.address .priceInfo .totalPrice span').text())
        per_meter.append(div.children('.address .priceInfo .unitPrice').text().rstrip("元/平"))
        count += 1

    table = {
        'place': place,
        'title': title,
        'msg': msg,
        'price': price,
        'per_meter': per_meter
    }

    df = pd.DataFrame(table)
    df.to_csv(f'D:/DSFiles/bk/data/{district}.csv', mode='a',
              header=None, index=False, encoding='utf-8')  #


if __name__ == '__main__':

    for num in range(1, 41):
        get_a_page1(num, 'chongming')
        print('page:', num)
        time.sleep(0.7)
