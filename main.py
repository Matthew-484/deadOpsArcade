import pygame as pg
from tkinter import *
import math
import random

# initialize loadoats
playerImg = "./assets/player_red.png"

# button functions


def click(colour, colour_num):
    global playerImg
    if colour == "red":
        playerImg = "./assets/player_red.png"
    elif colour == "blue":
        playerImg = "./assets/player_blue.png"
    elif colour == "purple":
        playerImg = "./assets/player_purple.png"
    elif colour == "teal":
        playerImg = "./assets/player_teal.png"

    colour_change(colour_num)


def colour_change(colour_num):
    btn_list = [red_btn, blue_btn,
                purple_btn, teal_btn]
    for num in range(len(btn_list)):
        if num == colour_num:
            if colour_num == 0:
                btn_list[num].configure(bg="red")
            elif colour_num == 1:
                btn_list[num].configure(bg="blue")
            elif colour_num == 2:
                btn_list[num].configure(bg="purple")
            elif colour_num == 3:
                btn_list[num].configure(bg="teal")
        else:
            btn_list[num].configure(bg="white")


def attachment_selection(attachment_num):
    global attachments_selected, buttonList
    selection_count = 0

    attachments_selected[attachment_num] = not attachments_selected[attachment_num]
    for selected in range(len(attachments_selected)):
        if attachments_selected[selected]:
            selection_count += 1
            buttonList[selected].configure(
                bg='blue')
        else:
            buttonList[selected].configure(
                bg='white')

    if selection_count >= 2:
        for disabled in range(len(attachments_selected)):
            if not attachments_selected[disabled]:
                buttonList[disabled].configure(state=DISABLED)
    else:
        for active in range(len(attachments_selected)):
            if not attachments_selected[active]:
                buttonList[active].configure(state=ACTIVE)


def close_window():
    window.destroy()


# window setup
window = Tk()
window.title("Loadout Selection")
window.geometry("800x750")
window.configure(bg="white")

# PLAYER SELECION

# Player selection button label
playerLabel = Label(window, text="Choose your Player",
                    fg="black", font=('Arial', 25), justify='center', bg="white")
playerLabel.grid(row=0, column=0, sticky="", pady=20, padx=150)

buttonFrame1 = Frame(window, bg="white")
buttonFrame1.grid(row=1, column=0, columnspan=2)

# Buttons to choose player colour
red_btn = Button(buttonFrame1, text="Red", width=20, height=3, bg="white",
                 command=lambda: click("red", 0))
red_btn.grid(row=1, column=0, padx=8)

blue_btn = Button(buttonFrame1, text="Blue", width=20, height=3, command=lambda: click("blue", 1),
                  bg="white")
blue_btn.grid(row=1, column=1, padx=8)

purple_btn = Button(buttonFrame1, text="Purple", width=20, height=3, command=lambda: click("purple", 2),
                    bg="white")
purple_btn.grid(row=1, column=2, padx=8)

teal_btn = Button(buttonFrame1, text="Teal", width=20, height=3, command=lambda: click("teal", 3),
                  bg="white")
teal_btn.grid(row=1, column=3, padx=8)

# WEAPON ATTACHMENTS
attachments_label = Label(window, text='Choose your attachments (max of 2)', font=(
    'Arial', 25), justify='center', bg="white")
attachments_label.grid(row=2, column=0, padx=150, sticky='', pady=20)

# Lining up the buttons
buttonFrame2 = Frame(window, bg="white")
buttonFrame2.grid(row=3, column=0, columnspan=2)
attachments_selected = [False, False, False, False]

# attachment buttons
fast_mags_btn = Button(buttonFrame2, text="Fast Magazine", width=20, height=3,
                       bg='white', command=lambda: attachment_selection(0))
fast_mags_btn.grid(row=4, column=0, padx=8)

fmj_btn = Button(buttonFrame2, text="FMJ", width=20, height=3,
                 bg='white', command=lambda: attachment_selection(1))
fmj_btn.grid(row=4, column=1, padx=8)

rapid_fire_btn = Button(buttonFrame2, text='Rapid Fire', width=20, height=3,
                        bg='white', command=lambda: attachment_selection(2))
rapid_fire_btn.grid(row=4, column=2, padx=8)

extendo_btn = Button(buttonFrame2, text='Extended Magazine', width=20, height=3,
                     bg='white', command=lambda: attachment_selection(3))
extendo_btn.grid(row=4, column=3, padx=8)
buttonList = [fast_mags_btn, fmj_btn, rapid_fire_btn, extendo_btn]

# close window
done_btn = Button(window, text="Done",
                  width=20, height=3, command=close_window, bg="white")
done_btn.grid(row=4, column=0, pady=40, sticky=W, padx=85)

window.mainloop()


# game window
pg.init()
font = pg.font.SysFont("ArialBold", 50)
# TODO: ADD TIME ASPECT

width = 1300
height = 800
screen = pg.display.set_mode((width, height))

background = pg.image.load("./assets/background.jpg")

# Player Details
playerImg = pg.image.load(playerImg)
playerImg = pg.transform.scale(playerImg, (64, 64))
playerX = int(width/2)
playerY = int(height/2)
playerImg_rect = playerImg.get_rect(topleft=(playerX, playerY))
player_speed = 8

# Zombie Details
zombieImgs = []
zombieImg_rects = []
zombiesX = []
zombiesY = []
zombiesX_change = []
zombiesY_change = []
zombies_health = []
zombie_flip = []
zombie_hit = []
zombie_hit_bullet = []
zombie_alive = []
zombies_speed = 3


# Bullet Details
bulletImg = pg.image.load('./assets/bullet.png')
bulletImgs = []
bulletImg_rects = []
bulletsX = []
bulletsY = []
bulletsX_change = []
bulletsY_change = []
bullet_on_screen = []
num_bullets = 0
bullet_speed = 16
clip = 5
ammo_storage = 20

# initialize game conditions
zombie_count = 5
zombie_health = 100
player_lives = 3
bullet_damage = 50
fire_rate = 1  # in seconds
magazine_size = 10
reload_rate = 3  # in seconds
coll_space = 10
round = 1
score = 0
displayText = False
score_multiplier = 1

# initialize extra life details
heartImg = pg.image.load("./assets/heart.png")
heartX = []
heartY = []
heartImg_rect = []
heart_exists = False

# initialize double points details
doubleImg = pg.image.load('./assets/double_points.png')
doubleX = []
doubleY = []
doubleImg_rect = []
double_exists = False

# initializing timer values
clock = pg.time.Clock()
current_time = 0

# double timer values
double_time = 0
activated = False
double_text = font.render("Double Points: " + str(5), True, (255, 255, 255))
double_timer_value = 0

# fire rate timer values
fire_time = 0

# reload timer value
reload_time = 0
reload_activated = False
reload_timer_value = 0

# Setting text score properties
scoreText = font.render("Score: " + str(score), True, (255, 255, 255))

def showScore(scoreText):
    screen.blit(scoreText, (10, height - 50))

# Setting round text properties
roundText = font.render("Round: " + str(round), True, (255, 255, 255))

def showRound(roundText):
    screen.blit(roundText, (10, 10))

# Setting lives text properties
livesText = font.render("Lives: " + str(player_lives), True, (255,255,255))

def showLives(livesText):
    screen.blit(livesText, (width - 150, height - 50))

game_over_text = font.render("Game Over", True, (255, 255,255))
final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))

def showGameOver(displayText, final_score_text):
    if displayText:
        screen.blit(game_over_text, ((width / 2) - 100, (height / 2) - 50))
        screen.blit(final_score_text, ((width / 2) - 125, height / 2))

def player(image, image_rect, x, y):
    image_rect.topleft=(x, y)
    screen.blit(image, image_rect)

def get_components(x1, y1, x2, y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    components = [xdiff, ydiff]

    return components


def rotate_player(surface, angle):
    rotated_surface = pg.transform.rotozoom(surface, -angle, 1)
    rotated_rectangle = rotated_surface.get_rect(center=(playerX + 32, playerY + 32))

    return rotated_surface, rotated_rectangle

def resetZombies():
    global zombies_health, zombiesX_change, zombiesY_change, zombieImgs, zombie_flip, zombie_hit, zombie_alive, zombiesX, zombiesY, zombie_hit_bullet
    zombies_health = []
    zombiesX_change = []
    zombiesY_change = []
    zombieImgs = []
    zombie_flip = []
    zombie_hit = []
    zombie_alive = []
    zombiesX = []
    zombiesY = []
    zombie_hit_bullet = []

    for x in range(zombie_count):
        zombies_health.append(zombie_health)
        zombiesX_change.append(1)
        zombiesY_change.append(1)
        zombieImgs.append(pg.image.load('./assets/zombie.png'))
        zombie_flip.append(False)
        zombie_hit.append(False)
        zombie_alive.append(True)
        zombie_hit_bullet.append(False)

resetZombies()

def setZombieCoordinates():
    for zombie1 in range(zombie_count):
        zombieY = random.randint(-150, 950)
        if zombieY >= 0 and zombieY <= height + 32:
            zombieX = random.randint(-200, -32)
        else:
            zombieX = random.randint(-150, width + 150)

        zombiesX.append(zombieX)
        zombiesY.append(zombieY)
        zombieImg_rects.append(zombieImgs[zombie1].get_rect(topleft=(zombiesX[zombie1], zombiesY[zombie1])))


def createBullet(player_angle, x, y):
    bulletsX.append(x)
    bulletsY.append(y)
    bulletImgs.append(pg.transform.rotozoom(bulletImg, -(player_angle * (180/math.pi) + 80), 1))
    bulletImg_rects.append(bulletImgs[-1].get_rect(center=(bulletsX[-1], bulletsY[-1])))
    x_change = bullet_speed * math.cos(player_angle)
    y_change = bullet_speed * math.sin(player_angle)
    bulletsX_change.append(x_change)
    bulletsY_change.append(y_change)
    bullet_on_screen.append(True)

def bullets(num_bullets):
    for bullet_number in range(num_bullets):
        bulletImg_rects[bullet_number] = bulletImgs[bullet_number].get_rect(center=(bulletsX[bullet_number], bulletsY[bullet_number]))
        screen.blit(bulletImgs[bullet_number], bulletImg_rects[bullet_number]) 

setZombieCoordinates()

def zombies(zombieImgs, playerX):
    for zombie2 in range(len(zombie_alive)):
        zombieImg_rects[zombie2] = zombieImgs[zombie2].get_rect(topleft=(zombiesX[zombie2], zombiesY[zombie2]))
        screen.blit(zombieImgs[zombie2], zombieImg_rects[zombie2])
        if zombiesX[zombie2] > playerX and not zombie_flip[zombie2]:
                zombieImgs[zombie2] = pg.transform.flip(
                    zombieImgs[zombie2], True, False)
                zombie_flip[zombie2] = True
        elif zombiesX[zombie2]  < playerX and zombie_flip[zombie2]:
            zombieImgs[zombie2] = pg.transform.flip(
                zombieImgs[zombie2], True, False)
            zombie_flip[zombie2] = False

def removeZombie(index):
    global zombie_count
    zombiesX_change[index] = 0
    zombiesY_change[index] = 0
    zombiesX[index] = -300
    zombiesY[index] = -300
    zombie_alive[index] = False

    zombie_count -= 1

def removeBullet(bullet_index):
    bulletsX_change[bullet_index] = 0
    bulletsY_change[bullet_index] = 0
    bullet_on_screen[bullet_index] = False

def updateRound():
    global roundText
    roundText = font.render("Round: " + str(round), True, (255, 255, 255))

def roundChange():
    global zombie_count, round, bulletImgs, bulletImg_rects, bulletsX, bulletsY, bulletsX_change, bulletsY_change, bullet_on_screen, num_bullets, zombie_health
    zombie_health += 5
    zombie_count = 5 + round
    round += 1
    bulletImgs = []
    bulletImg_rects = []
    bulletsX = []
    bulletsY = []
    bulletsX_change = []
    bulletsY_change = []
    bullet_on_screen = []
    num_bullets = 0
    resetZombies()
    setZombieCoordinates()
    updateRound()

def updateScore():
    global score, scoreText, score_multiplier
    score += (1 * score_multiplier)
    scoreText = font.render("Score: " + str(score), True, (255, 255, 255))

def updatePlayerLives(number):
    global livesText, player_lives
    player_lives += number
    livesText = font.render("Lives: " + str(player_lives), True, (255,255,255))

def createHeart(round):
    global heart_exists
    if round % 3 == 0:
        heart_exists = True
    else:
        heart_exists = False

    if heart_exists:
        x = random.randint(50, 900)
        y = random.randint(100, 750)

        heartX.append(x)
        heartY.append(y)
        heartImg_rect.append(heartImg.get_rect(topleft=(heartX[-1], heartY[-1])))


def heart():
    for heart in range(len(heartX)):
        heartImg_rect[heart].topleft = (heartX[heart], heartY[heart])
        screen.blit(heartImg, heartImg_rect[heart])

def createDouble(round):
    global double_exists

    if round % 5 == 0:
        double_exists = True
    else:
        double_exists = False

    if double_exists:
        x = random.randint(50, width - 100)
        y = random.randint(100, height - 50)

        doubleX.append(x)
        doubleY.append(y)
        doubleImg_rect.append(doubleImg.get_rect(topleft=(doubleX[-1], doubleY[-1])))

def double():
    for double_index in range(len(doubleX)):
        doubleImg_rect[double_index].topleft = (doubleX[double_index], doubleY[double_index])
        screen.blit(doubleImg, doubleImg_rect[double_index])

def doubleDuration(current_time):
    global double_time, score_multiplier, activated, double_timer_value
    if activated:
        if current_time - double_time < 5000:
            score_multiplier = 2
        else:
            score_multiplier = 1
            activated = False
            double_timer_value = 0

def updateTimer(time, max, tag, text, timer_value):
    if int(time) != timer_value:
        timer_value = int(time)
        number = max - timer_value
        text = font.render(tag + ": " + str(number), True, (255, 255, 255))

    return text, timer_value


def displayTimer(current, fixed_time, max, timer_activated, text, type, timer_value):
    if timer_activated:
        time = (current / 1000) - (fixed_time / 1000)
        timerX = 0
        timerY = 0
        tag = ""
        if type == "double":
            timerX = width - 300
            timerY = 50
            tag = "Double Points"
        elif type == "reload":
            timerX = width - 225
            timerY = 75
            tag = "Reloading"
        text, timer_value = updateTimer(time, max, tag, text, timer_value)
        if time < max:
            screen.blit(text, (timerX, timerY))


# change rates based on attachments
for attachment in range(len(attachments_selected)):
    if attachments_selected[attachment]:
        if attachment == 1:
            bullet_damage = 75
        elif attachment == 2:
            fire_rate = 0.5 # done
        elif attachment == 3:
            magazine_size = 15 # done
        else:
            reload_rate = 2 # done

mag = magazine_size
mag_text = font.render("Ammo: " + str(mag), True, (255, 255, 255))

def showMagCount(mag_text):
    screen.blit(mag_text, ((width / 2) - 100, height - 50))

def updateMag(mag_change):
    global mag_text, mag
    if mag_change == 1:
        mag -= 1
    else:
        mag = mag_change
    mag_text = font.render("Ammo: " + str(mag), True, (255, 255, 255))

reload_text = font.render("Reloading: " + str(reload_rate), True, (255, 255, 255))


# main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if mag > 0:
                        if num_bullets == 0:
                            createBullet(player_angle, rotated_playerImg_rectangle.center[0], rotated_playerImg_rectangle.center[1])
                            fire_time = pg.time.get_ticks()
                            num_bullets += 1
                            updateMag(1)
                        else:
                            if (current_time - fire_time) / 1000 >= fire_rate:
                                createBullet(player_angle, rotated_playerImg_rectangle.center[0], rotated_playerImg_rectangle.center[1])
                                fire_time = pg.time.get_ticks()
                                num_bullets += 1
                                updateMag(1)


    if player_lives > 0:

        # HANDLE ROUND CHANGE
        if zombie_count == 0:
            roundChange()
            createHeart(round)
            createDouble(round)

        # RELOAD
        if mag <= 0 and reload_time == 0:
            reload_time = pg.time.get_ticks()
            reload_activated = True

        if (current_time - reload_time) / 1000 >= reload_rate and reload_activated:
            updateMag(magazine_size)
            reload_time = 0
            reload_activated = False
            reload_timer_value = 0

        # PLAYER FOLLOWS MOUSE
        mouse_pos = pg.mouse.get_pos()

        # find x and y distance between player and mouse
        components = get_components(playerX, playerY, mouse_pos[0], mouse_pos[1])

        # determine player speed and direction
        player_angle = math.atan2(components[1], components[0])
        playerX_change = player_speed * math.cos(player_angle)
        playerY_change = player_speed * math.sin(player_angle)

        pm_distance = math.sqrt((components[0] ** 2) + (components[1] ** 2))

        # fix a bug where player would glitch when distance is small
        if pm_distance < 20:
            playerX_change = 0
            playerY_change = 0

        # PLAYER LOOKS AT MOUSE
        rotated_playerImg, rotated_playerImg_rectangle = rotate_player(playerImg, player_angle * (180 / math.pi) + 80)

        # UPDATE PLAYER LOCATION
        playerX += playerX_change
        playerY += playerY_change

        for hearts in range(len(heartX)):
            # COLLISION WITH HEART
            if heartImg_rect[hearts].colliderect(rotated_playerImg_rectangle):
                updatePlayerLives(1)
                heartY[hearts] = -400

        for doubles in range(len(doubleX)):
            if doubleImg_rect[doubles].colliderect(rotated_playerImg_rectangle):
                activated = True
                doubleX[doubles] = width + 200
                double_time = pg.time.get_ticks()

        # LOOP HANDLES ANYTHING PERTAINING TO THE ZOMBIES
        for zombie in range(len(zombie_alive)):

            if not zombie_alive[zombie]:
                continue
            # get x and y distance between zombies and player
            zombiesComponents = get_components(
                    zombiesX[zombie], zombiesY[zombie], playerX, playerY)
            
            # calculate distance between zombie and player
            zp_distance = math.sqrt((zombiesComponents[0] ** 2) + (zombiesComponents[1] ** 2))

            # determine speed and direction of zombie
            zombie_angle = math.atan2(zombiesComponents[1],  zombiesComponents[0])
            zombiesX_change[zombie] = zombies_speed * math.cos(zombie_angle)
            zombiesY_change[zombie] = zombies_speed * math.sin(zombie_angle)

            # update zombie position
            zombiesX[zombie] += zombiesX_change[zombie]
            zombiesY[zombie] += zombiesY_change[zombie]

            # check if zombie collides with player
            if zombieImg_rects[zombie].colliderect(rotated_playerImg_rectangle):
                if zombie_hit[zombie] == False:
                    rect1 = zombieImg_rects[zombie]
                    rect2 = rotated_playerImg_rectangle
                    if abs(rect1.top - rect2.bottom) < coll_space or abs(rect1.bottom - rect2.top) < coll_space or abs(rect1.left - rect2.right) < coll_space or abs(rect1.right - rect2.left) < coll_space:
                        updatePlayerLives(-1)
                        zombie_hit[zombie] = True
            else:
                zombie_hit[zombie] = False

            # collision between zombie and zombie
            for collZombie in range(zombie_count):
                if collZombie == zombie:
                    continue
                if zombieImg_rects[zombie].colliderect(zombieImg_rects[collZombie]):
                    if abs(zombieImg_rects[zombie].top - zombieImg_rects[collZombie].bottom) < coll_space:
                        zombiesY[zombie] += 1
                    if abs(zombieImg_rects[zombie].bottom - zombieImg_rects[collZombie].top) < coll_space:
                        zombiesY[zombie] -= 1
                    if abs(zombieImg_rects[zombie].right - zombieImg_rects[collZombie].left) < coll_space:
                        zombiesX[zombie] -= 1
                    if abs(zombieImg_rects[zombie].left - zombieImg_rects[collZombie].right) < coll_space:
                        zombiesX[zombie] += 1

            # Collision between zombie and bullet
            for bulletColl in range(num_bullets):
                if not bullet_on_screen[bulletColl]:
                    continue
                if bulletImg_rects[bulletColl].colliderect(zombieImg_rects[zombie]) and not zombie_hit_bullet[zombie]:
                    zombies_health[zombie] -= bullet_damage
                    zombie_hit_bullet[zombie] = True
                    if zombies_health[zombie] <= 0:
                        removeZombie(zombie)
                        updateScore()
                elif zombie_hit_bullet[zombie] and not bulletImg_rects[bulletColl].colliderect(zombieImg_rects[zombie]):
                    zombie_hit_bullet[zombie] = False

        for bullet in range(num_bullets):
            if not bullet_on_screen[bullet]:
                continue
            bulletsX[bullet] += bulletsX_change[bullet]
            bulletsY[bullet] += bulletsY_change[bullet]

            if bulletsX[bullet] < -100 or bulletsX[bullet] > width + 100 or bulletsY[bullet] < -100 or bulletsY[bullet] > height + 100:
                removeBullet(bullet)

    else:
        displayText = True
        final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        playerX = width + 300
        playerX_change = 0
        playerY_change = 0
        for removeZ in range(len(zombie_alive)):
            zombiesX[removeZ] = -300
            zombiesX_change[removeZ] = 0
            zombiesY_change[removeZ] = 0

        for removeB in range(num_bullets):
            bulletsY[removeB] = -300
            bulletsX_change[removeB] = 0
            bulletsY_change[removeB] = 0

    current_time = pg.time.get_ticks()

    player(rotated_playerImg, rotated_playerImg_rectangle, playerX, playerY)
    zombies(zombieImgs, playerX)
    bullets(num_bullets)
    showScore(scoreText)
    showRound(roundText)
    showLives(livesText)
    showGameOver(displayText, final_score_text)
    heart()
    double()
    doubleDuration(current_time)
    displayTimer(current_time, double_time, 5, activated, double_text, "double", double_timer_value)
    displayTimer(current_time, reload_time, reload_rate, reload_activated, reload_text, "reload", reload_timer_value)
    showMagCount(mag_text)
    pg.display.update()
    clock.tick(60)
