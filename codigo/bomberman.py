import telegram, requests, pyautogui, time, schedule, requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from enum import auto
import pyscreenshot as ImageGrab


TOKEN = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

#RESTART APLICATION CAPTURE INICIALIZATION
def restart(update, context):
    pyautogui.PAUSE = 5
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Reiniciando")
    
    #START PROCESS
    refresh = pyautogui.press("f5")
    time.sleep(10)
    connect_wallet = pyautogui.click(x=1001, y=758)
    time.sleep(10)
    connect_wallet_metamask = pyautogui.click(x=967, y=625)
    time.sleep(10)
    connect_wallet_confirm = pyautogui.click(x=1811, y=628)
    time.sleep(5)
    connect_wallet_confirm1 = pyautogui.click(x=1811, y=628)
    time.sleep(5)
    # fullscreen = pyautogui.click(x=1472, y=905)
    #END PROCESS
    
    #PICTURE CAPTURE
    im = ImageGrab.grab()
    im.save("connect_wallet.png")
    #END PICTURE CAPTURE
    
    #TELEGRAM ALERT 
    try:
        #ALERT
        files={'photo':open("connect_wallet.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
    #END TELEGRAM ALERT
#END APLICATION APLICATION CAPTURE INICIALIZATION

#START INICIALIZATION
def iniciar(update, context):
    pyautogui.PAUSE = 5
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Executando")
    
    #START AUTO PLAY SELECT HEROES
    heros_return = pyautogui.click(x=77, y=50)
    time.sleep(10)
    heroes = pyautogui.click(x=1794, y=956)
    time.sleep(10)
    scroll_map = pyautogui.moveTo(x=544, y=404)
    time.sleep(5)
    scroll = pyautogui.scroll(-100)
    time.sleep(5)
    
    x = range(13)

    for n in x:
        heros = pyautogui.click(x=712, y=898)
        time.sleep(2)

    exit = pyautogui.click(x=967, y=191)
    time.sleep(3)
    play = pyautogui.click(x=958, y=532)
    time.sleep(3)
    #END AUTO PLAY SELECT HEROES

    #PICTURE CAPTURE
    im = ImageGrab.grab()
    im.save("teste_bot.png")
    #END PICTURE CAPTURE
    
    #TELEGRAM ALERT 
    try:
        #ALERT
        message_sucess = ("Iniciando Mapa")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_sucess}'
        resultado = requests.get(telegram)
        print(resultado.json())
        files={'photo':open("teste_bot.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
    #END TELEGRAM ALERT
#END INICIALIZATION

def bcoins(update, context):
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Abrindo Báu")
    bcoin = pyautogui.click(x=1725, y=53)
    
    time.sleep(5)
    im = ImageGrab.grab()
    im.save("bcoins.png")
    time.sleep(5)

    try:
        #ALERT
        files={'photo':open("bcoins.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
    time.sleep(3)
    exit = pyautogui.click(x=1445, y=197)

def bcoinsHome(update, context):
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Abrindo Báu")
    bcoin = pyautogui.click(x=1844, y=50)

    time.sleep(5)
    im = ImageGrab.grab()
    im.save("bcoinsHome.png")
    time.sleep(5)

    try:
        #ALERT
        files={'photo':open("bcoinsHome.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
    time.sleep(3)
    exit = pyautogui.click(x=1445, y=197)

def Heroes(update, context):
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Status Heros")
    heroes = pyautogui.click(x=1795, y=953)

    time.sleep(5)
    captura_picture = ImageGrab.grab()
    captura_picture.save("heroes.png")
    time.sleep(5)

    try:
        #ALERT
        files={'photo':open("heroes.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
    time.sleep(3)
    exit = pyautogui.click(x=963, y=195)

def nextMapa(update, context):
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Iniciando Novo Mapa")
    mapa = pyautogui.click(x=949, y=873)
    
#START CAPTURA
def captura(update, context):
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    context.bot.send_message(chat_id=update.effective_chat.id, text="Capturando")

    captura_picture = ImageGrab.grab()
    captura_picture.save("captura.png")
    print('Enviando alerta')

    try:
        #ALERT
        files={'photo':open("captura.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())
#END CAPTURA

restart_handler = CommandHandler('restart', restart)
dispatcher.add_handler(restart_handler)

iniciar_handler = CommandHandler('iniciar', iniciar)
dispatcher.add_handler(iniciar_handler)

bcoins_handler = CommandHandler('bcoins', bcoins)
dispatcher.add_handler(bcoins_handler)

bcoinsHome_handler = CommandHandler('bcoinsHome', bcoinsHome)
dispatcher.add_handler(bcoinsHome_handler)

Heroes_handler = CommandHandler('Heroes', Heroes)
dispatcher.add_handler(Heroes_handler)

nextMapa_handler = CommandHandler('nextMapa', nextMapa)
dispatcher.add_handler(nextMapa_handler)

captura_handler = CommandHandler('captura', captura)
dispatcher.add_handler(captura_handler)

updater.start_polling()