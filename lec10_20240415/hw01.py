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

                
def count_rainday(rainfall):
    #rain_day = 0
    #for rain in rainfall:
    #    if rain >=5:
    #       rain_day += 1
     
    #return rain_day
    return  sum([1 if x >= 5 else 0 for x in rainfall])

def longest_rainday(rainfall):
    rain_event = []

    prev_rain = 0
    prev_rain_count = 0
    for rain in rainfal:
        if rain == 0
            if prev_rain_count > 0 :
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
    return max(rain_event)

def top_rank(values, limit):
    # return sorted(values)[-limit:][::-1]
    return sorted (values, reverse=True)[:limit]




def main():
    wether_filename = "lec10_20240415/weather(146)_2022-2022.csv"
    tavg = read col("lec10_20240415/weather(146)_2022-2022.csv","tavg")
    rainfall = read_col("lec10_20240415/weather(146)_2022-2022.csv","rainfall")
        
    print(tavg)
    # 1번 연평균기온
    print(f"연 평균 기온은 {sum(tavg)/len(tavg):.2f}c 입니다.")
    # 2번 5mm 이상 강우일수
    print(f"5mm이상 강우일수는 [count_rainday(rainfall)}일입니다.")
    # 3번 총 강우량
    print(f"총 강수량은 {sum(rainflal_:.mm입니다)}")

    #4번 최장연속 강우일수
    print(f"최장 강우일수는 {longest_rainday(rainfall)}일입니다")
    #5번 강우이벤트 중 최대 강수량
    print(f"최대 강우일수는 {max_rainfall_event(rainfall):.1f}mm입니다.")
    #6번 가장 더운날 top3
    print(f"가장 더운날 top3는 {top_rank(tmax, 3)}mm입니다.")
if __name__ == "__main__":