#bp_OS

#Introduction
print('Welcome to bp_OS! Use the command \'help\' for the list of all \navailable commands! ')

#Parts of the Code
from time import *
while True: 
    cmd = input('bp_OS - Type a command > ') 
    if cmd == 'ping':
        print('Pong!')
    elif cmd == 'say':
        print('It\'s a bit more complex command and I\'m not so advanced, but we can try.')
        print('First, what do you want me to say?')
        word = input()
        print('Sweet! You can print the word by typing \'say word\'')
    elif cmd == 'say word':
        print(word)
    elif cmd == 'help':
        print('Don\'t worry, I am here to help you out. \nThese are the commands available on bpOS:')
        print('help - Prints this list. USAGE: help')
        print('ping - Says back \"Pong!\" USAGE: ping')
        print('say - Says anything you want. USAGE: Type \"say\". Then type the \ntext that you want to see on your screen. After you are done, type \"say word\"')
        print('calculator - A workig calculator, that can add, sub, multiply and divide numbers. USAGE: calc > add / sub / mul / div > Write the numbers ')
        print('welcome - Welcomes you. USAGE: welcome > type your name')
        print('card - Generates you a card with your information. USAGE: card')
        print('time - Gives you the current time in your timezone. USAGE: time')
        print('epic - Loads a hilarious command. Use it only for your own risk. USAGE: epic load *')
        print('esc - Exits and closes the window. USAGE: esc')
        print('ATTENTION! You need to type the exact same things after \'usage\', \nin this case everything must be typed with lowercase.')
    elif cmd == ' ':
        print('I am not that stupid, don\'t try to juke me.')
    elif cmd == '':
        print('I am not that stupid, don\'t try to juke me.')
    elif cmd == 'hello':
        print('Hello friend, what do you want to talk about today?')
    elif cmd == 'how are you':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'how r u':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'how are you?':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'How are you?':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'How are you':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'hru':
        print('Thank you for the question, I am fine. :D')
    elif cmd == 'esc':
        exit()
    elif cmd == 'calculator':
        print('----- CALCULATOR -----')
        print('Included in bp_OS')
        print()
        print('Alright! Please follow my instructions to calculate!')
        print('First of all, what kind of thing do you want to do?')
        print('add / sub / mul / div')
        op = input()
        print('Cool! Now, which numbers do you want to \ncalculate with?')
        print('NOTE: If you want to work only with 2 numbers instead of 3, \nplease don\'t leave the fields blank, write 0 to one of the spaces.')
        n1 = int(input('First Number: '))
        n2 = int(input('Second Number: '))
        n3 = int(input('Third Number: '))
        if op == 'add':
            add_op = n1 + n2 + n3
            print('Your result is ', add_op, '.')
        elif op == 'sub':
            sub_op = n1 - n2 - n3
            print('Your result is ', sub_op, '.')
        elif op == 'mul':
            mul_op= n1 * n2 * n3
            print('Your result is ', mul_op, '.')
        elif op == 'div':
            div_op = n1 / n2 / n3
            print('Your result is ', div_op, '.')
    elif cmd == 'asd':
        print('If you don\'t know something and came to test, use the command \'help\'!')

    elif cmd == 'asdasd':
        print('If you don\'t know something and came to test, use the command \'help\'!')        

    elif cmd == 'asdasdasd':
        print('If you don\'t know something and came to test, use the command \'help\'!')

    elif cmd == 'welcome':
        welcome_name = input('Hello there! How can I call you? \n')
        print('Nice to meet you, ', welcome_name,'! Welcome to bp_OS!')

    elif cmd == 'card':
        print('----- CARD GENERATOR -----')
        print('Included in bp_OS')
        print()
        print('Let\'s get started!')
        card_name = input ('First, what is your name? \n')
        print('Thanks,', card_name, '!')
        card_age = input('Then, how old are you? \n')
        card_job = input('Sweet! What is your job? \n')
        card_hobby = input('OK! And finally: what is/are your hobby(s)? \n')
        print('You are awesome! I am ready to calculate your infos.')
        print('Status: 2%')
        sleep(2)
        print('Status: 9%')
        sleep(1)
        print('Status: 23%')
        sleep(3)
        print('Status: 59%')
        sleep(1)
        print('Status: 74%')
        sleep(4)
        print('Status: 98%')
        sleep(1)
        print('Status: 100%')
        sleep(1)
        print('Final Calculating...')
        print('Here it is, your card is done!')
        print()
        print('Name:', card_name)
        print('Age: ', card_age)
        print('Job: ', card_job)
        print('Hobby(s):', card_hobby)
    elif cmd == 'time':
        print('Your time is: %s' % ctime())

    elif cmd == 'epic':
        print('Commands available for EPIC:')
        print('load')

    elif cmd == 'epic load *':
        print('Preparing..')
        sleep(1)
        print('Preparing...')
        sleep(1)
        print('Preparing....')
        sleep(2)
        print('Checking for availability...')
        sleep(1)
        print('No issues found.')
        sleep(0.5)
        print('Downloading assets...')
        print('Progress below.')
        print('[|||||     ]')
        sleep(1.2)
        print('[|||||||   ]')
        sleep(3)
        print('[||||||||| ]')
        sleep(2.7)
        print('[||||||||||]')
        print('Downloading artifacts...')
        sleep(3)
        print('Setup was successful.')
        sleep(0.3)
        print('Combining data...')
        sleep(1)
        print('1%')
        sleep(2)
        print('3%')
        sleep(6)
        print('18%')
        sleep(3.6)
        print('24%')
        sleep(3)
        print('26%')
        sleep(2)
        print('33%')
        sleep(5.6)
        print('45%')
        sleep(1)
        print('63%')
        sleep(4.5)
        print('86%')
        sleep(3)
        print('92%')
        sleep(0.2)
        print('100%')
        sleep(3)
        print('Successfully loaded 0 item(s) from library \'epic\'.')
        
        
    else: 
        print('Hmmm... I cannot recognize the command \'', cmd, '\'. Maybe you \nmisspelled something?')
        
