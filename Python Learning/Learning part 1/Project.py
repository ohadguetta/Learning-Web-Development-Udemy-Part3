import random


def whoWon(user,oppo):
    oppoFirst = oppo[0]
    if (user == 'r' and oppoFirst == 'r') or (user == 's' and oppoFirst =='s') or (user == 'p' and oppoFirst == 'p'):
        message = 'Its a Tie!'
    elif (user == 'r' and oppoFirst == 's') or (user == 's' and oppoFirst == 'p') or (user == 'p' and oppoFirst == 'r'):
        message = 'You Won, Good job !!'
    else:
        message = 'You Lost :(('
    return message



message = 'pick (R)ock,(P)aper or (S)cissors or quit: '
user_input = input(message).lower()
while user_input != 'quit':
    if user_input in ['r','p','s']:
        opponent = random.choice(['rock','paper','scissors'])
        print(whoWon(user_input,opponent))
        if user_input == 'r':
            print('you chose Rock')
        elif user_input == 's':
            print('you chose Scissors')
        elif user_input == 'p':
            print('you chose Paper')
        print('opponent was',opponent[0].upper()+opponent[1::])
    else:
        print('Please type: R/P/S')    
    user_input = input(message).lower()


