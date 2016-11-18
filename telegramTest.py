import telebot
import xml.etree.ElementTree as et
import random
from telebot import types
import urllib

source_xml_file = "kural.xml"
user_id_txt_file = "userid.txt"
tree = et.parse(source_xml_file)
element_top = tree.getroot()



bot = telebot.TeleBot("<APITOKEN>")
bot.set_webhook()

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(m):
   cid = m.chat.id
   if(m.content.content_type='new_chat_participant'):
      if m.new_chat_

@bot.message_handler(commands=['start'])
def send_welcome(message):
   with open(user_id_txt_file, 'a') as f:
                print(str(message.from_user.id), file=f)
   print(str(message.from_user.id))
   bot.send_message(message.chat.id,"அகர முதல எழுத்தெல்லாம் ஆதி \n பகவன் முதற்றே உலகு.")
   
   
@bot.message_handler(commands=['random'])
def random_quote(message):
   print(str(message.from_user.username)+"###")
   temp_number = random.randint(1,1330)
   the_message = "குறள் எண்: " +str(temp_number)+ "\n\n"+element_top[temp_number][1].text+"\n"+element_top[temp_number][2].text+ "\n\n" +element_top[temp_number][3].text+"\n\n"+"- திருவள்ளுவர்" 
   bot.send_message(message.chat.id,the_message)



try: 
    bot.polling(none_stop=True)
except urllib.error.HTTPError:
    time.sleep(10)


while True:
    time.sleep(20)
