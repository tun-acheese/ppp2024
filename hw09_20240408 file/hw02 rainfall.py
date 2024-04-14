import csv
f = open('rainfall.csv'.'r'.encoding='cp949')
data=csv.reader(f.delimiter-',')
print(data)

data = csv.reader(f)
next(data)
low = []

for row in data :
    if row[-2] !=




평균 기온 (일평균 기온의 연평균)
5mm이상 강우 일수
총 강우량

if__name__=="__main__": 
main()