from cv2 import cv2
import numpy as np
import mss, pyautogui, time, sys, yaml, requests
import pyscreenshot as ImageGrab

if __name__ == '__main__':
    stream = open("config.yaml", 'r')
    c = yaml.safe_load(stream)
ct = c['trashhold']

pyautogui.PAUSE = c['time_intervals']['interval_between_moviments']

pyautogui.FAILSAFE = True
hero_clicks = 0
login_attempts = 0

crashed_img = cv2.imread('crashed.png') 
go_work_img = cv2.imread('targets/go-work.png')
commom_img = cv2.imread('targets/commom-text.png')
arrow_img = cv2.imread('targets/go-back-arrow.png')
hero_img = cv2.imread('targets/hero-icon.png')
x_button_img = cv2.imread('targets/x.png')
teasureHunt_icon_img = cv2.imread('targets/treasure-hunt-icon.png')
ok_btn_img = cv2.imread('targets/ok.png')
connect_wallet_btn_img = cv2.imread('targets/connect-wallet.png')
select_wallet_hover_img = cv2.imread('targets/select-wallet-1-hover.png')
select_metamask_no_hover_img = cv2.imread('targets/select-wallet-1-no-hover.png')
sign_btn_img = cv2.imread('targets/select-wallet-2.png')
new_map_btn_img = cv2.imread('targets/new-map.png')
green_bar = cv2.imread('targets/green-bar.png')


def dot():
    sys.stdout.write(".")
    sys.stdout.flush()


def clickBtn(img, name=None, timeout=3, trashhold = ct['default']):
    dot()
    if not name is None:
        pass
    start = time.time()
    clicked = False
    while(not clicked):
        matches = positions(img, trashhold=trashhold)
        if(len(matches)==0):
            hast_timed_out = time.time()-start > timeout
            if(hast_timed_out):
                if not name is None:
                    pass
                return False
            continue

        x,y,w,h = matches[0]
        pyautogui.moveTo(x+w/2,y+h/2,1)
        pyautogui.click()
        return True

def printSreen():
    with mss.mss() as sct:
        monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        sct_img = np.array(sct.grab(sct.monitors[0]))
        return sct_img[:,:,:3]

def positions(target, trashhold=ct['default']):
    img = printSreen()
    result = cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]
    yloc, xloc = np.where(result >= trashhold)
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def scroll():
    commoms = positions(commom_img, trashhold = ct['commom'])
    if (len(commoms) == 0):
        return
    x,y,w,h = commoms[len(commoms)-1]
    pyautogui.moveTo(x,y,1)

    if not c['use_click_and_drag_instead_of_scroll']:
        pyautogui.scroll(-c['scroll_size'])
    else:
        pyautogui.dragRel(0,-c['click_and_drag_amount'],duration=1)

def clickButtons():
    buttons = positions(go_work_img, trashhold=ct['go_to_work_btn'])
    for (x, y, w, h) in buttons:
        pyautogui.moveTo(x+(w/2),y+(h/2),1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
    return len(buttons)

def isWorking(bar, buttons):
    y = bar[1]

    for (_,button_y,_,button_h) in buttons:
        isBelow = y < (button_y + button_h)
        isAbove = y > (button_y - button_h)
        if isBelow and isAbove:
            return False
    return True

def clickGreenBarButtons():
    offset = 130
    green_bars = positions(green_bar, trashhold=ct['green_bar'])
    buttons = positions(go_work_img, trashhold=ct['go_to_work_btn'])

    not_working_green_bars = []
    for bar in green_bars:
        if not isWorking(bar, buttons):
            not_working_green_bars.append(bar)
    if len(not_working_green_bars) > 0:
        sys.stdout.write('\nclicking in %d heroes.' % len(not_working_green_bars))

    for (x, y, w, h) in not_working_green_bars:
        pyautogui.moveTo(x+offset+(w/2),y+(h/2),1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
    return len(not_working_green_bars)

def goToHeroes():
    if clickBtn(arrow_img):
        global login_attempts
        login_attempts = 0
    clickBtn(hero_img)

def goToGame():
    clickBtn(x_button_img)
    clickBtn(x_button_img)
    clickBtn(teasureHunt_icon_img)

def refreshHeroesPositions():
    clickBtn(arrow_img)
    clickBtn(teasureHunt_icon_img)
    clickBtn(teasureHunt_icon_img)

def login():
    global login_attempts
    if login_attempts > 3:
        sys.stdout.write('\ntoo many login attempts, refreshing.')
        login_attempts = 0
        pyautogui.press('f5')
        return

    if clickBtn(connect_wallet_btn_img, name='connectWalletBtn', timeout = 10):
        sys.stdout.write('\nConnect wallet button detected, logging in!')

    if clickBtn(sign_btn_img, name='sign button', timeout=8):
        login_attempts = login_attempts + 1
        if clickBtn(teasureHunt_icon_img, name='teasureHunt', timeout = 15):
            login_attempts = 0
        return

    if not clickBtn(select_metamask_no_hover_img, name='selectMetamaskBtn'):
        if clickBtn(select_wallet_hover_img, name='selectMetamaskHoverBtn', trashhold = ct['select_wallet_buttons'] ):
            pass
    else:
        pass

    if clickBtn(sign_btn_img, name='signBtn', timeout = 20):
        login_attempts = login_attempts + 1
        if clickBtn(teasureHunt_icon_img, name='teasureHunt', timeout=25):
            login_attempts = 0

    if clickBtn(ok_btn_img, name='okBtn', timeout=5):
        pass

def refreshHeroes():
    goToHeroes()
    if c['only_click_heroes_with_green_bar']:
        print('\nSending heroes with an green stamina bar to work!')
    else:
        sys.stdout.write('\nSending all heroes to work!')
    buttonsClicked = 1
    empty_scrolls_attempts = 3
    while(empty_scrolls_attempts >0):
        if c['only_click_heroes_with_green_bar']:
            buttonsClicked = clickGreenBarButtons()
        else:
            buttonsClicked = clickButtons()
        if buttonsClicked == 0:
            empty_scrolls_attempts = empty_scrolls_attempts - 1
        scroll()
        time.sleep(2)
    sys.stdout.write('\n{} heroes sent to work so far'.format(hero_clicks))
    goToGame()
    token = "2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ"
    
    time.sleep(5)
    im = ImageGrab.grab()
    im.save("bcoinsinMap.png")
    time.sleep(5)

    try:
        #ALERT
        files={'photo':open("bcoinsinMap.png", 'rb')}
        resp = requests.post('https://api.telegram.org/bot2052342020:AAG5ZW9--7KFef6PmNFTA60I9MbCwueVSQQ/sendPhoto?chat_id=-729635018', files=files)
        print(resp.status_code)
    except:
        #ALERT
        message_failed = ("Aplicação com o seguinte erro")
        telegram = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={-729635018}&text={message_failed}'
        resultado = requests.get(telegram)
        print(resultado.json())

def main():
    time.sleep(5)
    t = c['time_intervals']

    last = {
    "login" : 0,
    "heroes" : 0,
    "new_map" : 0,
    "refresh_heroes" : 0
    }

    while True:
        now = time.time()

        if now - last["heroes"] > t['send_heroes_for_work'] * 60:
            last["heroes"] = now
            sys.stdout.write('\nSending heroes to work.')
            refreshHeroes()
            sys.stdout.write("\n")

        if now - last["login"] > t['check_for_login'] * 60:
            sys.stdout.write("\nChecking if game has disconnected.")
            sys.stdout.flush()
            last["login"] = now
            login()
            sys.stdout.write("\n")

        if now - last["new_map"] > t['check_for_new_map_button']:
            last["new_map"] = now
            if clickBtn(new_map_btn_img):
                with open('new-map.log','a') as new_map_log:
                    new_map_log.write(str(time.time())+'\n')
                sys.stdout.write('\nNew Map button clicked!\n')

        if now - last["refresh_heroes"] > t['refresh_heroes_positions'] * 60 :
            last["refresh_heroes"] = now
            sys.stdout.write('\nRefreshing Heroes Positions.\n')
            refreshHeroesPositions()

        sys.stdout.write(".")
        sys.stdout.flush()

        time.sleep(1)
main()