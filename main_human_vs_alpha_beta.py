import numpy as np
from Player import Player
from Game import Game
import random
import time
import ai_player

p_0 = Player(0)
p_1 = Player(1)
game = Game()
game.start_game()
# game.print_board()

game.game_state='Play'

depth = 0
while True:
    if (game.win(p_0) == True):
        print('\nPlayer 0 wins')
        break
    elif (game.win(p_1) == True):
        print('\nPlayer 1 wins')
        break

    player_turn = game.turn
    if player_turn == 0:
        # make random move
        print("BOARD:\n")
        game.print_board()
        moves = game.getLegalMoves(p_0)
        print("YOUR TOKENS:")
        print(p_0.make_dict_tokens())
        print("YOUR CARDS:")
        p_0.print_player_cards()
        print("YOUR AVAILAIBLE MOVES:")
        print("ENTER INTEGER NUMBER CORRESPONDING TO THE MOVE YOU WANT TO MAKE")
        for move in range(len(moves)):
            print(move, '\t', moves[move])

        while True:
            try:
                move = int(input('Input your move\n'))
                game.move(moves[move])
                break
            except:
                print('Wrong move, try again')
        # print player resources
        print('Game Depth: ',depth, 'Player 0 played: total tokens: ', p_0.getTotalTokens(), ' player score: ',
              p_0.score, ' Num of res. cards: ', len(p_0.reserve))
    if player_turn == 1:
        # make random move
        moves = game.getLegalMoves(p_1)
        if len(moves) ==0:
            print('no more moves left')
            moves = game.getLegalMoves(p_1)
            break
        # random_move = random.randint(0, len(moves)-1)
        print("Number of moves: ", len(moves))
        start = time.time()
        _, move = ai_player.minmax(game, p_1, p_0, 0, 0)
        end = time.time()
        print("Minimax run time: ", end-start)
        move[1] = p_1
        print("Move: ", move)
        game.move(move)
        print('Game Depth: ',depth, ' Player 1 played: total tokens: ', p_1.getTotalTokens(), ' player score: ',
              p_1.score , ' Num of res. cards: ', len(p_1.reserve))

    game.switch_turns()
    depth += 1


game.tokens.print_tokens()
