# 평균 기온 (일평균 기온의 연평균)
# 5mm이상 강우 일수
# 총 강우량

def read_average_temperature(filename):  #연평균 강수량
    result=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tavg=float(tokens[4])
            result.append(tavg)
    return result

def read_rain_day(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            rainfall=float(tokens[-3])
            rainfall >5 == results.append(rainfall)

    return results

def read_total_rain(filename):
    result=[]
    with open(filename) as f:
        for line in lines[1:]:
            tokens=line.split(",")
            rainfalls=float(tokens[-3])
            result.append(rainfalls)
        return results


        return results

def main():
    
    tavg = read_average_temperature('hw10_20240408 file/weather(146)_2022-2022.csv')
    print(f'평균 기온(일평균 기온의 연평균)은 {sum(tavg)/len(tavg):1f}')
    rainfall=read_rain_day('hw10_20240408 file/weather(146)_2022-2022.csv')
    print(f'5mm이상인 강우량의 일수 {len(rainfall)}일 입니다')
    rainfalls=read_total_rain('hw10_20240408 file/weather(146)_2022-2022.csv')
    print(f'총 강우량은 {sum(rainfalls)}mm입니다')


if __name__ == "__main__":
    main()