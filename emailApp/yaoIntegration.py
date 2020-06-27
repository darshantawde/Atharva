import smtplib, getpass

def emailConnector():
    while True:
        global conn, e, t
        e = input('Enter your email: ')
        p = getpass.getpass(prompt='Enter your password: ')
        if '@outlook.com' not in e:
            e += '@outlook.com'

        conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
        conn.ehlo()
        conn.starttls()

        try:    
            conn.login(e, p)
            print('Logged in as', e + '.')
            t = input('Enter the recipient (specify target domain): ')
            
            subject = input('Subject: ')
            a = input('Line 1: ')
            b = input('Line 2: ')
            name = input('Name: ')
            
            try:
                conn.sendmail(e, t, 'Subject:%s Message:%s' % (subject, str(a + b)))
                print('Email Sent!')
            except:
                print('Email failed to send.')
        
        except:
            print('Invalid Email or Password! Try Again!')
            continue        

emailConnector()



































