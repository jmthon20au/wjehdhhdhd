# استيراد المكتبات اللازمة
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image, ImageFilter

# تعريف معلومات البوت
TOKEN = "6418845303:AAGV-jU1GiVv21Z44awdtN2f2ULwz_bkz2Q" # ضع رمز البوت الخاص بك هنا
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# تعريف دالة للترحيب بالمستخدم
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبا، أنا بوت يمكنه إضافة فلتر إلى الصور. أرسل لي صورة وسأرسلها لك بفلتر جميل.")

# تعريف دالة لمعالجة الصور
def filter_image(update, context):
    # تحميل الصورة من الرسالة
    file_id = update.message.photo[-1].file_id
    file = bot.get_file(file_id)
    file.download("image.jpg")

    # فتح الصورة وتطبيق فلتر
    image = Image.open("image.jpg")
    filtered_image = image.filter(ImageFilter.CONTOUR)

    # حفظ الصورة وإرسالها للمستخدم
    filtered_image.save("filtered_image.jpg")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("filtered_image.jpg", "rb"))

# إضافة معالجات للأوامر والرسائل
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

filter_handler = MessageHandler(Filters.photo, filter_image)
dispatcher.add_handler(filter_handler)

# بدء تشغيل البوت
updater.start_polling()
updater.idle()
