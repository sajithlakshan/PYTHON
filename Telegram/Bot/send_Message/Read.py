'''

#import telegram_send
#telegram_send.send(messages=["Wow that was easy!"])

'''
import telegram
bot = telegram.Bot(token='5025804925:AAGkXks9rf3q-f8bV_FUwBLr1ZKB0LjGGOM')
print(bot.get_me())
'''
#updates = bot.get_updates()
#print(updates[0])

import requests
ALL= requests.get("https://api.telegram.org/bot5025804925:AAGkXks9rf3q-f8bV_FUwBLr1ZKB0LjGGOM/getupdates")
print(ALL.text)

print("---------------------------------------------------------------------------")
ALL= requests.get("https://api.telegram.org/bot5025804925:AAGkXks9rf3q-f8bV_FUwBLr1ZKB0LjGGOM/getupdates?offset=884124153")
print(ALL.text)
