import telegram
 
token = "7402143139:AAGI7MfbPaAecxEdxEJgD7i--7Vx_o98sc8"
id = "1718895002"
 
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="테스트 중입니다.")

# updates = bot.getUpdates()
# for u in updates:
#     print(u.message)