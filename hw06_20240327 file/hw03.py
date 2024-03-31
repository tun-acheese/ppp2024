while True:
    try:
        input_year = int(input("윤년인지 확인하고 싶은 연도를 숫자로 입력하세요 :"))
        break
    except:
        print("\n")
        print("다시 입력해주세요.:")
        continue

if input_year % 4 == 0:
    if input_year % 100 == 0 and input_year % 400 ==0:
        print("윤년입니다!")
    elif input_year % 100 == 0 and input_year % 400 != 0:
        print("윤년이 아닙니다.")
    else:
        print("윤년입니다!")
else:
    print("윤년이 아닙니다")
