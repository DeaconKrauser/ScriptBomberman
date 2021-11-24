import requests, json, time, pyautogui
import schedule


def monRankE():
    
    url = f'https://api.binemon.io/api/binemons/?isEgg=false&isOnAuction=true&limit=60&page=1&sort=PRICE_UP'

    headers = {
    'authority': 'api.binemon.io',
    'accept': 'application/json, text/plain, */*',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTUyODYzYjdkYjBjYTNhNjg3OGRjM2IiLCJ1c2VyVHlwZSI6InJlZ2lzdGVyZWQiLCJpYXQiOjE2MzI3OTgzNDIsImV4cCI6MTY0MDU3NDM0Mn0.5LEX-OYADC6nwlWwRONNqfu405P6sqc2I_cSSPl28tE',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'sec-gpc': '1',
    'origin': 'https://app.binemon.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://app.binemon.io/',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.request("GET", url, headers=headers)
    res = json.loads(response.text)
    
    priceMonE = 200
    priceMonD = 400
    priceMonC = 700

    for b in res['response']:
        tokenID = b['tokenID']
        id_mon = b['_id']
        rank = b['rank']
        startingPrice = b['startingPrice']
        endPrice = b['endingPrice']
        token_telegram = "2061582833:AAFFQaxqA2E_AEtpVAykveYuiaY4dMeev-g"

        if startingPrice <= priceMonE and rank == 1:
            print("mon", startingPrice, rank, tokenID)
            print(f'Efetuando compra de mon RANK D\n {tokenID}')
            search = pyautogui.click(x=1124, y=89)
            time.sleep(0.1)
            keyboard = pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            url = pyautogui.write("https://app.binemon.io/binemon/225460")
            time.sleep(0.1)
            keyboard2 = pyautogui.press("enter")
            time.sleep(5)
            sing = pyautogui.click(x=1831, y=634)
            time.sleep(0.5)
            buy = pyautogui.click(x=1299, y=913)
            time.sleep(5)

            pyautogui.moveTo(x=1739, y=689)
            pyautogui.mouseDown()
            pyautogui.moveTo(1741, y=762)
            pyautogui.mouseUp()
            pyautogui.click(x=1748, y=921)

            time.sleep(5)
            confirmar = pyautogui.click(x=1812, y=722)
            time.sleep(10)
            message = (f"compra de mon efetuada\nPreço: {startingPrice}\nToken: {tokenID}\nID MON: {id_mon}")
            url_base = f'https://api.telegram.org/bot{token_telegram}/sendMessage?chat_id={-623866746}&text={message}'
            resultado = requests.get(url_base)
            print(resultado.json())
            break
        if startingPrice <= priceMonD and rank == 2:
            print("mon", startingPrice, rank, tokenID)
            print(f'Efetuando compra de mon RANK D\n {tokenID}')
            search = pyautogui.click(x=1124, y=89)
            time.sleep(0.1)
            keyboard = pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            url = pyautogui.write("https://app.binemon.io/binemon/225460")
            time.sleep(0.1)
            keyboard2 = pyautogui.press("enter")
            time.sleep(5)
            sing = pyautogui.click(x=1831, y=634)
            time.sleep(0.5)
            buy = pyautogui.click(x=1299, y=913)
            time.sleep(5)

            pyautogui.moveTo(x=1739, y=689)
            pyautogui.mouseDown()
            pyautogui.moveTo(1741, y=762)
            pyautogui.mouseUp()
            pyautogui.click(x=1748, y=921)

            time.sleep(5)
            confirmar = pyautogui.click(x=1812, y=722)
            time.sleep(10)
            message = (f"compra de mon efetuada\nPreço: {startingPrice}\nToken: {tokenID}\nID MON: {id_mon}")
            url_base = f'https://api.telegram.org/bot{token_telegram}/sendMessage?chat_id={-623866746}&text={message}'
            resultado = requests.get(url_base)
            print(resultado.json())
            break
        if startingPrice <= priceMonC and rank == 3:
            print("mon", startingPrice, rank, tokenID)
            print(f'Efetuando compra de mon RANK D\n {tokenID}')
            search = pyautogui.click(x=1124, y=89)
            time.sleep(0.1)
            keyboard = pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.1)
            url = pyautogui.write("https://app.binemon.io/binemon/225460")
            time.sleep(0.1)
            keyboard2 = pyautogui.press("enter")
            time.sleep(5)
            sing = pyautogui.click(x=1831, y=634)
            time.sleep(0.5)
            buy = pyautogui.click(x=1299, y=913)
            time.sleep(5)

            pyautogui.moveTo(x=1739, y=689)
            pyautogui.mouseDown()
            pyautogui.moveTo(1741, y=762)
            pyautogui.mouseUp()
            pyautogui.click(x=1748, y=921)

            time.sleep(5)
            confirmar = pyautogui.click(x=1812, y=722)
            time.sleep(10)
            message = (f"compra de mon efetuada\nPreço: {startingPrice}\nToken: {tokenID}\nID MON: {id_mon}")
            url_base = f'https://api.telegram.org/bot{token_telegram}/sendMessage?chat_id={-623866746}&text={message}'
            resultado = requests.get(url_base)
            print(resultado.json())
            break
        else:
            print("nenhum mon encontrado")
            break

schedule.every(5).minutes.do(monRankE)

while True:
    schedule.run_pending()
    time.sleep(5)