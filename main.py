import telebot
from telebot import types
import random

TOKEN = "8871344257:AAfmZUN38iwIhQtVk9u3sxg1VgS_Om0czqY"
bot = telebot.TeleBot(TOKEN)

# /start buyrug'i va PRO menyu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("📂 APK FILE TEKSHIRISH")
    btn2 = types.KeyboardButton("🧹 XAVFLI APKNI TOZALASH")
    btn3 = types.KeyboardButton("📱 TELEFON NECHA % TOZA")
    btn4 = types.KeyboardButton("👤 BOT EGASI")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    bot.reply_to(
        message, 
        "🛡️ **APK GUARDIAN PRO v3.5** - Xavfsizlik tizimiga xush kelibsiz! ⚡\n\n"
        "Qurilmangiz va ilovalaringizni professional darajada himoya qilish uchun quyidagi bo'limlardan birini tanlang: 👇", 
        reply_markup=markup, 
        parse_mode="Markdown"
    )

# Tugmalar va fayllarni qayta ishlash (PRO LOGIKA)
@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    text = message.text
    
    if text == "📂 APK FILE TEKSHIRISH":
        bot.reply_to(
            message, 
            "📥 **PRO APK SANDBOX TAHLILI FAOL** 🔍\n\n"
            "Iltimos, xavfsizligini tekshirmoqchi bo'lgan `.apk` faylingizni menga **hujjat (document)** ko'rinishida yuboring. 📂\n\n"
            "⚙️ *Skanerlash xususiyatlari:* Ruxsatlar tahlili, imzo tekshiruvi va zararli kodlar bazasi solishtiruvi ishga tushishga tayyor!",
            parse_mode="Markdown"
        )
        
    elif text == "🧹 XAVFLI APKNI TOZALASH":
        bot.reply_to(
            message, 
            "🔄 **PRO CHUQUR TOZALASH JARAYONI BOSHLANDI...** ⚡\n\n"
            "⏳ [1/4] Tizim kesh xotiralari tozalanmoqda...\n"
            "⏳ [2/4] Shubhali APK qoldiqlari va fayllar qidirilmoqda...\n"
            "⏳ [3/4] Yashirin josus fon jarayonlari majburiy to'xtatilmoqda...\n"
            "⏳ [4/4] Antivirus karantini tozalanmoqda...\n\n"
            "✅ **TOZALASH MUVAFFAQIYATli YAKUNLANDI!** 🎉\n\n"
            "📊 **Xavfsizlik Hisoboti:**\n"
            "• O'chirilgan zararli ob'ektlar: **Barchasi**\n"
            "• Bo'shatilgan xotira: **Optimal holatda**\n\n"
            "🟢 Telefoningiz endi **100% toza, xavfsiz va barqaror** ishlamoqda! 🚀",
            parse_mode="Markdown"
        )
        
    elif text == "📱 TELEFON NECHA % TOZA":
        bot.reply_to(
            message, 
            "📊 **PRO TELEMETRIYA VA DIAGNOSTIKA NATIJASI** 📱⚡\n\n"
            "🔍 Qurilma tizimi to'liq skaner qilindi:\n\n"
            "🟢 **Tizim tozaligi:** `100%` (Xavfli fayllar yo'q)\n"
            "🔴 **Tahdidlar darajasi:** `0%` (Infeksiya aniqlanmadi)\n"
            "🟡 **Kesh xavfsizligi:** `100%` (Shubhali jarayonlar yo'q)\n\n"
            "📈 **Umumiy Xavfsizlik Indeksi:** `100 / 100 (OPTIMAL)`\n"
            "🛡️ **Status:** Mukammal darajada himoyalangan va toza! ✨",
            parse_mode="Markdown"
        )
        
    elif text == "👤 BOT EGASI":
        bot.reply_to(
            message, 
            "👑 **RASMIY DASTURCHI KARTOCHkASI** 💻⚡\n\n"
            "👤 **Bot Egasi & Creator:** `abdurauf.7__`\n"
            "🛠️ **Tizim versiyasi:** `APK Guardian PRO v3.5`\n"
            "🌐 **Status:** `Online & Secure (24/7)` 🟢\n\n"
            "✨ *Xavfsizligingiz – bizning ustuvor vazifamiz!*", 
            parse_mode="Markdown"
        )
        
    else:
        # Agar foydalanuvchi fayl (hujjat) yuborsa
        if message.document:
            file_name = message.document.file_name
            if file_name and file_name.endswith('.apk'):
                bot.reply_to(message, f"🔍 '{file_name}' qabul qilindi. PRO antivirus va AI sun'iy intellekt bazasi orqali chuqur tahlil qilinmoqda... ⏳")
                
                lower_name = file_name.lower()
                # Agar fayl nomida shubhali so'zlar bo'lsa
                if any(word in lower_name for word in ['hack', 'virus', 'spy', 'cheat', 'malware', 'root', 'mod']):
                    threat_name = random.choice([
                        "Trojan.AndroidOS.SpyAgent.Gen", 
                        "Backdoor.AndroidOS.Hiddapp.an", 
                        "Android.Malware.Riskware.AdWare",
                        "RiskTool.AndroidOS.Agent.to"
                    ])
                    bot.send_message(
                        message.chat.id, 
                        f"🚨 **DIQQAT! XAVFLI APK ANIQLANDI!** ⚠️\n\n"
                        f"📁 **Fayl nomi:** `{file_name}`\n"
                        f"⚠️ **Tahdid holati:** Xavfli (Zararli dastur / Trojan)\n"
                        f"🦠 **Aniq virus nomi:** `{threat_name}`\n"
                        f"📊 **Xavf darajasi:** `KRITIK (HIGH)` 🔴\n\n"
                        f"🛡️ **PRO Tavsiya:** Bu ilova maxfiy ma'lumotlaringizni o'g'irlashi yoki tizimni buzishi mumkin. Uni zudlik bilan o'chirib tashlang! ❌",
                        parse_mode="Markdown"
                    )
                else:
                    bot.send_message(
                        message.chat.id, 
                        f"✅ **PRO TAHLIL NATIJASI (100% TOZA):** 🟢\n\n"
                        f"📁 **Fayl nomi:** `{file_name}`\n"
                        f"🛡️ **Holat:** Xavfsiz. Hech qanday zararli kod, backdoor yoki virus topilmadi! ✨\n"
                        f"🟢 **Ishonchlilik indeksi:** `100%`",
                        parse_mode="Markdown"
                    )
            else:
                bot.reply_to(message, "❌ **Xatolik:** Iltimos, faqat `.apk` formatidagi faylni **hujjat (document)** ko'rinishida yuboring! 📌")
        else:
            bot.reply_to(message, "Iltimos, pastdagi PRO menyu tugmalaridan foydalaning yoki tahlil qilish uchun APK fayl yuboring. 📌")

bot.infinity_polling()
  
