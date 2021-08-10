from config import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import filters, Client, sync
import time, re

print('Bot started')
client = Client('bot', pl_id, pl_hash)
client.start()
client.stop()
print('Bot worked!')

aaaaaaa = ""
a = 0
b = 0
def bonus_free_getus():
    global client, s, bonus_timer_free
    print("Бонус получен")
    client.send_message("LesyaTG_bot", "бонус")
    
def bonus_vip_getus():
    global client, s, bonus_timer_vip
    print("Бонус vip получен")
    client.send_message("LesyaTG_bot", "бонус vip")
    
def bonus_premium_getus():
    global client, s, bonus_timer_prem
    print("Бонус premium получен")
    client.send_message("LesyaTG_bot", "бонус premium")
    
def fight_auto():
    global client, s, a
    a += 1
    print("auto_fight", a, "min")
    client.send_message("LesyaTG_bot", "Бой")



@client.on_message(filters.regex('^[МмVv][ЕеTt][YyНн][Юю\>\.]$') & filters.me)
def menu_send_handler(client, message):
    menu = '''
    Меню:
1. Открыть гейс (напишите меню 1)
P.S Бои и бонус забираются автоматически (Если что можно настроить в файле config.py интервал между заберанием бонуса)
Будет писаться о том что вы открываете 10 кейсов,на самом деле вы открываете ваш лимит.
    '''
    client.send_message(message.chat.id, menu)
    
@client.on_message(filters.regex('^[МмVv][ЕеTt][YyНн][Юю\>\.] [1-3]$') & filters.me)
def menu2_send_handler(client, message):
    number = re.sub(r'^[МмVv][ЕеTt][YyНн][Юю\>\.] ', '', message.text)
    if number == "1":
        client.send_message(message.chat.id, """
        Для открытия кейсов введите команду
        гейс [номер_кейс] [количество_кейсов] [Время_один_кейс_в_секунду]
        Например
        "Гейс 10 5 30"
        """)
    elif number == "2":
        client.send_message(message.chat.id, """
        Для примера оставил
        """)        
        
        

@client.on_message(filters.regex('^\![ГгUu][ЕеTt][ЙйQq][СсCc]') & filters.me)
def case_open_handler(client, message):
    global aaaaaaa
    aaaaaaa = "stop"
   
@client.on_message(filters.regex('^[ГгUu][ЕеTt][ЙйQq][СсCc] [1-5]{1} \d{1,} \d{1,}') & filters.me)
def case_open_handler(client, message):
    global aaaaaaa
    getarg = re.sub(r'^[ГгUu][ЕеTt][ЙйQq][СсCc] ', '', message.text)
    result = getarg.split(" ")
    count = int(result[1])
    while count > 0:
        if aaaaaaa == "stop":
            aaaaaaa = ""
            break
            
        count -= 1
        client.send_message(message.chat.id, f"кейс открыть {result[0]} 10") # Число 3 в конце можете сменить на то,которое можете открывать вы
        time.sleep(int(result[2]))
    client.send_message(message.chat.id, "Всё")


@client.on_message(filters.regex('^[Бб\<\,][ОоJj][ЙйQq] \d{1,}') & filters.me)
def case_open_handler(client, message):
    number = re.sub(r'^[Бб\<\,][ОоJj][ЙйQq] ', '', message.text)


scheduler = AsyncIOScheduler()
scheduler.add_job(bonus_free_getus, "interval", hours=bonus_timer_free)
if bonus_vip_active:
    scheduler.add_job(bonus_vip_getus, "interval", hours=bonus_timer_vip)
if bonus_premium_active:
    scheduler.add_job(bonus_premium_getus, "interval", hours=bonus_timer_prem)
scheduler.add_job(fight_auto, "interval", minutes=fight_timer,)

scheduler.start()
client.run()