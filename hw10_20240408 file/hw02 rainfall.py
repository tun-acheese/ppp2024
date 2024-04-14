# 평균 기온 (일평균 기온의 연평균)
# 5mm이상 강우 일수
# 총 강우량
_

def read_average_temperature(filename):
    result=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tavg=float(tokens[4])
            result.append(tavg)
    return result

    
def main():
    
    tavg = read_average_temperature('weather(146)_2022_2022.csv')
    print(f'평균 기온(일평균 기온의 연평균)은 {sum(tavg)}')
     tavg = read_5mm ('weather(146)_2022_2022.csv')
    if 5 above average 
    print(f'5mm이상 강우량은 {sum(tavg)}')
     tavg = read_total_rainfall('weather(146)_2022_2022.csv')
    print(f'총 강우량은 {sum(tavg)}')


if __name__ == "__main__":
    main():