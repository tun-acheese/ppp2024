def total_calorie(fruits_wed, fruits):
    return 0.0

def main():
    fruit_calorie_dic=("한라봉": 50, "딸기": 34, "바나나":77)
    fruits_mon={"딸기": 300, "한라봉": 150}
    print(total_calorie(fruits_mon, fruits_calorie_dic))

    fruits_wed={"딸기": 200, "바나나": 300}
    print(total_calorie(fruits_wed, fruits_calorie_dic))

if __name__ == "__main__":
    main()
