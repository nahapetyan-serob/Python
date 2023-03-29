print('\nWelcome to Tic Tac Toe board game!\n')

board = [' '] * 10

def player1_choice():
    player_choice = 'Wrong'
    possible_choices = ['X', 'O']
    while player_choice not in possible_choices:
        player_choice = input('\nPlayer No 1 please choose either X or O: ')
        if player_choice not in possible_choices:
            print('\nInvalid symbol for Tic Tac Toe game\n')
    if player_choice == 'X':
        print ('Player No 1 you will start the game')
    else:
        print ('Player No 2 you will start the game')
    return player_choice


def display_board(board):
    print ('   |   |')
    print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('   |   |')
    print (11 * '-')
    print ('   |   |')
    print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('   |   |')
    print (11 * '-')
    print ('   |   |')
    print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('   |   |')

def position():
    board_position = 'Wrong'
    while not board_position.isdigit() or int(board_position) not in range(1,10):
        board_position = input('Please choose the position to put your symbol')
        if not board_position.isdigit():
            print('Please choose from 1 - 9')
        else:
            if int(board_position) not in range(1,10):
                print('Please choose from 1 - 9')
    return int(board_position)

def replay():
    board = [' '] * 10
    answer = 'Wrong'
    possible_answers = ['Yes', 'No']
    while answer not in possible_answers:
        answer = input('\nDo you want to play again?\n')
        if answer not in possible_answers:
            print('\nPlease answer Yes or no\n')
    if answer == 'Yes':
        gameplay(board)
    else:
        exit()

def winning_game(board):
    text = '\nCongrats! You have won the game'
    v1 = ['X', 'X', 'X']
    v2 = ['O', 'O', 'O']
    if board[1:4] == v1 or board[4:7] == v1 or board[7:] == v1 or board[1::4] == v1:
        print(text)
        replay()
    elif board[1::3] == v1 or board[2::3] == v1  or board[3::3]== v1 or board [3:8:2] == v1:
        print(text)
        replay()
    elif board[1:4] == v2 or board[4:7] == v2 or board [7:] == v2 or board[1::3] == v2:
        print(text)
        replay()
    elif board[2::3] == v2 or board[3::3] == v2 or board[1::4] == v2 or board[3:8:2] == v2:
        print(text)
        replay()
    else:
        pass

def gameplay(board):
    player_choice = player1_choice()
    display_board(board)
    while board.count(' ') != 1:
        for i in range(30):
            player_position = position()
            if player_choice == 'X':
                if i % 2 == 0:
                    if board[player_position] == ' ':
                        board[player_position] = 'X'
                    else:
                        print('\nThis spot is already taken\n')
                else:
                    if board[player_position] == ' ':
                        board[player_position] = 'O'
                    else:
                        print('\nThis spot is already taken\n')
            elif player_choice == 'O':
                if i % 2 == 0:
                    if board[player_position] == ' ':
                        board[player_position] = 'O'
                    else:
                        print('\nThis spot is already taken\n')
                else:
                    if board[player_position] == ' ':
                        board[player_position] = 'X'
                    else:
                        print('\nThis spot is already taken\n')
            print('\n' * 50)
            display_board(board)
            winning_game(board)
            if board.count(' ') == 1:
                break
    print("\nIt's a draw, try again to figure out the winner\n")

    replay()


gameplay(board)


