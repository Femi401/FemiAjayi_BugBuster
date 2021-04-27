import math
import random
import pygame
from pygame import mixer

pygame.init()

# width * height
screen = pygame.display.set_mode((800, 950))

pygame.display.set_caption("BUG BUSTER")
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

mixer.music.load('background.wav')
mixer.music.play(-1)

running = True
stage = 0

def show_beginner_button():

    button_font = pygame.font.Font(None, 24)
    button_rect = pygame.Rect((320, 400, 200, 60))
    text = button_font.render("Beginner", True, (204,0,102))
    text_rect = text.get_rect(center=button_rect.center)
    pygame.draw.rect(screen, (255,255,255), button_rect)
    screen.blit(text, text_rect)
    return button_rect


def show_expert_button():
    button_font = pygame.font.Font(None, 24)
    button_rect = pygame.Rect((320, 500, 200, 60))
    text = button_font.render("Intermediate", True, (204, 0, 102))
    text_rect = text.get_rect(center=button_rect.center)
    pygame.draw.rect(screen, (255, 255, 255), button_rect)
    screen.blit(text, text_rect)
    return button_rect


def show_game_name():
    button_font = pygame.font.Font(None, 100)
    text = button_font.render("BUG BUSTER", True, (204, 10, 102))
    screen.blit(text, (190,230))


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # backgroung image
    screen.blit(background, (0, 0))
    beginner_rect = show_beginner_button()
    intermediate_rect = show_expert_button()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse = pygame.mouse.get_pos()
        if beginner_rect.collidepoint(mouse):
            stage = 1
            running = False
        elif intermediate_rect.collidepoint(mouse):
            stage = 2
            running = False
    show_game_name()
    pygame.display.update()


# width * height
screen = pygame.display.set_mode((800, 950))

pygame.display.set_caption("BUG BUSTER")
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)
background = pygame.image.load('ActualBack.png')

mixer.music.load('background.wav')
mixer.music.play(-1)

kills = 0
font = pygame.font.Font('freesansbold.ttf', 18)
textX = 10
textY = 10

# flag score
yellow_flag_score = 0
yellow_flags = pygame.font.Font('freesansbold.ttf', 18)
yellowFlagX = 650
yellowFlagY = 10

levelkills = 0
levelkillsFont = pygame.font.Font('freesansbold.ttf', 18)
levelkillsX = 10
levelkillsY = 410

# flag score
levels_yellow_flag_score = 0
levels_yellow_flags = pygame.font.Font('freesansbold.ttf', 18)
levelsyellowFlagX = 650
levelsyellowFlagY = 410

levels_font = pygame.font.Font('freesansbold.ttf', 18)
levelsX = 380
levelsY = 410

playermg = pygame.image.load('player.png')
playerX = 370
playerY = 880
playerXchange = 3
playerYchange = 3

num_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(400, 550))
    enemyXchange.append(3)
    enemyYchange.append(40)

# ready and Fire state
BulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletYchange = -7
bullet_state = 'ready'

# yellow flag
yellow_flag_img = pygame.image.load('yellow-flag.png')
yellowX = random.randint(0, 736)
yellowY = random.randint(400, 880)

# Number of levels + for loop
number_of_levels = 3
normal_for_loop = pygame.font.Font('freesansbold.ttf', 24)

if stage == 1:
    number_of_levels = 4
    normal_for_loop = pygame.font.Font('freesansbold.ttf', 24)
elif stage == 2:
    number_of_levels = 5
    normal_for_loop = pygame.font.Font('freesansbold.ttf', 20)

game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score():
    score = font.render("Total Kills :" + str(kills), True, (255, 0, 0))
    screen.blit(score, (textX, textY))

def show_timer(time):
    score = font.render("Time : " + str(time), True, (255, 0, 0))
    screen.blit(score, (380, textY))

def show_yellow_flag_score():
    yellow_score = yellow_flags.render("Total Flags :" + str(yellow_flag_score), True, (255, 0, 0))
    screen.blit(yellow_score, (yellowFlagX, yellowFlagY))


def show_level_score():
    score = levelkillsFont.render("Level Kills :" + str(levelkills), True, (255, 0, 0))
    screen.blit(score, (levelkillsX, levelkillsY))


def show_level_yellow_flag_score():
    levelFlagScore = levels_yellow_flags.render("Level Flags :" + str(levels_yellow_flag_score), True, (255, 0, 0))
    screen.blit(levelFlagScore, (levelsyellowFlagX, levelsyellowFlagY))


def show_level(level):
    levels = levels_font.render("Level :" + str(level), True, (255, 0, 0))
    screen.blit(levels, (levelsX, levelsY))


def game_over(input_text):
    for j in range(num_of_enemies):
        enemyY[j] = 2000
    over_text = game_over_font.render(input_text, True, (255, 255, 255))
    close_text = normal_for_loop.render("Please close the game and run again", True, (255, 255, 255))
    screen.blit(over_text, (200, 450))
    screen.blit(close_text, (200, 550))


def show_next_level(level):
    level = game_over_font.render("LEVEL " + str(level), True, (255, 255, 255))
    screen.blit(level, (220, 450))


def for_loop_text_stage1(level):
    color = []
    for i in range(number_of_levels):
        if level == (i + 1):
            color.append((255, 255, 255))
        else:
            color.append((255, 255, 255))

    for_text = normal_for_loop.render("for (", True, (255, 255, 255))
    initialization_text = normal_for_loop.render("int level =1 ;", True, (255, 255, 255))
    condition_text = normal_for_loop.render("level <= 3 ;", True, (255, 255, 255))
    increment_text = normal_for_loop.render("level = level +1 ) {", True, (255, 255, 255))
    level1_text = normal_for_loop.render("Kill (level * 3) Aliens", True, color[0])
    level2_text = normal_for_loop.render("Collect (level * 2) flags", True, color[1])
    level3_text = normal_for_loop.render("}", True, color[2])
    close_text = normal_for_loop.render("No Kill and No Flag for 10 seconds", True, (255, 255, 255))

    screen.blit(for_text, (150, 100))
    screen.blit(initialization_text, (200, 100))
    screen.blit(condition_text, (350, 100))
    screen.blit(increment_text, (480, 100))
    screen.blit(level1_text, (200, 150))
    screen.blit(level2_text, (200, 200))
    screen.blit(level3_text, (200, 250))
    screen.blit(close_text, (200, 300))

def for_loop_text_stage2(level):
    color = []
    for i in range(number_of_levels):
        if level == (i + 1):
            color.append((255, 255, 255))
        else:
            color.append((255, 255, 255))

    for_text = normal_for_loop.render("for (", True, (255, 255, 255))
    initialization_text = normal_for_loop.render("int level =1 ;", True, (255, 255, 255))
    condition_text = normal_for_loop.render("level <= 4 ;", True, (255, 255, 255))
    increment_text = normal_for_loop.render("level = level +1 ) {", True, (255, 255, 255))
    even_levels = normal_for_loop.render("if(level % 2 == 0) {", True, color[0])
    level2_text = normal_for_loop.render("if(level <= 2) Kill (level * 2) Aliens", True, color[1])
    level4_text = normal_for_loop.render("else Collect (level * 2) Flags", True, color[1])
    odd_levels = normal_for_loop.render("} else {", True, color[2])
    level1_text = normal_for_loop.render("if(level <= 2) Collect (level * 2) flags", True, color[1])
    level3_text = normal_for_loop.render("else kill (level * 2) Aliens", True, color[1])
    end_loop = normal_for_loop.render("} }", True, color[1])
    ifTime = normal_for_loop.render("if(Time <= 80 seconds) Kill 3 Aliens", True, color[1])
    elseTime = normal_for_loop.render("else Collect 3 flags", True, (255, 255, 255))

    screen.blit(for_text, (150, 40))
    screen.blit(initialization_text, (200, 40))
    screen.blit(condition_text, (350, 40))
    screen.blit(increment_text, (480, 40))
    screen.blit(even_levels, (180, 70))
    screen.blit(level2_text, (210, 100))
    screen.blit(level4_text, (210, 130))
    screen.blit(odd_levels, (180, 160))
    screen.blit(level1_text, (210, 190))
    screen.blit(level3_text, (210, 220))
    screen.blit(end_loop, (150, 250))
    screen.blit(ifTime, (150, 280))
    screen.blit(elseTime, (150, 310))


def yellowflag(x, y):
    screen.blit(yellow_flag_img, (x, y))


def player(x, y):
    screen.blit(playermg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(BulletImg, (x + 15, y))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 40:
        return True
    return False


running = True
left_pressed = False
right_pressed = False
upper_pressed = False
down_pressed = False
game_over_bool = False
game_comp = False


def isLevelCompleted_stage1(levels_yellow_flag_score, levelkills, seconds, level):
    result = ()
    if (level == 1):
        if levelkills == 3 and levels_yellow_flag_score == 2:
            result = (True, False)
        elif levelkills > 3 or levels_yellow_flag_score > 2:
            result = (False, True)
        else:
            result = (False, False)
    elif (level == 2):
        if levelkills == 6 and levels_yellow_flag_score == 4:
            result = (True, False)
        elif levelkills > 6 or levels_yellow_flag_score > 4:
            result = (False, True)
        else:
            result = (False, False)
    elif (level == 3):
        if levelkills == 9 and levels_yellow_flag_score == 6:
            result = (True, False)
        elif levelkills > 9 or levels_yellow_flag_score > 6:
            result = (False, True)
        else:
            result = (False, False)
    elif (level == 4):
        if seconds >= 10 and levelkills == 0 and levels_yellow_flag_score == 0:
            result = (True, False)
        elif levelkills > 0 or levels_yellow_flag_score > 0:
            result = (False, True)
        else:
            result = (False, False)
    return result

def isLevelCompleted_stage2(levels_yellow_flag_score, levelkills, inTimeLevel5, level):
    result = ()
    if(level == 1):
        if levelkills == 0 and levels_yellow_flag_score == 2:
            result = (True, False)
        elif levelkills == 0 and levels_yellow_flag_score < 2:
            result = (False, False)
        else:
            result = (False, True)
    elif(level == 2):
        if levelkills == 4 and levels_yellow_flag_score == 0:
            result = (True, False)
        elif levelkills < 4 and levels_yellow_flag_score == 0:
            result = (False, False)
        else:
            result = (False, True)
    elif (level == 3):
        if levelkills == 6 and levels_yellow_flag_score == 0:
            result = (True, False)
        elif levelkills < 6 and levels_yellow_flag_score == 0:
            result = (False, False)
        else:
            result = (False, True)
    elif (level == 4):
        if levelkills == 0 and levels_yellow_flag_score == 8:
            result = (True, False)
        elif levelkills == 0 and levels_yellow_flag_score < 8:
            result = (False, False)
        else:
            result = (False, True)
    elif (level == 5):
        if inTimeLevel5 and levelkills == 3:
            result = (True, False)
        elif inTimeLevel5 and levelkills < 3:
            result = (False, False)
        elif not inTimeLevel5 and levels_yellow_flag_score == 3:
            result = (True, False)
        elif not inTimeLevel5 and levels_yellow_flag_score < 3:
            result = (False, False)
        else:
            result = (False, True)
    return result

def resetForNextLevel(level):
    for j in range(num_of_enemies):
        enemyY[j] = 2000

    global playerX
    playerX = 370
    global playerY
    playerY = 880
    global playerXchange
    playerXchange = level * 2
    global playerYchange
    playerYchange = level * 2.5
    global bulletYchange
    bulletYchange = level * -5

    show_next_level(level)
    pygame.display.update()
    pygame.time.delay(2000)

    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(400, 550)
        enemyXchange[i] = level * 1.5
        enemyYchange[i] = 40

    pygame.display.update()

start_time = pygame.time.get_ticks()
inTimeLevel5 = False

for level in range(1, number_of_levels+1):

    levelkills = 0
    levels_yellow_flag_score = 0
    if stage == 2 and level == number_of_levels:
        counting_time = pygame.time.get_ticks() - start_time
        counting_seconds = int(counting_time / 1000)
        if counting_seconds < 80:
            inTimeLevel5 = True
    elif stage == 1 and level ==  number_of_levels:
        start_time = pygame.time.get_ticks()

    while running:
        screen.fill((0, 0, 0))

        # backgroung image
        screen.blit(background, (0, 400))
        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = int(counting_time / 60000)
        counting_seconds = int(counting_time / 1000)
        counting_string = "%s" % (counting_seconds)
        show_timer(counting_string)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                if event.key == pygame.K_RIGHT:
                    right_pressed = True
                if event.key == pygame.K_UP:
                    upper_pressed = True
                if event.key == pygame.K_DOWN:
                    down_pressed = True
                if event.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                if event.key == pygame.K_RIGHT:
                    right_pressed = False
                if event.key == pygame.K_UP:
                    upper_pressed = False
                if event.key == pygame.K_DOWN:
                    down_pressed = False

        if left_pressed:
            playerX -= playerXchange
        elif right_pressed:
            playerX += playerXchange
        elif upper_pressed:
            playerY -= playerYchange
        elif down_pressed:
            playerY += playerYchange

        if playerX > 736:
            playerX = 736
        elif playerX < 5:
            playerX = 5
        if playerY > 880:
            playerY = 880
        elif playerY < 400:
            playerY = 400

        # enemy
        for i in range(num_of_enemies):
            enemyX[i] += enemyXchange[i]
            if enemyX[i] > 736:
                enemyX[i] = 736
                enemyXchange[i] = -enemyXchange[i]
                enemyY[i] += enemyYchange[i]
            elif enemyX[i] < 5:
                enemyX[i] = 5
                enemyXchange[i] = -enemyXchange[i]
                enemyY[i] += enemyYchange[i]
            if enemyY[i] > 880 and enemyY[i] < 1000:
                enemyY[i] = 880
                enemyYchange[i] = -enemyYchange[i]
            elif enemyY[i] < 400:
                enemyY[i] = 400
                enemyYchange[i] = -enemyYchange[i]

            if bullet_state is 'fire' and collision(enemyX[i], enemyY[i], bulletX, bulletY):
                bullet_state = 'ready'
                bulletY = playerY
                bulletX = playerX
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
                levelkills += 1
                kills += 1
                res = ()
                if stage == 1:
                    res = isLevelCompleted_stage1(levels_yellow_flag_score, levelkills, counting_seconds, level)
                elif stage ==2:
                    res = isLevelCompleted_stage2(levels_yellow_flag_score, levelkills, counting_seconds, level)
                game_over_bool = res[1]
                isLevComplete = res[0]
                if isLevComplete and level == number_of_levels:
                    game_comp = True
                elif isLevComplete:
                    resetForNextLevel(level + 1)
                    break
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(400, 550)

            # If enemy touches player Game over
            if collision(enemyX[i], enemyY[i], playerX, playerY):
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
                game_over_bool = True

            enemy(enemyX[i], enemyY[i], i)
            if game_over_bool:
                break

        if bulletY < 400:
            bullet_state = 'ready'
        if bullet_state is 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY += bulletYchange

        if collision(playerX, playerY, yellowX, yellowY):
            levels_yellow_flag_score += 1
            yellow_flag_score += 1
            res = ()
            if stage == 1:
                res = isLevelCompleted_stage1(levels_yellow_flag_score, levelkills, counting_seconds, level)
            elif stage == 2:
                res = isLevelCompleted_stage2(levels_yellow_flag_score, levelkills, counting_seconds, level)
            if not game_over_bool:
                game_over_bool = res[1]
            isLevComplete = res[0]
            if isLevComplete and level == number_of_levels:
                game_comp = True
            elif isLevComplete:
                resetForNextLevel(level + 1)
                break
            yellowX = random.randint(0, 736)
            yellowY = random.randint(400, 880)

        res = ()
        if stage == 1:
            res = isLevelCompleted_stage1(levels_yellow_flag_score, levelkills, counting_seconds, level)
        elif stage == 2:
            res = isLevelCompleted_stage2(levels_yellow_flag_score, levelkills, counting_seconds, level)
        if not game_over_bool:
            game_over_bool = res[1]
        isLevComplete = res[0]
        if isLevComplete and level == number_of_levels:
            game_comp = True
        elif isLevComplete:
            resetForNextLevel(level + 1)
            break

        show_score()
        show_yellow_flag_score()
        show_level_score()
        show_level_yellow_flag_score()
        show_level(level)
        if stage == 1:
            for_loop_text_stage1(1)
        elif stage == 2:
            for_loop_text_stage2(1)
        yellowflag(yellowX, yellowY)
        player(playerX, playerY)
        if game_over_bool:
            game_over("GAME OVER")
        elif game_comp:
            game_over("CONGRATS")

        pygame.display.update()

