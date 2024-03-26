def main():
    num_string = input("구구단 몇 단을 출력할까요?")
    number = int(num_string)
    gugudan_dan = str.format("구구단 {}단을 출력합니다.",number)
    print(gugudan_dan)
    for i in range(1,10):
        result = number * 1
        result_string = str. format("{} * {} = {}", number, i , result)
        print(result_string)

if_name_=="_main_":
    main()
