import pyautogui, time


pyautogui.PAUSE = 2

time.sleep(5)
posicao = pyautogui.position()
print(posicao)

# pyautogui.scroll(-100)
# x = range(12)

# for n in x:
#     heros = pyautogui.click(x=712, y=898)
#     time.sleep(5)

# pyautogui.scroll(-100)

# pyautogui.moveTo(x=1739, y=689)
# pyautogui.mouseDown()
# pyautogui.moveTo(1741, y=762)
# pyautogui.mouseUp()
# pyautogui.click(x=1748, y=921)


# #abrir navegador
# time.sleep(2)
# browser = pyautogui.click(x=25, y=546)

# #digitar link
# binemon = pyautogui.click(x=667, y=73)
# site = pyautogui.write("https://app.binemon.io/buy/mons")
# ir_ao_site = pyautogui.press("enter")

# # logar na conta metamask
# metamask = pyautogui.click(x=1833, y=79)
# senha = pyautogui.write("UFfn]cY>i7")
# logar = pyautogui.press("enter")
# assinar = pyautogui.click(x=1809, y=630)
# exit_wallet = pyautogui.click(x=1383, y=281)

# time.sleep(1)
# mon = pyautogui.click(x=1832, y=326)
# time.sleep(1)
# lowest_price = pyautogui.click(x=1819, y=403)

# price_mon = "500"

# if price_mon == "600":
#     buy = pyautogui.click(x=629, y=508)