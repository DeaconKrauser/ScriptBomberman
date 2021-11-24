import pyautogui, time, schedule, requests, datetime


def primeiraFase():
    pyautogui.PAUSE = 2
    maldrehswamp = pyautogui.click(x=706, y=630)
    time.sleep(5)
    level1 = pyautogui.click(x=727, y=864)
    time.sleep(5)
    start = pyautogui.click(x=978, y=896)
    time.sleep(20)
    restart = pyautogui.click(x=987, y=691)
    time.sleep(5)
    
    token = "2103902520:AAFfFuSjmCFlAKPz62rU1TvuvXwznL-l4sU"
    message = (f"Attack performed at {datetime.datetime.now()}").replace('.', '')
    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-794355163}&text={message}'
    resultado = requests.get(url_base)
    print(resultado)

        
schedule.every(1).hour.do(primeiraFase)

while True:
    schedule.run_pending()
    time.sleep(5)