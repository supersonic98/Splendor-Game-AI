import numpy as np
from Player import Player
from Game import Game
import random
import time
import ai_player


NumRuns = 1
ai_wins = 0
for rn in range(NumRuns):

    p_0 = Player(0)
    p_1 = Player(1)
    game = Game()
    game.start_game()
    # game.print_board()

    game.game_state = 'Play'

    depth = 0

    print("RUN TEST ", rn+1)
    while True:
        if (game.win(p_0) == True):
            print('\nPlayer 0 wins')
            break
        elif (game.win(p_1) == True):
            ai_wins = ai_wins+1
            print('\nPlayer 1 wins')
            break

        player_turn = game.turn
        if player_turn == 0:
            # make random move
            moves = game.getLegalMoves(p_0)
            if len(moves) != 0:
                #random_move = random.randint(0, len(moves)-1)
                move = ai_player.monte_carlo_tree_search(game, p_0, p_1)
                game.move(move)
                # print player resources
                print('Game Depth: ',depth, 'Player 0 played: total tokens: ', p_0.getTotalTokens(), ' player score: ',
                      p_0.score, ' Num of res. cards: ', len(p_0.reserve))
            else:
                print("No moves, Passing")
        if player_turn == 1:
            # make random move
            moves = game.getLegalMoves(p_1)
            if len(moves) != 0:
                # random_move = random.randint(0, len(moves)-1)
                # game.print_board()
                # p_1.print_player_cards()
                # print(p_1.make_dict_tokens())
                print("Number of moves: ", len(moves))
                start = time.time()
                pred, move = ai_player.minmax(game, p_1, p_0, 0, 0)
                end = time.time()
                print("Minimax run time: ", end-start)
                move[1] = p_1
                print("Move: ", move)
                print("Preditcted Store: ", pred)
                game.move(move)
                print('Game Depth: ',depth, ' Player 1 played: total tokens: ', p_1.getTotalTokens(), ' player score: ',
                      p_1.score , ' Num of res. cards: ', len(p_1.reserve))
            else:
                print("No moves, passing")

        game.switch_turns()
        depth += 1


    game.tokens.print_tokens()
