import os
import pandas as pd
from strsimpy.levenshtein import Levenshtein
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from valentine import valentine_match, valentine_metrics
from valentine.algorithms import Coma, Cupid, DistributionBased, JaccardLevenMatcher, SimilarityFlooding

class SchemaMatchingSystem():
    def __init__(self):
        self.levenshtein = Levenshtein()
        self.mapping_columns =  {
            "name": ["model", "name", "Tên"],
            "url": ["url", "short-link", "link", "short_url"],
            "cpu": ["chipset", "Bộ xử lý trung tâm", "chip_set", "chip", "chip xử lý", "Chipset (hãng SX CPU)"],
            "os": ["os", "hệ điều hành"],
            "gpu": ["Chip đồ họa", "gpu", "chip_do_hoa"],
            "ram": ["ram", "RAM", "Ram"],
            "rom": ["Bộ nhớ trong", "rom"],
            "price": ["giá", "price"],
            "connect": ["kết nối", "connect"],
            "screentype": ["công nghệ màn hình", "loại màn hình", "display_type", "chất lượng màn hình", "kiểu màn hình"],
            "color": ["color", "color-split", "màu"],
            "front_camera": ["camera phụ", "camera_truoc"],
            "rear_camera": ["camera chính", "camera_sau"],
            "battery_capacity": ["dung lượng pin", "pin"],
            "bluetooth": ["bluetooth"],
            "wifi": ["wifi", "Wifi"],
            "size": ["màn hình rộng", "kích thước màn hình", "size"],
            "resolution": ["resolution", "độ phân giải", "độ phân giải màn hình"],
            "weight": ["trọng lượng", "product_weight", "cân nặng", "Kích thước khối lượng"],
            "jack_audio": ["jack tai nghe"],
            "mobile_network": ["mạng di động", "hỗ trợ 5G"],
            "sim": ["sim"],
            "security": ["bảo mật nâng cao", "security"],
            "material": ["material", "chất liệu"]
        }

    def getTargetSchema(self):
        target_schema = []
        for col in self.mapping_columns:
            target_schema.append(col)
        return target_schema
    

    def similarity_score(self, x, y):
        x = x.lower().strip()
        y = y.lower().strip()
        return (len(x) + len(y) - self.levenshtein.distance(x, y)) / (len(x) + len(y))

    def check_similarity(self, x, y, threshold=0.8):

        score = self.similarity_score(x, y)
        if score > threshold:
            return True
        return False 

    def schema_matching(self, cols, threshold=0.85):

        res = dict()
        for colum in cols:
            for key in self.mapping_columns:
                listMatching = self.mapping_columns[key]
                for match in listMatching:
                    score = self.similarity_score(colum, match)
                    if(score > threshold):
                        print("{0:20}\t{0:20}\t".format(colum, match) + str(score))
                        res[colum] = key
        return res

    def matchedCol(result): 
        matched_col = []
        source_col = []
        for key in result:
            matched_col.append(result[key])
            source_col.append(key)
        
        return (matched_col, source_col)