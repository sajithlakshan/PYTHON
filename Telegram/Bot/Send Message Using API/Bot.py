import telepot


token = '5025804925:AAGkXks9rf3q-f8bV_FUwBLr1ZKB0LjGGOM' # telegram token
receiver_id = 1241796316 # https://api.telegram.org/bot<TOKEN>/getUpdates


bot = telepot.Bot(token)

bot.sendMessage(receiver_id, 'This is a automated test message.') # send a activation message to telegram receiver id

bot.sendPhoto(receiver_id, photo=open('test_img.png', 'rb')) # send message to telegram
