import random
print('welcome to rock paper sizers! (shoot the computer to quit)')
# options
opts = ['rock', 'paper', 'sizers']

while(True):
    # user's choice
    usrch = input('> ')
    if usrch == 'q':
        break
    # computer's choice
    cmpch = random.choice(opts)
    print(cmpch)
    if (usrch == 'rock' and cmpch == 'sizers') or (usrch == 'paper' and cmpch == 'rock') or (usrch == 'sizers' and cmpch == 'paper'):
        print('u win')    
    elif usrch == cmpch:
        continue
    else:
        print('u lose')
