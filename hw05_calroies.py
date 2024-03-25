eat_fruit = ["딸기","사과"]
eat_gram = [50,150]


cal = {"한라봉":0.5, "딸기":0.34,"바나나":0.77, "사과":0.57}

total_cal = 0
idx = 0
for eat_fruit in eat_fruits:
    for item in cal:
     if eat_fruit == fruit:  
        total_cal = cal[fruit] * eat_gram[idx]
    idx +=1
totla_cal = 0
for eat_fruit, 
print(f"총 칼로리는 {total_cal}입니다.")
