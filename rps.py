import random
print('welcome to rock paper sizers! (shoot the computer to quit)')

# player's score
plyrs = 0
# computer's score
cmps = 0

# options
opts = ['rock', 'paper', 'sizers']

while(True):
    # user's choice
    usrch = input('{}-{}  > '.format(plyrs, cmps))
    # quit
    if usrch == 'q':
        break
    # computer's choice
    cmpch = random.choice(opts)
    print(cmpch)
    if (usrch == 'rock' and cmpch == 'sizers') or (usrch == 'paper' and cmpch == 'rock') or (usrch == 'sizers' and cmpch == 'paper'):
        print('u win')    
        plyrs += 1
    elif usrch == cmpch:
        continue
    else:
        print('u lose')
        cmps += 1
