import random
num_random = random.randint(1,99)
coin = 10
# 반복문 만들기(10번 동안 문제를 냄)
while coin:
    coin-=1
    print("남은 코인 개수:{}".format(coin))
coin = 10
num = 0
#조건문 만들기
while coin:
    coin -= 1
    num = int(input("1~99 사이의 숫자를 맞춰보세요"))
    if num == num_random:
        print("축하합니다. {}이 정답입니다".format(num))
        break
    elif num > num_random:
        print("{}보다 작습니다. 남은 코인: {}개".format(num,coin))
    elif num < num_random:
        print("{}보다 큽니다. 남은 코인: {}개".format(num,coin))

if num != num_random and coin==0:
    print ("코인이 다 떨어졌습다. 숫자 맞추기 실패입니다.")

    
#
def input_check(casting = int) -> int:
    while 1:
        try:
            var = input("정답은?")
            if var == "exit":
                return "exit"
                break
            else:
                var = casting(var)
                return var
                break
        except:
            print("잘못된 입력입니다. 정수를 입력해주세요.")
            continue
#
while coin:
    num = input_check()
    coin -= 1
    if num == "exit":
        print("게임을 포기하시다니 아쉽습니다.")
        break
    elif num == num_random:
        print("축하합니다. {}이 정답입니다".format(num))
        break
    elif num > num_random:
        print("{}보다 작습니다. 남은 코인: {}개".format(num,coin))
    elif num < num_random:
        print("{}보다 큽니다. 남은 코인: {}개".format(num,coin))

    if num != num_random and coin==0:
        print("코인이 다 떨어졌습니다. 숫자 맞추기 실패입니다.")


             
                  