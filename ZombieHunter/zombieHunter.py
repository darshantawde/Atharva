import pygame
import random
import math
import json

pygame.init()
page = 1
fullGameRunning = True

try:
    FONT = 'C:\Windows\Fonts\JetBrainsMono-Medium.ttf'
    font = pygame.font.Font(FONT, 32)
except:
    FONT = 'C:\Windows\Fonts\calibrib.ttf'
    font = pygame.font.Font(FONT, 32)

#JSON Work

with open("score.json", "r") as f:
    scores = json.load(f)

while fullGameRunning:
    if page == 0:
        global text
        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 15)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(350, 304, 300, 60)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    fullGameRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 3
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    else:
                        if event.key == pygame.K_r:
                            done = True
                            page = 1

            screen.fill((30, 30, 30))
            
            txt_surface = font.render('Type your Display Name for the Leaderboards!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press Enter to enter the Game!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press R to return back to the Main Menu!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-110)
            screen.blit(txt_surface, textRect)
            
            txt_surface = font.render(text, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

    if page == 1:
        introScreen = pygame.display.set_mode((1000, 668))
        pygame.display.set_caption("The Zombie Hunter")
        icon = pygame.image.load('heart.png')
        pygame.display.set_icon(icon)
        b = pygame.image.load('grass2.png')

        introRunning = True

        while introRunning:
            introScreen.blit(b, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    introRunning = False
                    fullGameRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        introRunning = False
                        page = 0
                        continue
                    if event.key == pygame.K_r:
                        introRunning = False
                        page = 2
                    if event.key == pygame.K_q:
                        introRunning = False
                        page = 4

            introFont = pygame.font.Font(FONT, 30)
            msgBox = introFont.render("ZOMBIE HUNTER", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 85)
            introScreen.blit(msgBox, msgRect)

            introFontMed = pygame.font.Font(FONT, 20)
            msgBox = introFontMed.render("Press SPACEBAR to begin playing!", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-85)
            introScreen.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Press R to look at the Instructions!", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-110)
            introScreen.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Press Q to look at the Highest Score!", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-135)
            introScreen.blit(msgBox, msgRect)

            pygame.display.update()

    if page == 2:
        instrux = pygame.display.set_mode((1000, 668))
        pygame.display.set_caption("The Zombie Hunter")
        icon = pygame.image.load('heart.png')
        pygame.display.set_icon(icon)

        instruxRunning = True

        while instruxRunning:
            instrux.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        instruxRunning = False
                        fullGameRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        instruxRunning = False
                        page = 3
                    if event.key == pygame.K_r:
                        instruxRunning = False
                        introRunning = True
                        page = 1
                        continue

            introFont = pygame.font.Font(FONT, 30)
            introFontSm = pygame.font.Font(FONT, 13)
            introFontMed = pygame.font.Font(FONT, 20)

            msgBox = introFont.render("INSTRUCTIONS", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 85)
            instrux.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Controls", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 150)
            instrux.blit(msgBox, msgRect)
            
            msgBox = introFontSm.render("Space: Fire, Up and Down: Move Up and Down, Z: Buy Lives, X: Upgrade", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 170)
            instrux.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Objective", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 250)
            instrux.blit(msgBox, msgRect)
            
            msgBox = introFontSm.render("Destroy the Generator, and stop the Zombie Invasion!", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 270)
            instrux.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Press SPACEBAR to begin playing!", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-85)
            instrux.blit(msgBox, msgRect)

            msgBox = introFontMed.render("Press R to return to the Main Menu!", True, (255, 255, 0))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-110)
            instrux.blit(msgBox, msgRect)

            pygame.display.update()

    if page == 3:
        # Constants?
        number_of_zombies = 5
        number_of_baby_zombies = 4
        number_of_crawlers = 5
        number_of_wolves = 4
        number_of_ammoBoxes = 2
        bullets = 50
        killed = 0
        wallHealth = 300000
        generatorHealth = 7500
        score = 0
        lives = 10
        font = pygame.font.Font(FONT, 25)
        price_2x_upgrade = 250
        price_2x_speed = 350

        # COMIC BD
        running = True
        high = 85
        # Basics
        s = pygame.display.set_mode((1000, 668))
        pygame.display.set_caption("The Zombie Hunter")
        icon = pygame.image.load('heart.png')
        pygame.display.set_icon(icon)

        b = pygame.image.load('redGrass2.png')
        heart = pygame.image.load('heart.png')
        wall = pygame.image.load('brickWall2.png')
        star = pygame.image.load('score.png')
        ammo = pygame.image.load('ammo.png')
        kls = pygame.image.load('killed.png')
        wh = pygame.image.load('wallHealth.png')
        genMini = pygame.image.load('generatorMini.png')

        bullet_sound = pygame.mixer.Sound("laser.wav")
        bullet_hit_generator = pygame.mixer.Sound("hitGen.wav")

        pImg = pygame.image.load('man2.png')
        px = 75
        py = 668 / 2 - 112 / 2
        pxc = 0
        pyc = 0

        bImg = pygame.image.load('bullet2.png')
        bx = 165
        by = 285
        bxc = 20
        byc = 0
        bState = 'ready'

        zImg = []
        zx = []
        zy = []
        zxc = []
        zyc = []

        dImg = []
        dx = []
        dy = []
        dxc = []
        dyc = []

        cImg = []
        cx = []
        cy = []
        cxc = []
        cyc = []

        wImg = []
        wx = []
        wy = []
        wxc = []
        wyc = []

        aImg = []
        ax = []
        ay = []
        axc = []
        ayc = []

        generator = pygame.image.load('generatorMS.png')
        gx = 800
        gy = 225
        gxc = 2

        # Dead Graphics
        deadMan = pygame.image.load('deadMan2.png')
        deadGen = pygame.image.load('deadGenerator.png')

        for i in range(number_of_zombies):
            zImg.append(pygame.image.load('zwalk.png'))
            zx.append(1100)
            x = random.randint(1, 2)
            if x == 1:
                zy.append(random.randint(high, 127))
            else:
                zy.append(random.randint(481, 540))
            zxc.append(2)
            zyc.append(0)

        for i in range(number_of_crawlers):
            cImg.append(pygame.image.load('zcrawl.png'))
            cx.append(1100)
            x = random.randint(1, 2)
            if x == 1:
                cy.append(random.randint(high, 127))
            else:
                cy.append(random.randint(481, 540))
            cxc.append(3.5)
            cyc.append(0)

        for i in range(number_of_baby_zombies):
            dImg.append(pygame.image.load('znyert.png'))
            dx.append(1100)
            x = random.randint(1, 2)
            if x == 1:
                dy.append(random.randint(high, 127))
            else:
                dy.append(random.randint(481, 540))
            dxc.append(4.75)
            dyc.append(random.uniform(-2, 2))

        for i in range(number_of_wolves):
            wImg.append(pygame.image.load('wolf.png'))
            wx.append(1100)
            x = random.randint(1, 2)
            if x == 1:
                wy.append(random.randint(high, 127))
            else:
                wy.append(random.randint(481, 540))
            wxc.append(3.5)
            wyc.append(random.uniform(-1, 1))

        for i in range(number_of_ammoBoxes):
            aImg.append(pygame.image.load('ammoResupply.png'))
            ax.append(1100)
            x = random.randint(1, 2)
            if x == 1:
                ay.append(random.randint(high, 127))
            else:
                ay.append(random.randint(481, 540))
            axc.append(1)
            ayc.append(0)


        def player(x, y):
            if lives > 0:
                s.blit(pImg, (x, y))
            else:
                s.blit(deadMan, (x, y))


        def bullet(x, y):
            global bState
            bState = 'fire'
            s.blit(bImg, (x, y))


        def zombie(x, y, i):
            s.blit(zImg[i], (x, y))


        def baby_zombie(x, y, i):
            s.blit(dImg[i], (x, y))


        def wolf(x, y, i):
            s.blit(wImg[i], (x, y))


        def crawler(x, y, i):
            s.blit(cImg[i], (x, y))


        def ammobox(x, y, i):
            s.blit(aImg[i], (x, y))


        def gen(x, y):
            if generatorHealth > 0:
                s.blit(generator, (x, y))
            else:
                s.blit(deadGen, (x - 50, y))


        def is_z_bullet_collision(zux, zuy, bux, buy):
            distance = math.sqrt((math.pow(zux - bux, 2)) + (math.pow(zuy - buy, 2)))
            if distance < 65:
                return True
            else:
                return False


        def is_z_collision(zux, zuy, plx, ply):
            distance = math.sqrt((math.pow(zux - plx, 2)) + (math.pow(zuy - ply, 2)))
            if distance < 40:
                return True
            else:
                return False


        def is_c_bullet_collision(zux, zuy, bux, buy):
            distance = math.sqrt((math.pow(zux - bux, 2)) + (math.pow(zuy - buy, 2)))
            if distance < 65:
                return True
            else:
                return False


        def is_c_collision(zux, zuy, plx, ply):
            distance = math.sqrt((math.pow(zux - plx, 2)) + (math.pow(zuy - ply, 2)))
            if distance < 40:
                return True
            else:
                return False


        def is_b_bullet_collision(zux, zuy, bux, buy):
            distance = math.sqrt((math.pow(zux - bux, 2)) + (math.pow(zuy - buy, 2)))
            if distance < 65:
                return True
            else:
                return False


        def is_b_collision(zux, zuy, plx, ply):
            distance = math.sqrt((math.pow(zux - plx, 2)) + (math.pow(zuy - ply, 2)))
            if distance < 40:
                return True
            else:
                return False


        def is_w_bullet_collision(zux, zuy, bux, buy):
            distance = math.sqrt((math.pow(zux - bux, 2)) + (math.pow(zuy - buy, 2)))
            if distance < 65:
                return True
            else:
                return False


        def is_w_collision(zux, zuy, plx, ply):
            distance = math.sqrt((math.pow(zux - plx, 2)) + (math.pow(zuy - ply, 2)))
            if distance < 70:
                return True
            else:
                return False


        def is_a_collision(zux, zuy, plx, ply):
            distance = math.sqrt((math.pow(zux - plx, 2)) + (math.pow(zuy - ply, 2)))
            if distance < 40:
                return True
            else:
                return False


        def is_generator_collision(bux, buy, gux, guy):
            distance = math.sqrt((math.pow(bux - gux, 2)) + (math.pow(buy - guy, 2)))
            distance2 = math.sqrt((math.pow(bux - gux, 2)) + (math.pow(buy - (guy + 256), 2)))
            distance3 = math.sqrt((math.pow(bux - gux, 2)) + (math.pow(buy - (guy + 128), 2)))
            if (distance < 75) or (distance2 < 75) or (distance3 < 75):
                return True
            else:
                return False


        while running:
            s.blit(b, (0, 0))
            s.blit(wall, (15, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    fullGameRunning = False

                if lives > 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            pyc = -2
                        if event.key == pygame.K_DOWN:
                            pyc = 2
                        if event.key == pygame.K_SPACE:
                            if (bState is 'ready') and (bullets > 0):
                                by = py
                                bullet(bx, by)
                                bullets -= 1
                                if bullets <= 0:
                                    bullets = 0
                                pygame.mixer.Sound.play(bullet_sound)
                        if event.key == pygame.K_z:
                            if (score >= 50) and (lives > 0):
                                score -= 50
                                lives += 1
                        if event.key == pygame.K_x:
                            if (score >= int(price_2x_upgrade)) and (lives > 0):
                                score -= int(price_2x_upgrade)
                                bxc *= 2
                                price_2x_upgrade *= 1.5
                        if event.key == pygame.K_c:
                            if (score >= int(price_2x_speed)) and (lives > 0):
                                score -= int(price_2x_speed)
                                pyc *= 2
                                price_2x_speed *= 1.75
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                            pyc = 0
                
                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    if event.type == pygame.KEYDOWN:    
                        if event.key == pygame.K_r:

                            if text not in scores.keys():
                                iterator = []
                                
                                #for k in dict:
                                #    iterator.append(int(k))

                                #iteration = max(iterator)
                                #
                                #newEntry = {str(iteration): str(score)}

                                #scores[text].update(newEntry)

                                newEntry = {text : {"0": str(score)}}
                                scores.update(newEntry)
                            
                            elif text in scores.keys():
                                iterator = []
                                
                                names = list(scores.keys())
                                dicts = list(scores.values())
                                dict = dicts[names.index(text)]
                                
                                for k in dict:
                                    iterator.append(int(k))

                                iteration = max(iterator)

                                newEntry = {str(iteration + 1): str(score)}
                                
                                dict.update(newEntry)

                            with open('score.json', "w") as f:
                                json.dump(scores, f)

                            running = False
                            introRunning = True
                            page = 1
                            continue

            py += pyc
            player(px, py)

            if lives <= 0:
                lives = 0
                pyc = 0

            if py <= 0:
                py = 0
            elif py >= 540:
                py = 540

            for i in range(number_of_zombies):
                zx[i] -= zxc[i]
                if zx[i] <= 70:
                    wallHealth -= random.randint(50, 1000)
                    zx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        zy[i] = random.randint(high, 127)
                    else:
                        zy[i] = random.randint(481, 540)

                zombie_bullet_collision = is_z_bullet_collision(zx[i], zy[i], bx, by)
                if zombie_bullet_collision:
                    bx = 165
                    by = 1000000
                    bState = 'ready'
                    score += 1
                    zx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        zy[i] = random.randint(high, 127)
                    else:
                        zy[i] = random.randint(481, 540)
                    killed += 1

                zombie_collision = is_z_collision(zx[i], zy[i], px, py)
                if zombie_collision:
                    zx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        zy[i] = random.randint(high, 127)
                    else:
                        zy[i] = random.randint(481, 540)
                    lives -= 2

                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    zxc[i] = 0

                zombie(zx[i], zy[i], i)

            for i in range(number_of_crawlers):
                cx[i] -= cxc[i]
                if cx[i] <= 70:
                    wallHealth -= random.randint(50, 1000)
                    cx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        cy[i] = random.randint(high, 127)
                    else:
                        cy[i] = random.randint(481, 540)

                crawler_bullet_collision = is_c_bullet_collision(cx[i], cy[i], bx, by)
                if crawler_bullet_collision:
                    bx = 165
                    by = 1000000
                    bState = 'ready'
                    score += 5
                    cx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        cy[i] = random.randint(high, 127)
                    else:
                        cy[i] = random.randint(481, 540)
                    killed += 1

                crawler_collision = is_c_collision(cx[i], cy[i], px, py)
                if crawler_collision:
                    cx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        cy[i] = random.randint(high, 127)
                    else:
                        cy[i] = random.randint(481, 540)
                    lives -= 3

                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    cxc[i] = 0

                crawler(cx[i], cy[i], i)

            for i in range(number_of_baby_zombies):
                dx[i] -= dxc[i]
                dy[i] -= dyc[i]
                if dx[i] <= 70:
                    wallHealth -= random.randint(15, 300)
                    dx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        dy[i] = random.randint(high, 127)
                    else:
                        dy[i] = random.randint(481, 540)

                baby_zombie_bullet_collision = is_b_bullet_collision(dx[i], dy[i], bx, by)
                if baby_zombie_bullet_collision:
                    bx = 165
                    by = 1000000
                    bState = 'ready'
                    score += 2
                    dx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        dy[i] = random.randint(high, 127)
                    else:
                        dy[i] = random.randint(481, 540)
                    killed += 1

                baby_zombie_collision = is_b_collision(dx[i], dy[i], px, py)
                if baby_zombie_collision:
                    dx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        dy[i] = random.randint(high, 127)
                    else:
                        dy[i] = random.randint(481, 540)
                    lives -= 1

                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    dxc[i] = 0
                    dyc[i] = 0

                if (dy[i] <= high + 3) or (dy[i] >= 540):
                    dyc[i] *= -1

                baby_zombie(dx[i], dy[i], i)

            for i in range(number_of_wolves):
                wx[i] -= wxc[i]
                wy[i] += wyc[i]
                if wx[i] <= 70:
                    wallHealth -= random.randint(5, 450)
                    wx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        wy[i] = random.randint(high, 127)
                    else:
                        wy[i] = random.randint(481, 540)

                wolf_bullet_collision = is_w_bullet_collision(wx[i], wy[i], bx, by)
                if wolf_bullet_collision:
                    bx = 165
                    by = 1000000
                    bState = 'ready'
                    score += 7
                    wx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        wy[i] = random.randint(high, 127)
                    else:
                        wy[i] = random.randint(481, 540)
                    killed += 1

                wolf_collision = is_w_collision(wx[i], wy[i], px, py)
                if wolf_collision:
                    wx[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        wy[i] = random.randint(high, 127)
                    else:
                        wy[i] = random.randint(481, 540)
                    lives -= 2

                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    wxc[i] = 0
                    wyc[i] = 0

                if (wy[i] <= high) or (wy[i] >= 540):
                    wyc[i] *= -1

                wolf(wx[i], wy[i], i)

            for i in range(number_of_ammoBoxes):
                ax[i] -= axc[i]
                if ax[i] <= 70:
                    ax[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        ay[i] = random.randint(high, 127)
                    else:
                        ay[i] = random.randint(481, 540)

                ammobox_collision = is_a_collision(ax[i], ay[i], px, py)
                if ammobox_collision:
                    ax[i] = 1100
                    x = random.randint(1, 2)
                    if x == 1:
                        ay[i] = random.randint(high, 127)
                    else:
                        ay[i] = random.randint(481, 540)
                    bullets += random.randint(15, 105)

                if (lives <= 0) or (wallHealth <= 0) or (generatorHealth <= 0):
                    axc[i] = 0

                ammobox(ax[i], ay[i], i)

            if bx >= 1000:
                bx = 165
                bState = 'ready'

            if bState is 'fire':
                bullet(bx, by)
                bx += bxc

            if wallHealth <= 0:
                wallHealth = 0

            gen(gx, gy)
            gx += gxc

            generator_collision = is_generator_collision(bx, by, gx, gy)
            if generator_collision:
                bx = 165
                by = 1000000
                bState = 'ready'
                generatorHealth -= random.randint(50, 150)
                score += 15
                pygame.mixer.Sound.play(bullet_hit_generator)

            if (gx >= 803) or (gx <= 797):
                gxc *= -1

            scoreBox = font.render(' = ' + str(score), True, (255, 255, 255), 'bruh')
            scoreRect = scoreBox.get_rect()
            scoreRect.center = (900, 20)
            s.blit(star, (846, 5))
            s.blit(scoreBox, scoreRect)

            livesBox = font.render(' = ' + str(lives), True, (255, 255, 255), 'bruh')
            livesRect = scoreBox.get_rect()
            livesRect.center = (900, 60)
            s.blit(heart, (845, 45))
            s.blit(livesBox, livesRect)

            ammoBox = font.render(' = ' + str(bullets), True, (255, 255, 255), 'bruh')
            ammoRect = ammoBox.get_rect()
            ammoRect.center = (900, 100)
            s.blit(ammo, (847, 85))
            s.blit(ammoBox, ammoRect)

            killBox = font.render(' = ' + str(killed), True, (255, 255, 255), 'bruh')
            killRect = killBox.get_rect()
            killRect.center = (900, 140)
            s.blit(kls, (846, 125))
            s.blit(killBox, killRect)

            popBox = font.render(" = " + str(wallHealth), True, (255, 255, 255), 'bruh')
            popRect = popBox.get_rect()
            popRect.center = (900, 180)
            s.blit(wh, (819, 165))
            s.blit(popBox, popRect)

            genBox = font.render(str(generatorHealth), True, (19, 118, 158), 'bruh')
            genRect = genBox.get_rect()
            genRect.center = (920, 275)
            s.blit(genBox, genRect)

            msgBox = font.render('All you got to do is DESTROY THE GENERATOR!', True, (0, 0, 128),
                                 (255, 222, 18))
            msgRect = msgBox.get_rect()
            msgRect.center = (425, 20)
            s.blit(msgBox, msgRect)

            font2 = pygame.font.Font(FONT, 15)

            msgBox = font2.render("By the way, if you're running short on lives, try pressing Z!", True, (0, 0, 128),
                                  (255, 222, 18))
            msgRect = msgBox.get_rect()
            msgRect.center = (425, 45)
            s.blit(msgBox, msgRect)

            msgBox = font2.render(
                "Want faster bullets? Press X to buy 2x Speed Bullets for just " + str(int(price_2x_upgrade)) + " Score!", True,
                (0, 0, 128),
                (255, 222, 18))
            msgRect = msgBox.get_rect()
            msgRect.center = (425, 65)
            s.blit(msgBox, msgRect)

            msgBox = font2.render(
                "Want to travel faster yourself? Buy 2x Speed Boots for just " + str(int(price_2x_speed)) + " Score!", True,
                (0, 0, 128),
                (255, 222, 18))
            msgRect = msgBox.get_rect()
            msgRect.center = (425, 85)
            s.blit(msgBox, msgRect)

            if (lives <= 0) or (wallHealth <= 0):
                gameOver = font.render('GAME OVER! Press R to return back to the main menu!', True, (0, 0, 0), (250, 222, 18))
                goRect = gameOver.get_rect()
                goRect.center = (500, 334)
                s.blit(gameOver, goRect)
                gxc = 0
                bullets = 0

            if generatorHealth <= 0:
                generatorHealth = 0
                win = font.render('You destroyed the Generator!', True, (0, 0, 0), (250, 222, 18))
                winBox = win.get_rect()
                winBox.center = (500, 324)
                s.blit(win, winBox)

                win = font.render('Press R to return back to the main menu!', True, (0, 0, 0), (250, 222, 18))
                winBox = win.get_rect()
                winBox.center = (500, 354)
                s.blit(win, winBox)

                gxc = 0
                bullets = 0

                # Joe backs away from the destruction, as his objective is complete.
                pxc = 1
                px -= pxc

            pygame.display.update()

        pygame.display.update()

    if page == 4:
        leaderboard = pygame.display.set_mode((1000, 668))
        pygame.display.set_caption("The Zombie Hunter")
        icon = pygame.image.load('heart.png')
        pygame.display.set_icon(icon)

        boardRunning = True

        while boardRunning:
            leaderboard.blit(b, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    boardRunning = False
                    fullGameRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        boardRunning = False
                        introRunning = True
                        page = 1
    
            introFont = pygame.font.Font(FONT, 30)
            msgBox = introFont.render("High Scores", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 85)
            leaderboard.blit(msgBox, msgRect)

            scorelist = []
            keylist = []
            klist = []
            kvlist = []
            
            for key, dict in scores.items():
                keylist.append(key)
                for k, v in dict.items():
                    klist.append(int(k))
                    scorelist.append(int(v))
                    index = k + v
                    kvlist.append(index)
            
            print(keylist)
            print(scorelist)
            highscore = max(scorelist)
            print(highscore)
            
            findk = klist[scorelist.index(highscore)]
            print(findk)
            
            print(kvlist)
            findK = keylist[kvlist.index(str(findk) + str(highscore)) - 1]
            print(findK, highscore)

            for i in range(5):
                print(i)

            bigfont = pygame.font.Font(FONT, 32)
            msgBox = bigfont.render(nuchain[0], True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 200)
            leaderboard.blit(msgBox, msgRect)

            bigfont = pygame.font.Font(FONT, 32)
            msgBox = bigfont.render(nuchain[1], True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 250)
            leaderboard.blit(msgBox, msgRect)

            bigfont = pygame.font.Font(FONT, 32)
            msgBox = bigfont.render(nuchain[2], True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 300)
            leaderboard.blit(msgBox, msgRect)

            bigfont = pygame.font.Font(FONT, 32)
            msgBox = bigfont.render(nuchain[3], True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 350)
            leaderboard.blit(msgBox, msgRect)

            bigfont = pygame.font.Font(FONT, 32)
            msgBox = bigfont.render(nuchain[4], True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 400)
            leaderboard.blit(msgBox, msgRect)

            introFontMed = pygame.font.Font(FONT, 20)
            msgBox = introFontMed.render("Press R to return back to the Main Menu!", True, (0, 0, 128))
            msgRect = msgBox.get_rect()
            msgRect.center = (500, 668-85)
            leaderboard.blit(msgBox, msgRect)

            pygame.display.update()

# Lol, ik whatchur thinking, game code 2 long ;{