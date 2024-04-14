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
            results.append(tavg)
    return results

    
