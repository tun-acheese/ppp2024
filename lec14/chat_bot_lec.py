import telegram
 
token = '아까_발급_받은_API_토큰을_넣어주세요'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)

    #7402143139:AAGI7MfbPaAecxEdxEJgD7i--7Vx_o98sc8de