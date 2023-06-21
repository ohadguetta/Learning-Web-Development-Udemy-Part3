import random


def whoWon(user,oppo):
    oppoFirst = oppo[0]
    if (user == 'r' and oppoFirst == 'r') or (user == 's' and oppoFirst =='s') or (user == 'p' and oppoFirst == 'p'):
        message = 'Its a Tie!'
    elif (user == 'r' and oppoFirst == 's') or (user == 's' and oppoFirst == 'p') or (user == 'p' and oppoFirst == 'r'):
        message = 'You Won!!!!'
    else:
        message = 'You lost :('
    return message



message = 'pick (R)ock,(P)aper or (S)cissors: '
user_input = input(message).lower()
if user_input == 'r' or user_input == 'p' or user_input == 's':
    if user_input == 'r':
        print('you chose Rock!')
    elif user_input == 's':
        print('you chose Scissors!')
    elif user_input == 'p':
        print('you chose Paper!')
    opponent = random.choice(['rock','paper','scissors'])
    print(whoWon(user_input,opponent))
    print('opponent was',opponent[0].upper()+opponent[1::])


