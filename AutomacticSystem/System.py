import pandas as pd
import json
import re
from SchemaMatchingSystem import SchemaMatchingSystem
import strsimpy
from zmq import TYPE
from kafka import KafkaConsumer
import requests
from elasticsearch import Elasticsearch
import hashlib
# import schedule
# import time


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).digest()
    return "".join(["{:x}".format(b) for b in sha_signature])

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
    color1 = ['??en', 'Tr???ng', 'T??m', '?????', 'Xanh L??', 'Xanh', 'V??ng', 'Xanh D????ng', 'Than ch??',
              'H???ng', 'B???c', 'Xanh r??u', 'JetBlack', 'X??m', 'Xanh d????ng', 'Cam', 'Da Xanh',
              'Xanh Bi???n', 'V??ng h???ng']
    color2 = ['Black', 'White', 'Purple', 'Red', 'Blue', 'Green', 'Yellow', 'Blue', 'Graphite',
              'Pink', 'Silver', 'Moss Green', 'JetBlack', 'Gray', 'Blue', 'Orange', 'Blue Skin',
              'Sea Blue', 'Rose Gold']
    for j in range(len(model)):
        if data['name'].upper().find(model[j]) != -1:
            data['name'] = model[j]
            break

    for j in range(len(CPU)):
        if data['cpu'].find(CPU[j]) != -1:
            data['cpu'] = CPU[j]

    for j in range(len(color2)):
        if data['color'] == color1[j]:
            data['color'] = color2[j]
            break

    data['ram'] = re.sub(r'\D', '', data['ram'])

    data['price'] = re.sub(r'\D', '', data['price'])

    data['rom'] = data['rom'].replace(" ", "")

    if data['ram'] == '':
        data['ram'] = "unknown"

    if data['rom'] == '':
        data['rom'] = "unknown"

    if data['cpu'] == '':
        data['cpu'] = "unknown"

    return data


def matchedCol(result):
    matched_col = []
    source_col = []
    for key in result:
        matched_col.append(result[key])
        source_col.append(key)

    return matched_col, source_col


def matching(df, smSystem):
    columns = list(df.columns)
    res = smSystem.schema_matching(columns, threshold=0.85)
    matched_col, source_col = matchedCol(res)
    df_tmp = df[source_col].rename(columns=res)
    data = pd.DataFrame(columns=smSystem.getTargetSchema())
    # print(data.shape)
    # print(df_tmp.shape)
    data[matched_col] = df_tmp[matched_col]
    return data


LEVENSSHTEIN = strsimpy.NormalizedLevenshtein()


def levenshtein_score(x, y):
    if (x == 'unknown' or y == 'unknown'):
        return 1
    return 1 - LEVENSSHTEIN.distance(x, y)


def difference_score(x, y):
    if (x == 'unknown' or y == 'unknown'):
        return 1
    return 1 if x == y else 0

# input is series type and was preprocessed


def newDataRecord(TYPE_PRODUCT, record):
    id = str(record["url"])+str(record["color"].upper())
# print(id)
    enid = encrypt_string(id)
    for i in range(len(TYPE_PRODUCT)):
        # print(len(TYPE_PRODUCT))
        # if record["url"] =="https://www.xtmobile.vn/iphone-13-128gb-cu-likenew":
            # print("day roi")
            # print(record)
        record['ram'] =  record['ram'].upper().replace("GB", "")
        record['rom'] =  record['rom'].upper().replace("GB", "")
        name = levenshtein_score(TYPE_PRODUCT[i]['name'].upper(), record['name'].upper())
        cpu = difference_score(TYPE_PRODUCT[i]['cpu'].upper(), record['cpu'].upper())
        ram = difference_score(TYPE_PRODUCT[i]['ram'].upper(), record['ram'].upper())
        rom = difference_score(TYPE_PRODUCT[i]['rom'].upper(), record['rom'].upper())
        color = difference_score(TYPE_PRODUCT[i]['color'].upper(), record['color'].upper())
        score = 0.5 * name + 0.05 * cpu + 0.2 * ram + 0.2 * rom + 0.05 * color
        # print(score)
        # print(enid)

        if (score > 0.95):
            record["product_type_id"] = TYPE_PRODUCT[i]["id"]
            insertEs(record, "apple_product", enid)
            print(TYPE_PRODUCT[i]["id"])
            print(record)
            return 1

    newType = {"id":len(TYPE_PRODUCT),"name":record["name"],"ram":record["ram"],"rom":record["rom"],"color":record["color"],"cpu":record["cpu"]}
    insertEs(newType, "apple_product_type", newType["id"])
    record["product_type_id"] = newType["id"]
    insertEs(record, "apple_product", enid)
    return 2


# def newDataRecord(TYPE_PRODUCT, record):
#     # id = len(ALL_PRODUCT.index)
#     # ALL_PRODUCT.loc[id] = record
#     for id in TYPE_PRODUCT:
#         name = levenshtein_score(TYPE_PRODUCT[id]['name'], record['name'])
#         cpu = difference_score(TYPE_PRODUCT[id]['cpu'], record['cpu'])
#         ram = difference_score(TYPE_PRODUCT[id]['ram'], record['ram'])
#         rom = difference_score(TYPE_PRODUCT[id]['rom'], record['rom'])
#         color = difference_score(TYPE_PRODUCT[id]['color'], record['color'])
#         score = 0.5 * name + 0.05 * cpu + 0.2 * ram + 0.2 * rom + 0.05 * color
#         if (score > 0.95):
#             record["product_type_id"] = TYPE_PRODUCT[id]["id"]
#             insertEs(record, "apple_product", encrypt_string(record["url"]+record["color"]))
#
#
#     record['list_id'] = [id]
#     TYPE_PRODUCT.loc[len(TYPE_PRODUCT.index)] = record


def getMessFromKafka():
    bootstrap_servers = ['localhost:9092']
    topicName = 'crawler-apple-product'
    consumer = KafkaConsumer (topicName, group_id ='thdl',bootstrap_servers = bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    data = []
    for message in consumer:
        item = message.value
        a_json = json.dumps(item)
        schemaMatchingSystem = SchemaMatchingSystem()

        headers = list(item.keys())
        values = [list(item.values())]

        df = pd.DataFrame(values, columns=headers)

        # print(df['Ki???u m??n h??nh'])
        if "Ki???u m??n h??nh" in df:
            del df['Ki???u m??n h??nh']
        result = matching(df, schemaMatchingSystem)

        schemaMatematchingItem = result.to_json()
        data = json.loads(schemaMatematchingItem)

        newResultTmp = {}
        for itm in data:
            values = json.loads(result[itm].to_json())

            for idx in values:
                if idx not in newResultTmp:
                    newResultTmp[idx] = {}
                    newResultTmp[idx][itm] = values[idx]
                else:
                    newResultTmp[idx][itm] = values[idx]

        newResult = [newResultTmp[itm] for itm in newResultTmp]
        # print(newResult)
        preItem = PreData(newResult[0])
        TYPE_PRODUCT = getProductTypeFromElasticsearch()
        newDataRecord(TYPE_PRODUCT, preItem)
    consumer.close()
    return data

def getProductTypeFromElasticsearch():
    substring = "You Know, for Search".encode()
    response = requests.get("http://127.0.0.1:9200")
    if substring in response.content:
        es = Elasticsearch("http://127.0.0.1:9200")
        # res = es.get(index="apple_product_type", id=1)
        # print(res['_source'])
        res = es.search(index="apple_product_type", query ={
            'match_all' : {}
        }, size=1000)

        TYPE_PRODUCT = []

        for doc in res['hits']['hits']:
            TYPE_PRODUCT.append(doc['_source'])
        return TYPE_PRODUCT

def updateEs(doc, index, id):
    substring = "You Know, for Search".encode()
    response = requests.get("http://127.0.0.1:9200")
    if substring in response.content:
        es = Elasticsearch("http://127.0.0.1:9200")
        es.update(index=index,id=id,body={"doc": doc})

def insertEs(doc, index, id):
    substring = "You Know, for Search".encode()
    response = requests.get("http://127.0.0.1:9200")
    if substring in response.content:
        es = Elasticsearch("http://127.0.0.1:9200")
        es.index(index=index, id=id, document=doc)



# def pipeline():
#     data = getMessFromKafka()
#     for item in data:
#         print(item)
#         a_json = json.loads(item)
#         schemaMatchingSystem = SchemaMatchingSystem()
#         df = pd.DataFrame.from_dict(a_json, orient="index")
#         df2 = df.drop(["Ki???u m??n h??nh"], axis=1)
#         result = matching(df2, schemaMatchingSystem)
#         schemaMatematchingItem = result.to_json()
#         a_json = json.loads(schemaMatematchingItem)
#         a_json = json.dumps(a_json)
#         preItem = PreData(a_json)
#         TYPE_PRODUCT = getProductTypeFromElasticsearch()
#         newDataRecord(TYPE_PRODUCT, preItem)

# def demo():
#     item = '{"name": "iPhone 11 64GB Ch??nh h??ng (VN/A)", "url": "https://www.xtmobile.vn/iphone-11-64gb-vna", "C??ng ngh??? m??n h??nh": "Liquid Retina LCD", "????? ph??n gi???i": "12 MP", "M??n h??nh r???ng": "6.1", "M???t k??nh c???m ???ng": "K??nh oleophobic coating (ion c?????ng l???c)", "Quay phim": "Quay phim 4K 2160p@60fps", "????n Flash": "4 ????n LED (2 t??ng m??u)", "Ch???p ???nh n??ng cao": "Ch???p ???nh x??a ph??ng, L???y n??t d??? ??o??n, T??? ?????ng l???y n??t, Ch???m l???y n??t, Nh???n di???n khu??n m???t, HDR, Panorama, Ch???ng rung quang ho??c (OIS), Night Mode, Zoom quang 2x, Ch???p ???nh trong khi quay video", "Videocall": "C??", "T??nh n??ng kh??c": "Selfie ng?????c s??ng HDR, Camera g??c r???ng, Quay video 4K, Quay video slow motion, Nh???n di???n khu??n m???t, Ch???p ???nh li??n t???c", "H??? ??i???u h??nh": "iOS", "Chipset (h??ng SX CPU)": "Apple A13 Bionic 6 nh??n", "cpu": "", "Chip ????? h???a (GPU)": "Apple GPU 4 nh??n", "ram": "4 GB", "rom": "64 GB", "Th??? nh??? ngo??i": "Kh??ng", "M???ng di ?????ng": "3G, 4G LTE Cat 16", "SIM": "1 Nano SIM", "Wifi": "Wi-Fi 802.11 a/b/g/n/ac/ax, dual-band, hotspot", "GPS": "A-GPS, GLONASS, GALILEO, QZSS", "Bluetooth": "5.0, A2DP, LE", "C????ng k????t n????i/sa??c": "Lightning", "Jack tai nghe": "Kh??ng", "K???t n???i kh??c": "NFC, OTG", "Thi???t k???": "Nguy??n kh???i", "Ch???t li???u": "Khung nh??m 7000 series + m???t k??nh c?????ng l???c", "K??ch th?????c": "D??i 150.9 mm - Ngang 75.7 mm - D??y 8.3 mm", "Tr???ng l?????ng": "194 g", "Dung l?????ng pin": "3110 mAh", "Lo???i pin": "Pin chu???n Li-Ion", "C??ng ngh??? pin": "", "B???o m???t n??ng cao": "Nh???n di???n khu??n m???t Face ID", "T??nh n??ng ?????c bi???t": "Haptic Touch, Siri, Animoji, Memoji, Ch???ng n?????c IP68, S???c nhanh, S???c kh??ng d??y", "Ghi ??m": "C??, microphone chuy??n d???ng ch???ng ???n", "Radio": "Kh??ng", "color": "Xanh L??", "price": "11.490.000??", "date": "2022-7-10"}'
#     a_json = json.loads(item)
#     schemaMatchingSystem = SchemaMatchingSystem()
#     df = pd.DataFrame.from_dict(a_json, orient="index")
#     # df2 = df.drop(["Ki???u m??n h??nh"], axis=1)
#     result = matching(df, schemaMatchingSystem)
#     schemaMatematchingItem = result.to_json()
#     a_json = json.loads(item)
#     print("Type:", type(a_json))
#     preItem = PreData(a_json)
#     TYPE_PRODUCT = getProductTypeFromElasticsearch()
#     newDataRecord(TYPE_PRODUCT, preItem)


if __name__ == '__main__':
    # schedule.every(10).minutes.do(run())
    # while True:
    # pipeline()
    getMessFromKafka()
    # print(encrypt_string("https://www.xtmobile.vn/iphone-13-pro-128gb"+"YELLOW"))
        # schedule.run_pending()


