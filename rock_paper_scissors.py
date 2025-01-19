from random import randint


ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

while True:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or \n[q]uit if you want to quit the game: ").lower()

    if player_move == 'r':
        player_move = ROCK
    elif player_move == 'p':
        player_move = PAPER
    elif player_move == 's':
        player_move = SCISSORS
    else:
        break



    computer_random_number = randint(1,3)

    computer_move = ''
    if computer_random_number == 1:
        computer_move = ROCK
    elif computer_random_number == 2:
        computer_move = PAPER
    elif computer_random_number == 3:
        computer_move = SCISSORS

    print()
    print(f'You\'r choose: {player_move}')
    print(f'Computer choose: {computer_move}')


    if (player_move == ROCK and computer_move == SCISSORS
            or player_move == PAPER and computer_move == ROCK
            or player_move == SCISSORS and computer_move == PAPER):
        print('You win! 😁\n')
    elif player_move == computer_move:
        print('Draw! 😊\n')
    else:
        print('You lose! 🙁\n')

