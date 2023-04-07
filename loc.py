import json
from math import radians, cos, sin, asin, sqrt
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

proxy_list = ['http://112.85.2.204:35104', 'http://112.66.252.203:40022', 'http://1.80.227.4:41696', 'http://175.170.40.229:40049', 'http://175.175.85.96:40012', 'http://223.243.79.46:40007', 'http://49.82.55.234:48418', 'http://223.242.115.236:65531', 'http://183.152.216.114:40013', 'http://60.184.24.105:40005', 'http://122.232.156.252:40015', 'http://112.195.120.135:40012', 'http://1.84.253.232:40015', 'http://219.135.78.45:29000', 'http://36.6.142.198:26905', 'http://115.220.190.254:51826', 'http://114.238.113.199:52758', 'http://113.137.110.33:40006', 'http://123.144.145.29:40003', 'http://140.224.153.146:38439']


# 根据地址返回经纬度
def getposition(ak, dw):
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    headers = {
        'user-agent': random.choice(USER_AGENTS)}
    url = 'http://api.map.baidu.com/geocoding/v3/?address={Address}&output=json&ak={Ak}'.format(Address=dw, Ak=ak)
    res = requests.get(url, headers=headers)  #  , proxies=proxies
    json_data = json.loads(res.text)
    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat']  # 纬度
        lng = json_data['result']['location']['lng']  # 经度
    else:
        print("Error output!")
        print(json_data)
        return json_data['status']
    return lat, lng


def addposition(district):
    ak = 'gh9u1qMjV72Wgif2b5mSWxabPMW1IhW7'

    file = pd.read_csv(f'D:/bk/data/{district}.csv', encoding="GBK",
                       names=['place', 'title', 'msg', 'price', 'per_meter', 'year', 'area', 'age'])  #
    #  file.sort_values(by='place', inplace=True)
    lines = file.shape[0]
    place = file['place'].tolist()
    #  print(place)

    lat = [];
    lng = []
    for i in range(0, lines):
        if i % 50 == 0 and i > 1:
            print('rest---------------------')
            time.sleep(5)
        print(place[i], i)
        if i > 0 and place[i] == place[i - 1]:
            lat.append(lat[-1])
            lng.append(lng[-1])
        else:
            loc = getposition(ak, "上海" + place[i])
            if loc == 1:
                lat.append(0)
                lng.append(0)
                pass
            else:
                lat.append(loc[0])
                lng.append(loc[1])
                time.sleep(3*random.random())

    file['lat'] = lat
    file['lng'] = lng
    file.to_csv(f'D:/DSFiles/bk/data/{district}1.csv', index=None)


if __name__ == '__main__':
    districts = ['sample']
    for dis in districts:
        print(dis)
        addposition(dis)

