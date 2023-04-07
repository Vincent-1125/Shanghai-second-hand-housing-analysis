import pandas as pd


def read(district):
    file = pd.read_csv(f'D:/DSFiles/bk/data/{district}.csv',
                       names=['place', 'title', 'msg', 'price', 'per_meter'])  # encoding="utf-8", encoding="GBK",
    lines = file.shape[0]
    file.sort_values(by='place', inplace=True)

    a = [];
    b = [];
    c = []
    for it in file['msg']:
        year = it.split('|')[1]
        if "年" not in year:
            a.append('')
            c.append('')
        else:
            a.append(year[0:-3])
            c.append(2022 - int(year[0:-3]))

        area = it.split('|')[-2]
        b.append(area[0:-3])

    file['year'] = a
    file['area'] = b
    file['age'] = c

    file.to_csv(f'D:/DSFiles/bk/data/{district}.csv', index=None, header=None)


if __name__ == '__main__':
    read('jiading')
    read('jingan')
    read('jinshan')
    read('minhang')
    read('pudong')
    read('putuo')
    read('qingpu')
    read('songjiang')
    read('yangpu')

# print(data)
# print(l)
#print(file.head(20))
