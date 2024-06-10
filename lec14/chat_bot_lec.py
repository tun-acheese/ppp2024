import telegram
 
token = '7402143139:AAGI7MfbPaAecxEdxEJgD7i--7Vx_o98sc8'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)
