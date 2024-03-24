kcal_dictionary = ("hallabong":50, "strawberry":34, "banana":77)
eat = input("한라봉(hallabong), 딸기(strawberry), 바나나(banana) 중 먹은 것을 영어로 작성해주세요.")
amount =float(input("100g 기준 먹은것의 양 (단위:100g)을 입력해주세요, 예시 2(200g 섭취시), 0.2(20g 섭취시)"))
if eat == "hallabong" :
        print("섭취한 한라봉의 칼로리는", amount*kcal_dictionary["hallabong"],"kcal입니다.")
elif eat == "hallabong" :
        print("섭취한 한라봉의 칼로리는", amount*kcal_dictionary["hallabong"],"kcal입니다.")
else:
        print("섭취한 한라봉의 칼로리는", amount*kcal_dictionary["hallabong"],"kcal입니다.")
