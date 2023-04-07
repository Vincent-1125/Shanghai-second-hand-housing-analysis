from matplotlib import pyplot as plt
import numpy as np

'''
with open('ip2.txt', 'r') as f:
    proxy_ip = []
    for ip in f.readlines():
        ip = ip.strip('\n')  # 去掉列表中每一个元素的换行符
        proxy_ip.append('http://' + ip)
    print(proxy_ip)

proxies = {'http': proxy_ip}
print(proxies)
'''
x = np.arange(1,10)
fig = plt.figure(figsize=(8, 5))
plt.scatter(x, x, s=16)
plt.show()