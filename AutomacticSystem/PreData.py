import pandas as pd
import json
import re


def PreData(data):
    model = ["IPHONE 13 MINI", "IPHONE 13 PRO MAX", "IPHONE 13 PRO", "IPHONE 13", "IPHONE 12 MINI", "IPHONE 12 PRO MAX",
             "IPHONE 12 PRO", "IPHONE 12",
             "IPHONE 11 PRO MAX", "IPHONE 11 PRO",
             "IPHONE 11", "IPHONE XS MAX", "IPHONE XS", "IPHONE XR", "IPHONE X",
             "IPHONE 8 PLUS", "IPHONE 8", "IPHONE 7 PLUS", "IPHONE 7",
             "IPHONE 6S PLUS", "IPHONE 6 PLUS", "IPHONE 6S", "IPHONE 6",
             "IPHONE 5S", "IPHONE 5C", "IPHONE 5", "IPHONE 4S", "IPHONE 4",
             "IPHONE SE 2020", "IPHONE SE 2022",
             "IPHONE SE 2", "IPHONE SE 3",
             "IPHONE SE",
             "IPHONE 3GS", "IPHONE 3G", "IPHONE 2G",
             "IPAD MINI 3", "IPAD MINI 1", "IPAD GEN 5", "IPAD AIR 2", "IPAD AIR 1", "IPAD 4", "IPAD GEN 6",
             "IPAD PRO 12,9", "IPAD PRO 9.7", "IPAD PRO 10.5", "IPAD PRO 12.9", "IPAD 10.2",
             "IPAD 9 10.2", "IPAD AIR 10.9", "IPAD PRO M1 12.9", "IPAD AIR 10.9 INCH", "IPAD 10.2 INCH",
             "IPAD MINI 6", "IPAD 2010", "IPAD 2 2011", "IPAD PRO M1 11 INCH", "IPAD 10.2 INCH",
             "IPAD 6 MINI", "IPAD 3 MINI", "IPAD AIR 3", "IPAD GEN 9", "IPAD PRO M1 11", "IPAD AIR M1 10.9",
             "IPAD MINI GEN 6TH", "IPAD PRO M1 11", "IPAD AIR4 10.9",
             "IPAD 3 2012", "IPAD 4 2012", "IPAD MINI 2012", "IPAD AIR 2013",
             "IPAD MINI 2", "IPAD AIR 2 2014", "IPAD MINI 3 2014", "IPAD PRO 12,9 INCH",
             "IPAD MINI 4", "IPAD PRO 9.7 INCH", "IPAB 2017", "IPAD PRO 10.5 INCH", "IPAD PRO 12.9 INCH",
             "IPAD PRO 12.9 INCH 2017", "IPAD 2018", "IPAD PRO 11", "IPAD PRO 12.9 INCH 2018",
             "IPAD AIR 2019", "IPAD MINI 5", "IPAD 10.2 INCH 2019", "IPAD AIR 4",
             "IPAD AIR 4 2020", "IPAD PRO 11 INCH 2020", "IPAD PRO 12.9 INCH 2020", "IPAD PRO 12.9 INCH 2021",
             "IPAD 9", "IPAD 9 10.2 INCH", "IPAD 9 10.2 INCH 2021", "IPAB MINI 6 2021",
             "IPAD AIR 5 M1", "IPAD AIR 5 M1 2022", "IPAD PRO M1 12.9 INCH",
             "IPAD MINI 7.9 INCH", "IPAD PRO M1 2021 12.9 INCH", "IPAD PRO M1 2021 11 INCH", "IPAD AIR 10.5 INCH",
             "IPAD PRO M1 2021 12.9 INCH", "IPAD PRO M1 2021 12.9 INCH", "IPAD AIR 10.5 INCH",
             "APPLE GEN 1", "APPLE SERIES 1", "APPLE SERIES 2", "APPLE SERIES 3", "APPLE SERIES 4",
             "APPLE SERIES 5", "APPLE SERIES 6", "APPLE WATCH GEN 1",
             "APPLE WATCH SERIES 1", "APPLE WATCH SERIES 2", "APPLE WATCH SERIES 3", "APPLE WATCH SERIES 4",
             "APPLE WATCH SERIES 5", "APPLE WATCH SERIES 6", "APPLE WATCH S1", "APPLE WATCH S2", "APPLE WATCH S3",
             "APPLE WATCH S4", "APPLE WATCH S5", "APPLE WATCH S6", "APPLE WATCH S7", "APPLE WATCH SE", "APPLE SE",
             "MACBOOK PRO M1 PRO", "MACBOOK AIR M1", "MACBOOK PRO", "MACBOOK AIR", "MAC MINI", "MAC STUDIO"]
    CPU = ["A15", "A14", "A13", "A12", "A11", "A10", "A9", "A8", "A7", "A6"]
    color1 = ['Đen', 'Trắng', 'Tím', 'Đỏ', 'Xanh Lá', 'Xanh', 'Vàng', 'Xanh Dương', 'Than chì',
              'Hồng', 'Bạc', 'Xanh rêu', 'JetBlack', 'Xám', 'Xanh dương', 'Cam', 'Da Xanh',
              'Xanh Biển', 'Vàng hồng']
    color2 = ['Black', 'White', 'Purple', 'Red', 'Blue', 'Green', 'Yellow', 'Blue', 'Graphite',
              'Pink', 'Silver', 'Moss Green', 'JetBlack', 'Gray', 'Blue', 'Orange', 'Blue Skin',
              'Sea Blue', 'Rose Gold']
    for i in range(len(data)):
        for j in range(len(model)):
            if data[i]['name'].upper().find(model[j]) != -1:
                data[i]['name'] = model[j]
                break

        for j in range(len(CPU)):
            if data[i]['Chipset (hãng SX CPU)'].find(CPU[j]) != -1:
                data[i]['Chipset (hãng SX CPU)'] = CPU[j]

        for j in range(len(color1)):
            if data[i]['color'] == color1[j]:
                data[i]['color'] = color2[j]
                break

        data[i]['RAM'] = re.sub(r'\D', '', data[i]['ram'])

        data[i]['price'] = re.sub(r'\D', '', data[i]['price'])

        data[i]['Bộ nhớ trong'] = data[i]['rom'].replace(" ", "")

        if data[i]['RAM'] == '':
            data[i]['RAM'] = "unknown"

        if data[i]['Bộ nhớ trong'] == '':
            data[i]['Bộ nhớ trong'] = "unknown"

        if data[i]['Chipset (hãng SX CPU)'] == '':
            data[i]['Chipset (hãng SX CPU)'] = "unknown"


if __name__ == '__main__':
    with open("input.json", encoding="utf8") as jsonFile:
        data = json.load(jsonFile)

    PreData(data)

    with open("output.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # df = pd.read_json('./output.json')
    # print(df.RAM.unique())
    # print(df['Bộ nhớ trong'].unique())
    # print(df.color.unique())
    # print(df.name.unique())
    # print(df['Chipset (hãng SX CPU)'].unique())
