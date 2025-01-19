from random import randint

# These are the constants that will be used in the game.
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

while True:
    # We ask the player about his choice.
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or \n[q]uit if you want to quit the game: ").lower()

    # Assign a constant to the player choice
    if player_move == 'r':
        player_move = ROCK
    elif player_move == 'p':
        player_move = PAPER
    elif player_move == 's':
        player_move = SCISSORS
    else:
        break


    # Computer choice - a random int from 1 to 3.
    computer_random_number = randint(1,3)


    # Assign a constant to the computer choice.
    computer_move = ''
    if computer_random_number == 1:
        computer_move = ROCK
    elif computer_random_number == 2:
        computer_move = PAPER
    elif computer_random_number == 3:
        computer_move = SCISSORS

    # Print the choices.
    print()
    print(f'You\'r choose: {player_move}')
    print(f'Computer choose: {computer_move}')


    # Identify the winner of the game.
    if (player_move == ROCK and computer_move == SCISSORS
            or player_move == PAPER and computer_move == ROCK
            or player_move == SCISSORS and computer_move == PAPER):
        print('You win! 😁\n')
    elif player_move == computer_move:
        print('Draw! 😊\n')
    else:
        print('You lose! 🙁\n')

