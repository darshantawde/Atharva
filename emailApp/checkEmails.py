#import imaplib (the og one)
import imapclient, getpass

def emailChecker():    
    while True:
        conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        username = input('Enter your email: ')
        password = getpass.getpass(prompt='Enter your password: ')
        username += '@gmail.com'

        try:
            conn.login(username, password)
            pass
        except:
            print('Re-enter credentials.')
            continue

        print('Logged in as', username + '.')
        friend = input('Check emails from: ')
        friend += '@gmail.com'

        conn.select_folder('INBOX', readonly=True)
        messages = conn.search(['FROM', friend])
        
        if len(messages) == 1:
            print('%d message from %s' % (len(messages), friend))
        else:
            print('%d messages from %s' % (len(messages), friend))

        if len(messages) > 0:
            for id, data in conn.fetch(messages, ['ENVELOPE']).items():
                envelope = data[b'ENVELOPE']
                try: 
                    subject = envelope.subject.decode()   
                    print('ID #%d: "%s" (Received %s)\n' % (id, subject, envelope.date))
                except:
                    print('ID #%d: "%s" (Received %s)\n' % (id, envelope.subject, envelope.date))
        else:
            print('Oof!\n')

emailChecker()