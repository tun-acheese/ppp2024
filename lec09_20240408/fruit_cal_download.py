

def main():
    service_id = 'I2790'

    index_ranges = []
    for i 


    'endIdx': str(end),
    formatted 
url = 'http'

    df = pd.concat(results, ignore_index=True)
    df = preproces(df)

    df.to_csv('식품칼로리.csv, encoding='utf-8)











    df = df
    df = df[['DESC_KOR', 'NUTR_CONT1', 'SERVING_SIZE']]
    df = df.rename(columns-{'DESC_KOR': '작목', 'NUTR_CONT1': '열량(kcal)(1회제공량)'})

    return df