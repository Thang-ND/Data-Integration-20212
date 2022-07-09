from SchemaMatchingSystem import SchemaMatchingSystem
import pandas as pd 


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
    data[matched_col] = df_tmp[matched_col]
    return data

if __name__ == '__main__':
    path = "../PreprocessingData/Dataprocess/iphone/xtmobile.json"
    schemaMatchingSystem = SchemaMatchingSystem()
    df = pd.read_json(path)
    df2 = df.drop(["Kiểu màn hình"], axis=1)
    result = matching(df2, schemaMatchingSystem)
    result.to_json('./test_schema_matching.json')
    