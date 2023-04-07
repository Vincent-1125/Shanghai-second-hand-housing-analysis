import pandas as pd


def points(district):
    file = pd.read_excel(f'D:/bk/data/points/{district}.xlsx',
                         names=['place', 'lat', 'lng', 'per_meter'])  # encoding="GBK", encoding="utf-8",
    points = []
    lines = file.shape[0]
    for i in range(1, lines-2):
        d1 = dict(zip(['lat', 'lng', 'count'],
                      [file['lat'][i], file['lng'][i], file['per_meter'][i]]))
        points.append(d1)

    with open(f"D:/bk/data/points/Zpoints_{district}.txt", "w+") as f:
        for it in points:
            print(it, ',')
        f.writelines(str(points))


if __name__ == '__main__':
    points('jingan')


