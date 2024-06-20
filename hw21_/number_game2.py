import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
 
token = "7402143139:AAGI7MfbPaAecxEdxEJgD7i--7Vx_o98sc8"
id = "7028566921"
 
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="테스트 중입니다.")
 
# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
 



def handler(update, context):
    user_text = update.message.text 

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

    #if user_text == "나에게 잘 어울리는 사람 추천해줘": # 사용자가 보낸 메세지가 "안녕"이면?
    #    bot.send_message(chat_id=id, text="띠 궁합 한 번 봐줄까") # 답장 보내기


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)