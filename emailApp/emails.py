import smtplib, getpass

def emailConnector():
    while True:
        global conn, e, t
        e = input('Enter your email: ')
        p = getpass.getpass(prompt='Enter your password: ')
        e += '@gmail.com'
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        print('Logged in as', e + '.')

        try:    
            conn.login(e, p)
            t = input('Enter your target email (Who you\'re going to send the email to): ')  
            t += '@gmail.com'
            pass
        except:
            print('Invalid Email or Password! Try Again!')
            continue        

            subject = input('Subject: ')
            a = input('Line 1: ')
            b = input('Line 2: ')
            name = input('Name: ')
            
            try:
                conn.sendmail(e, t, 'Subject:%s\n%s\n%s\n-%s' % (subject, a, b, name))
                print('Email Sent!')
            except:
                print('Email failed to send.')

emailConnector()



































