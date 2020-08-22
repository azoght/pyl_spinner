import pygame as pg
import random

pg.init()

# Window
window = pg.display.set_mode((1000, 750))
window.fill((255,0,0))
pg.display.set_caption("Press Your Luck Spinner")

# Press Your Luck Theme
pg.mixer_music.load("files/Press-Your-Luck.ogg")
pg.mixer_music.set_volume(0.75)
pg.mixer_music.play(-1)

# Title Text
font = pg.font.Font("files/Aganè 65 (Bold).ttf", 80)
text = font.render("Press Your Luck!",True,(0,0,0))
textRect = text.get_rect()
textRect.center = (500,375)
window.blit(text,textRect)

clock = pg.time.Clock()
gifClock = pg.time.Clock()

# Variables
spins = random.randint(4, 20)

start = False
stop = False

run = True
GIF = False
s = True

themePlayed = False
counting = False

money = 0
whammies = 0

reward = 0
f = 0

message = ""

# Whammy Icon
Whammy = pg.image.load("files/Whammy.png")
whammy = pg.transform.scale(Whammy,(80,155))

# Winnings/Reward Rect
win_rect = text.get_rect()
win_rect.center = (500, 200)

# Text for Spin Buttons
smallfont = pg.font.Font("files/DejaVuSans.ttf", 20)
startbuttonText = smallfont.render("Start Spin",True,(0,0,0))
texrect2 = startbuttonText.get_rect()
texrect2.center = (438,490)
stopbuttonText = smallfont.render("Stop Spin",True,(0,0,0))
texrect3 = stopbuttonText.get_rect()
texrect3.center = (542,490)

# Other Fonts
numFont = pg.font.Font("files/STIXGeneralBol.ttf", 60)
numFontSmall = pg.font.Font("files/sans.ttf", 30)

exText = numFontSmall.render("$1000000",True,(0,0,0))
exRect = exText.get_rect()
exRect.right = 1000

spinFont = pg.font.Font("files/STIXGeneralBol.ttf", 30)

spinsLeftFont = pg.font.Font("files/DejaVuSans.ttf", 50)

# Initialization of Money in Bank Rect
bank_rect = exRect

# Functions
def playGif(frames: [], frame: int, x: int, y: int):
    global s
    s = False
    fn = "files/ezgif-2-890a93be7cdd-gif-im/" + frames[frame][0]
    img = pg.image.load(fn)
    for a in range(frames[frame][1] * 50):
        window.blit(img, (x,y))
    s = True

def spinReward() -> int:
    r = random.randint(1,1000)
    if r >= 1 and r <= 369:
        return 1000
    if r >= 370 and r <= 559:
        return 2000
    if r >= 560 and r <= 659:
        return 2500
    if r >= 660 and r <= 704:
        return 5000
    if r >= 705 and r <= 725:
        return 10000
    if r >= 725 and r <= 734:
        return 20000
    if r >= 735 and r <= 739:
        return 25000
    if r >= 740 and r <= 743:
        return 50000
    if r >= 744 and r <= 745:
        return 100000
    if r >= 746 and r <= 747:
        return 250000
    if r >= 748 and r <= 749:
        return 500000
    if r == 750:
        return 1000000
    else:
        return 0

# Frames for Whammy GIF
frames = [["frame_00_delay-1.1s.gif", 150],["frame_01_delay-0.15s.gif", 15],["frame_02_delay-0.15s.gif", 15],["frame_03_delay-0.15s.gif", 15],["frame_04_delay-0.15s.gif", 15],["frame_05_delay-0.15s.gif", 15],["frame_06_delay-0.15s.gif", 15],["frame_07_delay-0.15s.gif", 15],["frame_08_delay-0.15s.gif", 15],["frame_09_delay-0.15s.gif", 15],["frame_10_delay-0.15s.gif", 15],["frame_11_delay-0.15s.gif", 15],["frame_12_delay-0.15s.gif", 15],["frame_13_delay-0.15s.gif", 15],["frame_14_delay-0.15s.gif", 15],["frame_15_delay-0.1s.gif", 10],["frame_16_delay-1.5s.gif", 15],["frame_17_delay-0.15s.gif", 15],["frame_18_delay-0.15s.gif", 15],["frame_19_delay-0.15s.gif", 15],["frame_20_delay-0.15s.gif", 15],["frame_21_delay-0.15s.gif", 15],["frame_22_delay-0.15s.gif", 15],["frame_23_delay-0.15s.gif", 15],["frame_24_delay-0.15s.gif", 15],["frame_25_delay-0.15s.gif", 15],["frame_26_delay-0.15s.gif", 15],["frame_27_delay-0.15s.gif", 15],["frame_28_delay-0.15s.gif", 15],["frame_29_delay-0.15s.gif", 15],["frame_30_delay-0.15s.gif", 15],["frame_31_delay-0.15s.gif", 15],["frame_32_delay-0.15s.gif", 15],["frame_33_delay-0.15s.gif", 15],["frame_34_delay-0.15s.gif", 15],["frame_35_delay-2s.gif", 20]]

# Main Loop
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    mouse = pg.mouse.get_pos()

    # Start and Stop Buttons
    pg.draw.rect(window, (180, 20, 10), (388, 450, 100, 80))
    pg.draw.rect(window, (180, 20, 10), (492, 450, 100, 80))
    window.blit(startbuttonText, texrect2)
    window.blit(stopbuttonText, texrect3)

    # Start Spin Button Clicked
    if 100 + 388 > mouse[0] > 388 and 450 + 80 > mouse[1] > 450:

        if pg.mouse.get_pressed()[0] == 1:
            pg.draw.rect(window, (250, 90, 80), (388, 450, 100, 80))
            if not themePlayed:
                pg.mixer_music.fadeout(500)
                themePlayed = True
            pg.mixer_music.load("files/pyl-board2.wav")
            pg.mixer_music.set_volume(0.75)
            pg.mixer_music.play(-1)
            start = True
            stop = False
    if start:
        reward = spinReward()
        if reward != 0:
            spinText = spinFont.render("${}".format(reward), True, (0, 0, 0))
            spinRect = spinText.get_rect()
            spinRect.center = (490, 685)
            pg.draw.rect(window, (0, 0, 255), (430, 625, 120, 120))
            window.blit(spinText, spinRect)
        else:
            whammyIcon = pg.image.load("files/whammyicon.png")
            whammy_icon = pg.transform.scale(whammyIcon, (120, 120))
            window.blit(whammy_icon, (430, 625))

    # Stop Spin Button Clicked
    if 100 + 492 > mouse[0] > 492 and 450 + 80 > mouse[1] > 450:

        if pg.mouse.get_pressed()[0] == 1:
            pg.mixer_music.stop()
            pg.draw.rect(window, (250, 90, 80), (492, 450, 100, 80))
            start = False
            stop = True

        if reward == 0 and stop:
            pg.draw.rect(window, (255, 0, 0),exRect)
            pg.mixer_music.load("files/Press-Your-Luck-Whammy.ogg")
            pg.mixer_music.play()
            money = 0
            stop = False
            GIF = True

        if reward > 0 and stop:
            counting = True

    # Change Spins Left
    spinsLeftText = spinsLeftFont.render("{}".format(spins), True, (255, 200, 0))
    spinsLeftRect = spinsLeftText.get_rect()
    spinsLeftRect.left = 25
    window.blit(spinsLeftText, spinsLeftRect)

    # Display Winnings
    if counting:
        pg.draw.rect(window, (255, 0, 0), bank_rect)
        winnings = numFont.render("You won ${}!".format(reward), True, (0, 20, 255))
        if reward != -1:
            money += reward
            spins -= 1
            pg.draw.rect(window,(255, 0, 0), spinsLeftRect)
        reward = -1
        win_rect = winnings.get_rect()
        win_rect.center = (500, 200)
        window.blit(winnings, win_rect)
        counting = False

    # Display Money Earned So Far
    bank = numFontSmall.render("${}".format(money),True,(0,0,0))
    bank_rect = bank.get_rect()
    bank_rect.right = 1000
    window.blit(bank,bank_rect)

    # Add Whammies To Screen
    if whammies >= 1:
        window.blit(whammy,(50, 100))

    if whammies >= 2:
        window.blit(whammy,(50, 300))

    if whammies >= 3:
        window.blit(whammy,(50, 500))

    if whammies == 4:
        print("Game over!")
        run = False

    # Display Money Earned After Game
    if spins == 0:
        print("You finished with ${}!".format(money))
        run = False

    # Start Button Pressed
    if start:
        pg.draw.rect(window, (250, 90, 80), (388, 450, 100, 80))
        r = random.randint(1, 10)
        if not GIF:
            pg.draw.rect(window, (255, 0, 0), win_rect)
            pg.display.update(win_rect)

    # Stop Button Pressed
    if stop:
        pg.draw.rect(window, (250, 90, 80), (492, 450, 100, 80))

    # Play Whammy GIF
    if GIF:
        playGif(frames,f,100,150)
        if s:
            f += 1
            if f == len(frames):
                whammies += 1
                spins -= 1
                pg.draw.rect(window, (255, 0, 0), spinsLeftRect)
                stop = False
                GIF = False

    # Stop Whammy GIF
    if not GIF and f == len(frames):
        fn = "files/ezgif-2-890a93be7cdd-gif-im/" + frames[0][0]
        img = pg.image.load(fn)
        pg.draw.rect(window, (255, 0, 0), (100, 150, img.get_width(), img.get_height()))
        window.blit(text, textRect)
        f = 0

    pg.display.update()
    clock.tick(30)
