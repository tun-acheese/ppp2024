def read_col(filename, col_idx):
    dataest = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")
        print(header)
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens=  line.split(",")
            dataset.append(float(tokens[col_idx]))
        return dataest

def count_rainday(rainfall)
    #rain_day = 0
    #for rain in rainfall:
    #     if rain >= 5:
    #           rain_day += 1
    #return rain_day
    return sum([1 if x >= 5 else 0 for x in rainfall])

                
def main():
    wether_filename = "lec10_20240415/weather(146)_2022-2022.csv"
    tavg = read col("lec10_20240415/weather(146)_2022-2022.csv","tavg")
    rainfall = read_col("lec10_20240415/weather(146)_2022-2022.csv","rainfall")


def count_rainday(rainfall):
    rain_day = 0
    for rain in rainfall:
        if rain >=5:
        
    print(tavg)
    # 1번 연평균기온
    print(f"연 평균 기온은 {sum(tavg)/len(tavg)}c 입니다.")
    # 2번 5mm 이상 강우일수
    print(f"5mm이상 강우일수는 [count_rainday(rainfall)}일입니다.")
    # 3번 총 강우량

if __name__ == "__main__":