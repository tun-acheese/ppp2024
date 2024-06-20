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
    elif user_text =="음..내 성격이라..양띠라 하면 부드럽고 온화한 성격 아닐까??": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="맞아! 양띠는 온순함과 자비로운 태도로 주변에 긍정적인 에너지를 뿜어내지. 친절하고 여성적인 기질이 풍부하여, 대화를 통한 직업에서 특히 빛을 발하는 특징이 있어. 강인한 모성애는 양띠의 상징적인 특성으로, 따뜻함과 보호 본능을 나타내.부드럽고 온화한 성격을 지닌 양띠는 자신의 영역이 침범당할 경우 강한 저항을 보일 수 있지만, 이는 독립적인 면모를 드러내며, 자신의 공간과 가치를 지키려는 의지를 나타내기도 한다고 해.") # 답장 보내기 
    elif user_text =="오호!!좋은 점이 많은 것 같군..그럼 쥐띠와의 궁합을 알려줘": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="흉이야. 2008년생과 1996년생은 만나지 않는게 좋을 것 같아 ") # 답장 보내기 
    elif user_text =="이유가 뭔데??": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="양띠와 쥐띠는 서로 공통점이라고는 찾아볼 수 없는 상극이야. 함께할 경우 어색함이 느껴지고, 오해가 쌓이면 결국 싸움으로 번지게 되므로, 만남을 갖더라도 오래 관계를 유지하는 것이 어려울 거야.") # 답장 보내기
    elif user_text =="그럼 소띠는?": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="절대 안돼!! 대흉이야") # 답장 보내기 
    elif user_text =="헉..그건 또 왜 그러는데...": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="소띠는 일적으로 만나게 되면, 느긋한 양띠는 쉬지 않고 일하는 소띠방식에 스트레스를 받게 되는데, 소띠는 자신의 감정을 솔직하게 말하지만, 소심한 양띠는 상처를 받고,서로가 서로를 피해다니는 관계이니 둘 관계는 멀어지게 될 거야") # 답장 보내기 
    elif user_text =="흠..그럼 호랑이 띠는?": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="오 그건 나쁘지 않은데?! 원만해~그래도 대화하는 것을 좋아하는 양띠는 표현을 잘하지 않는 호랑이띠에게 마음의 상처를 입거나, 오해를 하게 될 수도 있으니 주의하는 것이 좋아") # 답장 보내기 
    elif user_text =="알았어~참고할게! 그럼 마지막 토끼띠는 어때??": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="오 길인데? 토끼띠와 양띠는 굉장히 비슷한 면이 많아. 두 띠 모두 성격이 온화하며, 싸우는 것을 싫어하고, 평화주의적 성향을 가지고 있지. 그래서 둘이 만나면 금세 친하게 되고, 두띠는 결혼을 해도 좋으며, 오랫동안 친구처럼 지낼 수 있는 궁합이라고 해") # 답장 보내기 
    elif user_text =="아하!그럼 난 연상이 좋으니까 99년생을 찾으러 가볼게! 띠 궁합 봇 고마워~~": # 사용자가 보낸 메세지가 "뭐해"면?
        bot .send_message (chat_id =id , text ="궁금한 게 있으면 언제든지 물어봐~ 꼭 좋은 인연이 닿길 기도할게") # 답장 보내기 

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)