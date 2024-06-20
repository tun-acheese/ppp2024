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
    elif user_text == "음..내 성격이라..양띠라 하면 부드럽고 온화한 성격 아닐까??": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="맞아! 양띠는 대체로 온순함과 자비로운 태도로 주변에 긍정적인 에너지를 뿜어내지. 친절하고 여성적인 기질이 풍부하여, 대화를 통한 직업에서 특히 빛을 발하는 특징이 있어. 강인한 모성애는 양띠의 상징적인 특성으로, 따뜻함과 보호 본능을 나타내.

부드럽고 온화한 성격을 지닌 양띠는 자신의 영역이 침범당할 경우 강한 저항을 보일 수 있지만, 이는 독립적인 면모를 드러내며, 자신의 공간과 가치를 지키려는 의지를 나타내기도 한다고 해.") # 답장 보내기 
    elif user_text == "": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="음..내 성격이라..양띠라 하면 부드럽고 온화한 성격 아닐까??") # 답장 보내기 

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
