from telegram.ext import Updater , MessageHandler , Filters

def demo1(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the lights on')
  
  
def demo2(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the lights off')
  
  
def demo3(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the fan on')
  
  
def demo4(bot,update):
  
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning the fan off')
  
  

def main(bot,update):
  a = bot.message.text
  if a=='Turn on light':
   demo1(bot,update)
   b=1
  elif a =='Turn off light':
    demo2(bot,update)
    b=0
  elif a =='Turn on fan':
    demo3(bot,update)
    b=1
  elif a =='Turn off fan':
    demo4(bot,update)
    b=0

bot_token = '1977456057:AAGCRikNBGbx3Hx_Ev8ve8XFJVUaUnnmXis'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

