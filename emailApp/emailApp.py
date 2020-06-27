import pygame, smtplib, imapclient

page = 'username'
apprunning = True
pygame.init()
pygame.display.set_caption("The Greatest Gmail Application")

def FontSelector():
    global FONT, f
    try:
        FONT = 'C:\Windows\Fonts\JetBrainsMono-Medium.ttf'
        f = pygame.font.Font(FONT, 32)
    except:
        FONT = 'calibri.ttf'
        f = pygame.font.Font(FONT, 32)

FontSelector()

while apprunning:
    if page == 'username':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(200, 334-25, 600, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        username = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'password'
                        elif event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Enter Email', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Log in Using GMAIL', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 140)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(username, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'password':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(200, 334-25, 600, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        password = ''
        passwordCover = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if '@' not in username:
                                username += '@gmail.com'

                            conn = smtplib.SMTP('smtp.gmail.com', 587)
                            conn.ehlo()
                            conn.starttls()

                            try:
                                conn.login(username, password)
                                done = False
                                txt_surface = font2.render('Logging In...', True, (255, 255, 255))
                                textRect = txt_surface.get_rect()
                                textRect.center = (500, 668-85)
                                screen.blit(txt_surface, textRect)
                                pygame.display.update()
                                pygame.time.wait(1000)
                                done = True
                                page = 'sendto'

                            except:
                                done = False
                                txt_surface = font2.render('Invalid Username or Password', True, (255, 255, 255))
                                textRect = txt_surface.get_rect()
                                textRect.center = (500, 668-85)
                                screen.blit(txt_surface, textRect)
                                password = ''
                                passwordCover = ''
                                pygame.display.update()
                                pygame.time.wait(1000)
                                continue
                                                            
                        elif event.key == pygame.K_BACKSPACE:
                            password = password[:-1]
                            passwordCover = passwordCover[:-1]

                        elif event.key != pygame.K_LSHIFT:
                            password += event.unicode
                            passwordCover += '*'
                            
            screen.fill((30, 30, 30))

            txt_surface = font.render('Enter Password', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(passwordCover, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'sendto':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(200, 334-25, 600, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        recipient = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'confirmation'
                            if '@' not in recipient:
                                recipient += '@gmail.com'
                        elif event.key == pygame.K_BACKSPACE:
                            recipient = recipient[:-1]
                        else:
                            recipient += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Enter Recipient', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(recipient, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()
    
    if page == 'confirmation':
        pygame.init()
        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'subject'
                    if event.key == pygame.K_r:
                        done = True
                        page = 'username'
                        continue
                    if event.key == pygame.K_q:
                        done = True
                        page = 'inbox'

            screen.fill((30, 30, 30))

            txt_surface = font.render('Email Information', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Logged in as: ' + username, True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 309)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Sending Email To: ' + recipient, True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 359)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press R to re-enter all information', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press ENTER to proceed to message writing', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-110)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press Q to proceed to checking inbox', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-135)
            screen.blit(txt_surface, textRect)

            pygame.display.update()

    if page == 'subject':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(200, 334-25, 600, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        subject = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'lineone'
                        elif event.key == pygame.K_BACKSPACE:
                            subject = subject[:-1]
                        else:
                            subject += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Subject', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(subject, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)
                    
            pygame.display.update()

    if page == 'lineone':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(50, 334-25, 900, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        lineone = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'linetwo'
                        elif event.key == pygame.K_BACKSPACE:
                            lineone = lineone[:-1]
                        else:
                            lineone += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Line One', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(lineone, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'linetwo':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(50, 334-25, 900, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        linetwo = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'name'
                        elif event.key == pygame.K_BACKSPACE:
                            linetwo = linetwo[:-1]
                        else:
                            linetwo += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Line Two', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(linetwo, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'name':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(100, 334-25, 800, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        name = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            page = 'send'
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            name += event.unicode

            screen.fill((30, 30, 30))

            txt_surface = font.render('Name', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render(name, True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(15)

            pygame.display.update()

    if page == 'send':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        send = pygame.Rect(200, 334-25, 600, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if send.collidepoint(event.pos):
                        active = True
                    else:
                        active = False  
                    color = color_active if active else color_inactive
                if active:
                    try:
                        conn.sendmail(username, recipient, 'Subject:%s\n%s\n%s\n-%s' % (subject, lineone, linetwo, name))            
                        done = True
                        page = 'sent'
                    except:
                        done = True
                        page = 'fail'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        done = True
                        page = 'username'
                        continue
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'sendto'
                        continue

            screen.fill((30, 30, 30))

            txt_surface = font.render('Confirm Send', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press R to LOG OUT', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-85)
            screen.blit(txt_surface, textRect)

            txt_surface = font2.render('Press ENTER to SEND A NEW EMAIL', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 668-110)
            screen.blit(txt_surface, textRect)

            txt_surface = font.render('CLICK TO SEND', True, color)
            textRect = txt_surface.get_rect()
            textRect.center = (500, 334)
            screen.blit(txt_surface, textRect)
            pygame.draw.rect(screen, color, send, 2)
            pygame.display.flip()      

            pygame.display.update()

    if page == 'sent':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        send = pygame.Rect(300, 334-25, 400, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        name = ''
        success = False
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'sendto'
                        continue
                    if event.key == pygame.K_r:
                        done = True
                        page = 'username'
                        continue


            screen.fill((30, 30, 30))
   
            txt_surface = font.render('EMAIL SENT!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 344)
            screen.blit(txt_surface, textRect)
            txt_surface = font2.render('Press R to LOG OUT or ENTER to SEND A NEW EMAIL!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 390)
            screen.blit(txt_surface, textRect)
                
            pygame.display.update()

    if page == 'fail':
        pygame.init()

        screen = pygame.display.set_mode((1000, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        clock = pygame.time.Clock()
        send = pygame.Rect(300, 334-25, 400, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'sendto'
                        continue
                    if event.key == pygame.K_r:
                        done = True
                        page = 'username'
                        continue

            screen.fill((30, 30, 30))
            
            txt_surface = font.render('FAILED TO SEND EMAIL!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 344)
            screen.blit(txt_surface, textRect)
            txt_surface = font2.render('Press R to LOG OUT or ENTER to SEND A NEW EMAIL!', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (500, 390)
            screen.blit(txt_surface, textRect)
   
            pygame.display.update()

    if page == 'inbox':
        pygame.init()
        conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        conn.login(username, password)
        screen = pygame.display.set_mode((1500, 668))
        font = pygame.font.Font(FONT, 32)
        font2 = pygame.font.Font(FONT, 20)
        font3 = pygame.font.Font(FONT, 13)
        clock = pygame.time.Clock()
        send = pygame.Rect(300, 334-25, 400, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = True
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    apprunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        page = 'sendto'
                        continue
                    if event.key == pygame.K_r:
                        done = True
                        page = 'confirmation'
                        continue

            screen.fill((30, 30, 30))

            conn.select_folder('INBOX', readonly=True)
            messages = conn.search(['FROM', recipient])
            messages = messages[::-1]
            
            if len(messages) == 1:
                txt_surface = font2.render('%d message from %s' % (len(messages), recipient), True, pygame.Color('lightskyblue3'))
                textRect = txt_surface.get_rect()
                textRect.center = (750, 65)
                screen.blit(txt_surface, textRect)
            else:
                txt_surface = font2.render('%d messages from %s' % (len(messages), recipient), True, pygame.Color('lightskyblue3'))
                textRect = txt_surface.get_rect()
                textRect.center = (750, 65)
                screen.blit(txt_surface, textRect)
            
            if len(messages) > 0:
                i = 0
                envelopes = []
                for id, data in conn.fetch(messages, ['ENVELOPE']).items():
                    envelope = data[b'ENVELOPE']
                    envelopes.append(envelope)
                
                envelopes = envelopes[::-1]

                if len(envelopes) > 25:
                    txt_surface = font2.render('+%d More' % (len(messages) - 25), True, pygame.Color('lightskyblue3'))
                    textRect = txt_surface.get_rect()
                    textRect.center = (750, 668-70)
                    screen.blit(txt_surface, textRect)
                    for j in range(25):                        
                        try: 
                            envelope = envelopes[j]
                            subject = envelope.subject.decode()   
                            txt_surface = font3.render('"%s" (Received %s)' % (subject, envelope.date), True, pygame.Color('lightskyblue3'))
                            textRect = txt_surface.get_rect()
                            textRect.center = (750, 90 + i)
                            screen.blit(txt_surface, textRect)
                            i += 20

                        except:
                            envelope = envelopes[j]
                            txt_surface = font3.render('"%s" (Received %s)' % (envelope.subject, envelope.date), True, pygame.Color('lightskyblue3'))
                            textRect = txt_surface.get_rect()
                            textRect.center = (750, 90 + i)
                            screen.blit(txt_surface, textRect)
                            i += 20

                else:
                    for j in range(len(envelopes)):
                        try: 
                            envelope = envelopes[j]
                            subject = envelope.subject.decode()   
                            txt_surface = font3.render('"%s" (Received %s)' % (subject, envelope.date), True, pygame.Color('lightskyblue3'))
                            textRect = txt_surface.get_rect()
                            textRect.center = (750, 90 + i)
                            screen.blit(txt_surface, textRect)
                            i += 20

                        except:
                            envelope = envelopes[j]
                            txt_surface = font3.render('"%s" (Received %s)' % (envelope.subject, envelope.date), True, pygame.Color('lightskyblue3'))
                            textRect = txt_surface.get_rect()
                            textRect.center = (750, 90 + i)
                            screen.blit(txt_surface, textRect)
                            i += 20
            else:
                txt_surface = font2.render('You have received no messages from this person.', True, pygame.Color('lightskyblue3'))
                textRect = txt_surface.get_rect()
                textRect.center = (750, 334)
                screen.blit(txt_surface, textRect)
            
            txt_surface = font.render('Your Messages', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (750, 25)
            screen.blit(txt_surface, textRect)
            txt_surface = font2.render('Press R to Return to the Menu', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (750, 668-15)
            screen.blit(txt_surface, textRect)
            txt_surface = font2.render('Press ENTER to Check Messages from Another Sender', True, pygame.Color('lightskyblue3'))
            textRect = txt_surface.get_rect()
            textRect.center = (750, 668-40)
            screen.blit(txt_surface, textRect)
   
            pygame.display.update()

#big oof