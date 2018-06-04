import numpy.random as random

def rock_paper_scissors():
    """
    Implementation of the game Rock, Paper, Scissors
    """
    scissors = {'rock': False, 'paper': True}
    rock = {'scissors': True, 'paper': False}
    paper = {'scissors': False, 'rock': True}
    
    choices = {'scissors': scissors, 'rock': rock, 'paper': paper}
    
    answer = None
    while answer not in choices:
        answer = input("'rock', 'paper', or 'scissors'? ")

    computer_answer = random.choice(['rock', 'paper', 'scissors'])

    if answer == computer_answer:
        print('Computer has {} as well!'.format(computer_answer))
        print('TIED GAME')
    else:
        if choices[answer][computer_answer]:
            print('Computer has {}'.format(computer_answer))
            print('YOU WON')
        else:
            print('Computer has {}'.format(computer_answer))
            print('YOU LOST')

    new_game = input("Another round? (y/n) ")
    if new_game in ['y', 'Y', 'yes', ]:
        rock_paper_scissors()

if __name__ == "__main__":
    rock_paper_scissors()