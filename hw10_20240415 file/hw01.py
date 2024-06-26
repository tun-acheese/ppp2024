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

def sumifs(rainfall, months, conditions):
    totla = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        month = months[i]
        if month in donditions:    
            total += Rain
    
    
    for rain, month in zip(rainfall, months):
        if month in conditions:
            total += rain
            return total

def get_data_ifs(values, conditions, creiteria):
    #dataset = []
    #for rain, year in zip(values, conditions):
    #   if year == criteria:
    #       dataest.append(rain)
    #    return dataset

    return [rain for rain, year in zip(values, conditions) if year == criteria]

def read_col(weather_filename, col_idx,year):
    dataest = []
    with open(weather_filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens=  line.split(",")
            y= int(tokens[0])
            if y == year:
                dataset.append(float(tokens[col_idx]))
        return dataest

        


def main():
    wether_filename = "lec10_20240415/weather(146)_2022-2022.csv"
    tavg = read col("lec10_20240415/weather(146)_2022-2022.csv","tavg")
    rainfall = read_col("lec10_20240415/weather(146)_2022-2022.csv","rainfall")
    month = read_col_int("lec10_20240415/weather(146)_2022-2022.csv","month")
    months = [int(2) for x in months_float]
    month = read_col_int("lec10_20240415/weather(146)_2022-2022.csv","month")
    print(months)

    #4번 최장연속 강우일수
    print(f"최장 강우일수는 {longest_rainday(rainfall)}일입니다")
    #5번 강우이벤트 중 최대 강수량
    print(f"최대 강우일수는 {max_rainfall_event(rainfall):.1f}mm입니다.")
    #6번 가장 더운날 top3
    print(f"가장 더운날 top3는 {top_rank(tmax, 3)}mm입니다.")

    # 7번, 6,7,8 강수량
    print(f"여름철 강수량은 {sumifs(rainfall, months, [6,7,,8])}mm입니다")
    #8번 2021, 2022년 강수량
    rainfall_all = read_co;l(weather_filename, "rainfall")
    year_all = read_col_int(weather_filename, "year")
    rainfall_2021 = get_year_data(rainfall_all, year_all,2021)

    rainfall_2021 = read_col_year(weather_fliename, "rainfall, 2021")
    print(f"총 강수량은 {sum(rainfall_2021):.1f}mm입니다")
if __name__ == "__main__":