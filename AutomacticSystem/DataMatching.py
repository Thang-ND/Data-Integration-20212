import pandas as pd
import strsimpy
from zmq import TYPE


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


def newDataRecord(TYPE_PRODUCT, ALL_PRODUCT, record):
    id = len(ALL_PRODUCT.index)
    ALL_PRODUCT.loc[id] = record
    for i in range(len(TYPE_PRODUCT)):
        name = levenshtein_score(TYPE_PRODUCT.loc[i]['name'], record['name'])
        cpu = difference_score(TYPE_PRODUCT.loc[i]['cpu'], record['cpu'])
        ram = difference_score(TYPE_PRODUCT.loc[i]['ram'], record['ram'])
        rom = difference_score(TYPE_PRODUCT.loc[i]['rom'], record['rom'])
        color = difference_score(TYPE_PRODUCT.loc[i]['color'], record['color'])
        score = 0.5 * name + 0.05 * cpu + 0.2 * ram + 0.2 * rom + 0.05 * color
        if (score > 0.95):
            TYPE_PRODUCT.loc[i]['list_id'].append(id)
            return ALL_PRODUCT, TYPE_PRODUCT

    record['list_id'] = [id]
    TYPE_PRODUCT.loc[len(TYPE_PRODUCT.index)] = record
    return ALL_PRODUCT, TYPE_PRODUCT


if __name__ == '__main__':
    TYPE_PRODUCT = pd.read_json(
        'D:\\THDL\\Data-Integration-20212\\DataMatching\\products_Result.json')
    ALL_PRODUCT = pd.read_json(
        'D:\THDL\Data-Integration-20212\DataMatching\data.json')

    test_record = ALL_PRODUCT.iloc[0]

    NEW_ALL_PRODUCT , NEW_TYPE_PRODUCT = newDataRecord(TYPE_PRODUCT,ALL_PRODUCT,test_record)

    print(NEW_ALL_PRODUCT.tail(5))
    print(TYPE_PRODUCT.loc[0]['list_id'])

    

