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
    if user_text == "나에게 잘 어울리는 사람 추천해줘": # 사용자가 보낸 메세지가 "안녕"이면?
        bot.send_message(chat_id=id, text="띠 궁합 한 번 봐줄까") # 답장 보내기
    elif user_text == "좋아!": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="출생년도가 뭐야?") # 답장 보내기 
    elif user_text == "2003년생!": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="양띠네!? 일단 궁합을 찾기 전에 너의 성격을 먼저 알아야! 너의 성격이 어떤 것 같아??") # 답장 보내기 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
