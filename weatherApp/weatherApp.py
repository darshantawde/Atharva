import pygame, requests, random

pygame.init()
page = 'weather'
running = True


def fonts():
    global FONT, f
    try:
        FONT = 'C:\Windows\Fonts\JetBrainsMono-Medium.ttf'
        f = pygame.font.Font(FONT, 32)
    except:
        FONT = 'calibri.ttf'
        f = pygame.font.Font(FONT, 32)

pygame.display.set_caption("Weather Checker")

fonts()

while running:
    if page == 'weather': 
        done = False
        lights = [(234, 32, 39), (163, 203, 56), (27, 20, 100), (87, 88, 187), (111, 30, 81)]
        darks = [(238, 90, 36), (0, 148, 50), (6, 82, 221), (153, 128, 250), (131, 52, 113)]
        bgs = [(247, 159, 31), (0, 98, 102), (18, 137, 167), (217, 128, 250), (181, 52, 113)]
        x = random.randint(0, len(lights) - 1)
        light = lights[x]
        dark = darks[x]
        bg = bgs[x]

        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(200, 334 - 25, 600, 50)
        color_inactive = light
        color_active = dark
        color = color_inactive
        active = True
        city = ''
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:

                            try:
                                query = 'q=' + city
                                response = requests.get(
                                    'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
                                w_data = response.json()
                                temperature = str(round(float(w_data['main']['temp'] * 1.8 + 32), 2))
                                wind = w_data['wind']['speed']
                                description = w_data['weather'][0]['description']
                                weather = w_data['weather'][0]['main']
                                country = w_data['sys']['country']
                                txt_surface = font2.render('Searching...', True, (255, 255, 255))
                                textRect = txt_surface.get_rect()
                                textRect.center = (500, 664 - 85)
                                screen.blit(txt_surface, textRect)
                                pygame.display.update()
                                pygame.time.wait(1000)
                                done = True
                                page = 'display'

                            except:
                                txt_surface = font2.render('Invalid Location Entered', True, (255, 255, 255))
                                textRect = txt_surface.get_rect()
                                textRect.center = (500, 664 - 85)
                                screen.blit(txt_surface, textRect)
                                pygame.display.update()
                                pygame.time.wait(1000)
                                done = True
                                page = 'weather'
                                continue

                            city = list(city)
                            city[0] = city[0].upper()
                            city = ''.join(city)

                        elif event.key == pygame.K_BACKSPACE:
                            city = city[:-1]
                        else:
                            city += event.unicode

            screen.fill(bg)

            txt_surface = font.render('Weather Searcher', True, light)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Enter City Name', True, light)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85 + 40)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press ENTER to View Weather!', True, light)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 664 - 45)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(city, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'display':
        done = False
        lights = [(234, 32, 39), (163, 203, 56), (27, 20, 100), (87, 88, 187), (111, 30, 81)]
        darks = [(238, 90, 36), (0, 148, 50), (6, 82, 221), (153, 128, 250), (131, 52, 113)]
        bgs = [(247, 159, 31), (0, 98, 102), (18, 137, 167), (217, 128, 250), (181, 52, 113)]
        x = random.randint(0, len(lights) - 1)
        light = lights[x]
        dark = darks[x]
        bg = bgs[x]
        
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        color_inactive = light
        color_active = dark
        color = color_inactive
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'weather'
                        continue

            screen.fill(bg)

            txt_surface = font.render("%s's Weather" % city, True, light)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render("Temperature: %s°F" % temperature, True, (255, 255, 255))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334 - 80)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render("Wind speed: %s m/s" % wind, True, (255, 255, 255))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334 - 40)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render("Description: %s" % description, True, (255, 255, 255))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render("Weather: %s" % weather, True, (255, 255, 255))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334 + 40)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render("Country: %s" % country, True, (255, 255, 255))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334 + 80)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press ENTER to Search For Another City!', True, light)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 664 - 85)
            screen.blit(txt_surface, textRect)

            pygame.display.update()
