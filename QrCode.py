import qrcode
from telegram import Update
from telegram.ext import Updater,commandhandler,callbackcontext,MessageHandler,Filters
import telegram
import os 
global TOKEN
TOKEN="5671686293:AAFKSpXZYIK3bmIBZHH0vNr1YAmvbtF_KIU"
updater=Updater(TOKEN)


"""def start(update :Update , context : callbackcontext):
    chat_id=update.effective_chat.id
    bot=telegram.Bot(token=TOKEN)
    start_text="hello welcome to QrCode_maker bot  lets start making qr codes by sending a link or a text to me ."
    bot.send_message(chat_id=chat_id,text=start_text)"""

    


    
def main(update :Update , context : callbackcontext):
    chat_id=update.effective_chat.id
    username=update.effective_chat.username
    link=update.message.text
    chanel_id="@testisgood"
    BOT=telegram.Bot(token=TOKEN)
    member=BOT.get_chat_member(chat_id=chanel_id,user_id=chat_id,)
    print(member)
    if  member.status!="member":
        joining_text="for supporting us you must join https://t.me/testisgood channel , please join this chanel and press /start"
        BOT.send_message(chat_id=chat_id,text=joining_text)
    else:
        img=qrcode.make(link)
        img.save(f"{chat_id}.jpg")
        BOT=telegram.Bot(token=TOKEN)
        BOT.send_photo(chat_id=chat_id,photo=open(f"{chat_id}.jpg",'rb'))
        os.remove(f"{chat_id}.jpg")
        logs=f"{username}    , {chat_id}     , {link}"
        BOT.send_message(chat_id="137734386",text=logs)

    
    
#updater.dispatcher.add_handler(commandhandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, main))

updater.start_polling()
updater.idle()