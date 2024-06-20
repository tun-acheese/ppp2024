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
    if user_text == "나에게 잘 어울리는 사람 좀 추천해줘": 
        bot.send_message(chat_id=id, text="띠 궁합 알려줄까") 
    elif user_text == "뭐해": 
        bot.send_message(chat_id=id, text="그냥 있어") # 답장 보내기 
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
