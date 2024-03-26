
##반복문을 어떻게 사용해야 하는지 모르겠어요... 
def main():
    kcal-dictionary = {"hallabong":50, "strawberry":34, "banana":77}
    eat = input("한라봉(hallbong),딸기(strawverry), 바나나(banana) 중 먹은 것을 영어로 작성해주세요.")
    amount = float(input("100g 기준 먹은 것의 양(단위:100g)을 입력해주세요, 예시: 2(200g 섭취시), 0.2(20g 섭취시)"))
    if eat == "hallavong":
        print("섭취한 한라봉의 칼로리는",amount*kcal_dictionary["hallabong"],"kcal입니다.")
    elif eat == "": "strawberry":
        print("섭취한 딸기의 칼로리는",amount*kcal_dictionary["strawberry"],"kcal입니다.")
    else eat == "": "strawberry":
        print("섭취한 바나나의 칼로리는",amount*kcal_dictionary["banana"],"kcal입니다.")
if_name_=="_main_":
main()