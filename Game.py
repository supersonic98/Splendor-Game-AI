import random
import numpy as np
import copy
from Resources import  Card, Noble, Tokens
from itertools import combinations

# the following properties are constant
# each card is automatically assigned an id number
# level 1 cards have id numbers from 0-39 (inclusive)
# level 2 cards have id numbers from 40-69 (inclusive)
# level 3 cards have id numbers from 70-89 (inclusive)
# noble cards have id numbers from 90-99 (inclusive)
LEVEL_1 = [
    Card('black', 0, 1, 1, 1, 1, 0),
    Card('black', 0, 1, 2, 1, 1, 0),
    Card('black', 0, 2, 2, 0, 1, 0),
    Card('black', 0, 0, 0, 1, 3, 1),
    Card('black', 0, 0, 0, 2, 1, 0),
    Card('black', 0, 2, 0, 2, 0, 0),
    Card('black', 0, 0, 0, 3, 0, 0),
    Card('black', 1, 0, 4, 0, 0, 0),
    Card('blue', 0, 1, 0, 1, 1, 1),
    Card('blue', 0, 1, 0, 1, 2, 1),
    Card('blue', 0, 1, 0, 2, 2, 0),
    Card('blue', 0, 0, 1, 3, 1, 0),
    Card('blue', 0, 1, 0, 0, 0, 2),
    Card('blue', 0, 0, 0, 2, 0, 2),
    Card('blue', 0, 0, 0, 0, 0, 3),
    Card('blue', 1, 0, 0, 0, 4, 0),
    Card('white', 0, 0, 1, 1, 1, 1),
    Card('white', 0, 0, 1, 2, 1, 1),
    Card('white', 0, 0, 2, 2, 0, 1),
    Card('white', 0, 3, 1, 0, 0, 1),
    Card('white', 0, 0, 0, 0, 2, 1),
    Card('white', 0, 0, 2, 0, 0, 2),
    Card('white', 0, 0, 3, 0, 0, 0),
    Card('white', 1, 0, 0, 4, 0, 0),
    Card('green', 0, 1, 1, 0, 1, 1),
    Card('green', 0, 1, 1, 0, 1, 2),
    Card('green', 0, 0, 1, 0, 2, 2),
    Card('green', 0, 1, 3, 1, 0, 0),
    Card('green', 0, 2, 1, 0, 0, 0),
    Card('green', 0, 0, 2, 0, 2, 0),
    Card('green', 0, 0, 0, 0, 3, 0),
    Card('green', 1, 0, 0, 0, 0, 4),
    Card('red', 0, 1, 1, 1, 0, 1),
    Card('red', 0, 2, 1, 1, 0, 1),
    Card('red', 0, 2, 0, 1, 0, 2),
    Card('red', 0, 1, 0, 0, 1, 3),
    Card('red', 0, 0, 2, 1, 0, 0),
    Card('red', 0, 2, 0, 0, 2, 0),
    Card('red', 0, 3, 0, 0, 0, 0),
    Card('red', 1, 4, 0, 0, 0, 0),
]
LEVEL_2 = [
    Card('black', 1, 3, 2, 2, 0, 0),
    Card('black', 1, 3, 0, 3, 0, 2),
    Card('black', 2, 0, 1, 4, 2, 0),
    Card('black', 2, 0, 0, 5, 3, 0),
    Card('black', 2, 5, 0, 0, 0, 0),
    Card('black', 3, 0, 0, 0, 0, 6),
    Card('blue', 1, 0, 2, 2, 3, 0),
    Card('blue', 1, 0, 2, 3, 0, 3),
    Card('blue', 2, 5, 3, 0, 0, 0),
    Card('blue', 2, 2, 0, 0, 1, 4),
    Card('blue', 2, 0, 5, 0, 0, 0),
    Card('blue', 3, 0, 6, 0, 0, 0),
    Card('white', 1, 0, 0, 3, 2, 2),
    Card('white', 1, 2, 3, 0, 3, 0),
    Card('white', 2, 0, 0, 1, 4, 2),
    Card('white', 2, 0, 0, 0, 5, 3),
    Card('white', 2, 0, 0, 0, 5, 0),
    Card('white', 3, 6, 0, 0, 0, 0),
    Card('green', 1, 3, 0, 2, 3, 0),
    Card('green', 1, 2, 3, 0, 0, 2),
    Card('green', 2, 4, 2, 0, 0, 1),
    Card('green', 2, 0, 5, 3, 0, 0),
    Card('green', 2, 0, 0, 5, 0, 0),
    Card('green', 3, 0, 0, 6, 0, 0),
    Card('red', 1, 2, 0, 0, 2, 3),
    Card('red', 1, 0, 3, 0, 2, 3),
    Card('red', 2, 1, 4, 2, 0, 0),
    Card('red', 2, 3, 0, 0, 0, 5),
    Card('red', 2, 0, 0, 0, 0, 5),
    Card('red', 3, 0, 0, 0, 6, 0),
]
LEVEL_3 = [
    Card('black', 3, 3, 3, 5, 3, 0),
    Card('black', 4, 0, 0, 0, 7, 0),
    Card('black', 4, 0, 0, 3, 6, 3),
    Card('black', 5, 0, 0, 0, 7, 3),
    Card('blue', 3, 3, 0, 3, 3, 5),
    Card('blue', 4, 7, 0, 0, 0, 0),
    Card('blue', 4, 6, 3, 0, 0, 3),
    Card('blue', 5, 7, 3, 0, 0, 0),
    Card('white', 3, 0, 3, 3, 5, 3),
    Card('white', 4, 0, 0, 0, 0, 7),
    Card('white', 4, 3, 0, 0, 3, 6),
    Card('white', 5, 3, 0, 0, 0, 7),
    Card('green', 3, 5, 3, 0, 3, 3),
    Card('green', 4, 0, 7, 0, 0, 0),
    Card('green', 4, 3, 6, 3, 0, 0),
    Card('green', 5, 0, 7, 3, 0, 0),
    Card('red', 3, 3, 5, 3, 0, 3),
    Card('red', 4, 0, 0, 7, 0, 0),
    Card('red', 4, 0, 3, 6, 3, 0),
    Card('red', 5, 0, 0, 7, 3, 0),
]
NOBLE = [
    Noble(0, 3, 0, 0, 0, 4, 4),
    Noble(1, 3, 0, 0, 3, 3, 3),
    Noble(2, 3, 0, 4, 4, 0, 0),
    Noble(3, 3, 4, 4, 0, 0, 0),
    Noble(4, 3, 3, 3, 0, 0, 3),
    Noble(5, 3, 0, 0, 4, 4, 0),
    Noble(6, 3, 0, 3, 3, 3, 0),
    Noble(7, 3, 4, 0, 0, 0, 4),
    Noble(8, 3, 3, 3, 3, 0, 0),
    Noble(9, 3, 3, 0, 0, 3, 3),
]
COLOR_TO_TOKEN = {
    'green': 'emerald',
    'blue': 'sapphire',
    'red': 'ruby',
    'white': 'diamond',
    'black': 'onyx',
}

class Game:
    def __init__(self):
        self.turn = 0
        self.num_players = 2

        # individual cards from these decks will be deleted as
        # the game puts new cards on the board
        self.decks = {
            "level_1": copy.deepcopy(LEVEL_1),
            "level_2": copy.deepcopy(LEVEL_2),
            "level_3": copy.deepcopy(LEVEL_3),
        }
        self.tokens = Tokens()
        self.cards_on_the_board = []
        self.game_state = None
        self.actions = {
            "buy_card": None,
            "reserve_card": None,
            "get_tokens": None
        }

    def shuffle_deck(self, deck):
        n = len(deck)
        for i in range(n):
            j = random.randint(i, n - 1)
            temp = deck[j]
            deck[j] = deck[i]
            deck[i] = temp

    def switch_turns(self):
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0

    def print_board(self):
        print('Cards on the board: ')
        for level_ in self.cards_on_the_board.keys():
            print("\t", level_, ":")
            for ii in range(4):
                print("\t", self.cards_on_the_board[level_][ii].make_dict())
        print("Tokens available: ")
        print(self.tokens.make_dict())

    def pop_deck(self, lvl, index):
        # take the card
        val = self.decks['level_' + str(lvl)][index]
        # remove it from the deck
        self.decks['level_' + str(lvl)].pop(index)
        # and return the card
        return val

    def start_game(self):
        # shuffle each deck separately
        for deck in self.decks.keys():
            self.shuffle_deck(self.decks[deck])

        # open 4 cards from each deck
        self.cards_on_the_board = {
                    "level_1": [self.pop_deck(1, i) for i in range(4)],
                    "level_2": [self.pop_deck(2, i) for i in range(4)],
                    "level_3": [self.pop_deck(3, i) for i in range(4)],
        }

        # player 0 plays first
        self.turn = 0
        self.game_state = 'Start'
        print('Game started')
        print('Player 0 plays first')

    def find_requested_card(self, card_id):
        if card_id <= 39:
            index = 0
            for card in self.cards_on_the_board["level_1"]:
                if card.id == card_id:
                    card_to_buy = card
                    card_to_buy.level=1
                    return card_to_buy, 1, index

                index += 1

        elif card_id > 39 and card_id<=69:
            index = 0
            for card in self.cards_on_the_board["level_2"]:
                if card.id == card_id:
                    card_to_buy = card
                    card_to_buy.level = 2
                    return card_to_buy, 2, index
                index += 1

        elif card_id > 69 and card_id<=89:
            index = 0
            for card in self.cards_on_the_board["level_3"]:
                if card.id == card_id:
                    card_to_buy = card
                    card_to_buy.level = 3
                    return card_to_buy, 3, index
                index += 1

        print('The requested card is not on the board')
        return None, None, None

    def buy_cards(self, player, card_id, gold_gem_use=False, gold_gem_used_as = None):

        card_to_buy, lvl, index = self.find_requested_card(card_id)
        if card_to_buy is not None:
            # get players bonus points
            player.count_bonus()
            # if player chooses to use gold gem as something else
            gold_to_other_tokens = {
                'green': 0,
                'blue': 0,
                'red': 0,
                'white': 0,
                'black': 0,
            }
            if gold_gem_use == True:
                if player.gold>=len(gold_gem_used_as):
                    for i in range(len(gold_gem_used_as)):
                        # increment player's token by one
                        gold_to_other_tokens[gold_gem_used_as[i]] +=1
                else:
                    print('Not enough gold tokens')
                    return 0

            # if the player can afford to buy
            card_cost = card_to_buy.cost
            if player.emerald+player.bonus_emerald + gold_to_other_tokens['green'] >= card_cost['green'] and \
                       player.sapphire+player.bonus_sapphire + gold_to_other_tokens['blue'] >= card_cost['blue'] and\
                       player.ruby+player.bonus_ruby + gold_to_other_tokens['red'] >= card_cost['red'] and \
                       player.diamond+player.bonus_diamond + gold_to_other_tokens['white']>= card_cost['white'] and\
                       player.onyx+player.bonus_onyx + gold_to_other_tokens['black'] >= card_cost['black']:

                # add card to players resources
                if lvl == 1:
                    player.lvl_1.append(card_to_buy)
                elif lvl == 2:
                    player.lvl_2.append(card_to_buy)
                elif lvl == 3:
                    player.lvl_3.append(card_to_buy)

                # subtract tokens from player's resource
                if card_cost['green']>0:
                    player.emerald = player.emerald - (max(card_cost['green'] - player.bonus_emerald, 0) - gold_to_other_tokens['green'])
                if card_cost['blue']>0:
                    player.sapphire = player.sapphire - (max(card_cost['blue']  - player.bonus_sapphire, 0) - gold_to_other_tokens['blue'])
                if card_cost['red']>0:
                    player.ruby = player.ruby - (max(card_cost['red'] -  player.bonus_ruby, 0) - gold_to_other_tokens['red'])
                if card_cost['white']>0:
                    player.diamond = player.diamond - (max(card_cost['white'] - player.bonus_diamond, 0) - gold_to_other_tokens['white'])
                if card_cost['black']>0:
                    player.onyx = player.onyx - (max(card_cost['black']  - player.bonus_onyx, 0) - gold_to_other_tokens['black'])

                # increment player's score
                player.score += card_to_buy.points

                # add tokens back to the board
                if card_cost['green'] > 0:
                    self.tokens.green = self.tokens.green + (max(card_cost['green'] - player.bonus_emerald, 0) - gold_to_other_tokens['green'])
                if card_cost['blue'] > 0:
                    self.tokens.blue = self.tokens.blue + (max(card_cost['blue']  - player.bonus_sapphire, 0) - gold_to_other_tokens['blue'])
                if card_cost['red'] > 0:
                    self.tokens.red = self.tokens.red + (max(card_cost['red'] -  player.bonus_ruby, 0) - gold_to_other_tokens['red'])
                if card_cost['white'] > 0:
                    self.tokens.white = self.tokens.white + (max(card_cost['white'] - player.bonus_diamond, 0) - gold_to_other_tokens['white'])
                if card_cost['black'] > 0:
                    self.tokens.black = self.tokens.black + (max(card_cost['black']  - player.bonus_onyx, 0) - gold_to_other_tokens['black'])

                if gold_gem_use == True:
                    if player.gold >= len(gold_gem_used_as):
                        for i in range(len(gold_gem_used_as)):
                            # decrement player's gold gems
                            player.gold -= 1
                            # increment board gold
                            self.tokens.gold += 1

                # remove the card from the board
                self.cards_on_the_board['level_' + str(lvl)].pop(index)
                # pop a new card from the deck
                new_card = self.pop_deck(lvl, 0)
                # add that card to the board
                self.cards_on_the_board['level_' + str(lvl)].append(new_card)

                # reset player bonus points to zero to avoid stacking
                player.reset_bonus()
                return 1  # return 1 means the action was successfully applied
            else:
                print('Player cannot afford the card')
                return 0 # return 0 means the action could not be applied
        else:
            print('Requested card is not on the board')
            return 0

    def test_buy_card(self, player, card_id, gold_gem_use=False, gold_gem_used_as=None):
        card_to_buy, lvl, index = self.find_requested_card(card_id)
        missing_tokens = {
            'green': 0,
            'blue': 0,
            'red': 0,
            'white': 0,
            'black': 0,
        }
        if card_to_buy is not None:
            # get players bonus points
            player.count_bonus()
            # if player chooses to use gold gem as something else
            gold_to_other_tokens = {
                'green': 0,
                'blue': 0,
                'red': 0,
                'white': 0,
                'black': 0,
            }
            if gold_gem_use == True:
                if player.gold >= len(gold_gem_used_as):
                    for i in range(len(gold_gem_used_as)):
                        # increment player's token by one
                        gold_to_other_tokens[gold_gem_used_as[i]] += 1
                else:
                    return 0, missing_tokens

            # if the player can afford to buy
            card_cost = card_to_buy.cost
            if player.emerald + player.bonus_emerald + gold_to_other_tokens['green'] >= card_cost['green'] and \
                    player.sapphire + player.bonus_sapphire + gold_to_other_tokens['blue'] >= card_cost['blue'] and \
                    player.ruby + player.bonus_ruby + gold_to_other_tokens['red'] >= card_cost['red'] and \
                    player.diamond + player.bonus_diamond + gold_to_other_tokens['white'] >= card_cost['white'] and \
                    player.onyx + player.bonus_onyx + gold_to_other_tokens['black'] >= card_cost['black']:
                player.reset_bonus()
                return 1, missing_tokens  # return 1 means the action was successfully applied
            else:
                missing_tokens = {
                    'green': max(card_cost['green'] - (player.emerald + player.bonus_emerald), 0),
                    'blue': max(card_cost['blue'] - (player.sapphire + player.bonus_sapphire), 0),
                    'red': max(card_cost['red'] - (player.ruby + player.bonus_ruby), 0),
                    'white': max(card_cost['white'] - (player.diamond + player.bonus_diamond), 0),
                    'black': max(card_cost['black'] - (player.onyx + player.bonus_onyx), 0)
                }
                return 0, missing_tokens  # return 0 means the action could not be applied
        else:
            return 0, missing_tokens

    def test_reserve_card(self, player, card_id):
        card_to_buy, lvl, index = self.find_requested_card(card_id)
        total_number_of_tokens = player.getTotalTokens()
        if card_to_buy is not None and len(player.reserve)<3:
            return 1
        else:
            return 0

    def reserve_card(self, player, card_id):
        card_to_buy, lvl, index = self.find_requested_card(card_id)
        total_number_of_tokens = player.getTotalTokens()
        if card_to_buy is not None and len(player.reserve)<3:

            gold_on_the_board = self.tokens.gold
            if gold_on_the_board > 0 and total_number_of_tokens+1<=10:
                player.gold += 1
                self.tokens.gold -= 1
                player.reserve.append(card_to_buy)
                # remove the card from the board
                self.cards_on_the_board['level_' + str(lvl)].pop(index)
                # pop a new card from the deck
                new_card = self.pop_deck(lvl, 0)
                # add that card to the board
                self.cards_on_the_board['level_' + str(lvl)].append(new_card)
                return 1

            else:
                player.reserve.append(card_to_buy)
                # remove the card from the board
                self.cards_on_the_board['level_' + str(lvl)].pop(index)
                # pop a new card from the deck
                new_card = self.pop_deck(lvl, 0)
                # add that card to the board
                self.cards_on_the_board['level_' + str(lvl)].append(new_card)
                return 1
        else:
            print('Card cannot be reserved, either it is not on the board or you already have 3')
            return 0

    def test_buy_reserved_card(self, player, card_id, gold_gem_use=False, gold_gem_used_as = None):
        reserved_cards = player.reserve
        card_to_buy = None
        missing_tokens = {
            'green': 0,
            'blue': 0,
            'red': 0,
            'white': 0,
            'black': 0,
        }
        for card in reserved_cards:
            if card.id == card_id:
                card_to_buy = card

        if card_to_buy is not None:
            # get players bonus points
            player.count_bonus()
            # if player chooses to use gold gem as something else
            gold_to_other_tokens = {
                'green': 0,
                'blue': 0,
                'red': 0,
                'white': 0,
                'black': 0,
            }
            if gold_gem_use == True:
                if player.gold >= len(gold_gem_used_as):
                    for i in range(len(gold_gem_used_as)):
                        # increment player's token by one
                        gold_to_other_tokens[gold_gem_used_as[i]] += 1
                else:
                    return 0, missing_tokens

            # if the player can afford to buy
            card_cost = card_to_buy.cost
            if player.emerald + player.bonus_emerald + gold_to_other_tokens['green'] >= card_cost['green'] and \
                    player.sapphire + player.bonus_sapphire + gold_to_other_tokens['blue'] >= card_cost['blue'] and \
                    player.ruby + player.bonus_ruby + gold_to_other_tokens['red'] >= card_cost['red'] and \
                    player.diamond + player.bonus_diamond + gold_to_other_tokens['white'] >= card_cost['white'] and \
                    player.onyx + player.bonus_onyx + gold_to_other_tokens['black'] >= card_cost['black']:

                # reset player bonus points to zero to avoid stacking
                player.reset_bonus()
                return 1, missing_tokens  # return 1 means the action was successfully applied
            else:
                missing_tokens = {
                    'green': max(card_cost['green'] - (player.emerald + player.bonus_emerald), 0),
                    'blue': max(card_cost['blue'] - (player.sapphire + player.bonus_sapphire), 0),
                    'red': max(card_cost['red'] - (player.ruby + player.bonus_ruby), 0),
                    'white': max(card_cost['white'] - (player.diamond + player.bonus_diamond), 0),
                    'black': max(card_cost['black'] - (player.onyx + player.bonus_onyx), 0)
                }
                return 0, missing_tokens  # return 0 means the action could not be applied
        else:
            return 0, missing_tokens

    def buy_reserved_card(self, player, card_id, gold_gem_use=False, gold_gem_used_as = None):
        reserved_cards = player.reserve
        card_to_buy = None
        for card in reserved_cards:
            if card.id == card_id:
                card_to_buy = card

        if card_to_buy is not None:
            # get players bonus points
            player.count_bonus()
            # if player chooses to use gold gem as something else
            gold_to_other_tokens = {
                'green': 0,
                'blue': 0,
                'red': 0,
                'white': 0,
                'black': 0,
            }
            if gold_gem_use == True:
                if player.gold >= len(gold_gem_used_as):
                    for i in range(len(gold_gem_used_as)):
                        # increment player's token by one
                        gold_to_other_tokens[gold_gem_used_as[i]] += 1
                else:
                    print('Not enough gold tokens')
                    return 0

            # if the player can afford to buy
            card_cost = card_to_buy.cost
            if player.emerald + player.bonus_emerald + gold_to_other_tokens['green'] >= card_cost['green'] and \
                    player.sapphire + player.bonus_sapphire + gold_to_other_tokens['blue'] >= card_cost['blue'] and \
                    player.ruby + player.bonus_ruby + gold_to_other_tokens['red'] >= card_cost['red'] and \
                    player.diamond + player.bonus_diamond + gold_to_other_tokens['white'] >= card_cost['white'] and \
                    player.onyx + player.bonus_onyx + gold_to_other_tokens['black'] >= card_cost['black']:

                # add card to players resources
                if card_to_buy.level == 1:
                    player.lvl_1.append(card_to_buy)
                elif card_to_buy.level == 2:
                    player.lvl_2.append(card_to_buy)
                elif card_to_buy.level == 3:
                    player.lvl_3.append(card_to_buy)

                # subtract tokens from player's resource
                if card_cost['green'] > 0:
                    player.emerald = player.emerald - (
                                max(card_cost['green'] - player.bonus_emerald, 0) - gold_to_other_tokens['green'])
                if card_cost['blue'] > 0:
                    player.sapphire = player.sapphire - (
                                max(card_cost['blue'] - player.bonus_sapphire, 0) - gold_to_other_tokens['blue'])
                if card_cost['red'] > 0:
                    player.ruby = player.ruby - (
                                max(card_cost['red'] - player.bonus_ruby, 0) - gold_to_other_tokens['red'])
                if card_cost['white'] > 0:
                    player.diamond = player.diamond - (
                                max(card_cost['white'] - player.bonus_diamond, 0) - gold_to_other_tokens['white'])
                if card_cost['black'] > 0:
                    player.onyx = player.onyx - (
                                max(card_cost['black'] - player.bonus_onyx, 0) - gold_to_other_tokens['black'])

                # increment player's score
                player.score += card_to_buy.points

                # add tokens back to the board
                if card_cost['green'] > 0:
                    self.tokens.green = self.tokens.green + (
                                max(card_cost['green'] - player.bonus_emerald, 0) - gold_to_other_tokens['green'])
                if card_cost['blue'] > 0:
                    self.tokens.blue = self.tokens.blue + (
                                max(card_cost['blue'] - player.bonus_sapphire, 0) - gold_to_other_tokens['blue'])
                if card_cost['red'] > 0:
                    self.tokens.red = self.tokens.red + (
                                max(card_cost['red'] - player.bonus_ruby, 0) - gold_to_other_tokens['red'])
                if card_cost['white'] > 0:
                    self.tokens.white = self.tokens.white + (
                                max(card_cost['white'] - player.bonus_diamond, 0) - gold_to_other_tokens['white'])
                if card_cost['black'] > 0:
                    self.tokens.black = self.tokens.black + (
                                max(card_cost['black'] - player.bonus_onyx, 0) - gold_to_other_tokens['black'])

                # remove the card reserved
                player.reserve.remove(card_to_buy)

                # remove gold gems
                if gold_gem_use == True:
                    if player.gold >= len(gold_gem_used_as):
                        for i in range(len(gold_gem_used_as)):
                            # decrement player's gold gems
                            player.gold -= 1
                            # increment board gold
                            self.tokens.gold += 1


                # reset player bonus points to zero to avoid stacking
                player.reset_bonus()
                return 1  # return 1 means the action was successfully applied
            else:
                print('Player cannot afford the card')
                return 0  # return 0 means the action could not be applied
        else:
            return 0

    def test_get_tokens(self, player, tkns):
        # convert to set to get rid of duplicates
        tkns = set(tkns)
        tkns = list(tkns)

        total_number_of_tokens = player.getTotalTokens()
        # if player wants to take 2 of the same color
        if len(tkns)==1:

            # if there are enough tokens to buy
            val_tok = getattr(self.tokens, tkns[0])
            if val_tok == 4:
                if total_number_of_tokens + 2 > 10:
                    return 0
                else:
                    return 1

            elif val_tok<4 and val_tok > 0:
                for color in list(COLOR_TO_TOKEN.keys()):
                    if color in tkns:
                        continue
                    if getattr(self.tokens, color) > 0:
                        return 0

                if total_number_of_tokens + 1 > 10:
                    return 0
                else:
                    return 1
            else:
                return 0

        elif len(tkns) == 3:
            # get 3 tokens of different color

            if total_number_of_tokens + 3 > 10:
                return 0
            else:
                val_tok_0 = getattr(self.tokens, tkns[0])
                val_tok_1 = getattr(self.tokens, tkns[1])
                val_tok_2 = getattr(self.tokens, tkns[2])

                if val_tok_0 > 0 and val_tok_1 > 0 and val_tok_2 > 0:
                    return 1
                else:
                    return 0

        elif len(tkns) == 2:
            if total_number_of_tokens + 2 > 10:
                return 0
            else:

                for tk in tkns:
                    if getattr(self.tokens, tk)==0 or getattr(self.tokens, tk)==4:
                        return 0

                for color in list(COLOR_TO_TOKEN.keys()):
                    if color in tkns:
                        continue
                    if getattr(self.tokens, color) > 0:
                        return 0

                val_tok_0 = getattr(self.tokens, tkns[0])
                val_tok_1 = getattr(self.tokens, tkns[1])

                if val_tok_0 > 0 and val_tok_1 > 0:
                    return 1
                else:
                    return 0
        else:
            return 0

    def get_tokens(self, player, tkns):
        # convert to set to get rid of duplicates
        tkns = set(tkns)
        tkns = list(tkns)

        total_number_of_tokens = player.getTotalTokens()
        # if player wants to take 2 of the same color
        if len(tkns)==1:

            # if there are enough tokens to buy
            val_tok = getattr(self.tokens, tkns[0])
            if val_tok == 4:
                # increment players number of tokens
                val_ = getattr(player, COLOR_TO_TOKEN[tkns[0]])

                if total_number_of_tokens + 2 > 10:
                    print('Your total tokens exceeds 10')
                    return 0
                else:
                    setattr(player, COLOR_TO_TOKEN[tkns[0]], val_ + 2)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[0], val_tok - 2)
                    return 1

            elif val_tok<4 and val_tok>0:
                for color in list(COLOR_TO_TOKEN.keys()):
                    if color in tkns:
                        continue
                    if getattr(self.tokens, color) > 0:
                        print('Invalid token request')
                        return 0

                # increment players number of tokens
                val_ = getattr(player, COLOR_TO_TOKEN[tkns[0]])

                if total_number_of_tokens + 1 > 10:
                    print('Your total tokens exceeds 10')
                    return 0
                else:
                    setattr(player, COLOR_TO_TOKEN[tkns[0]], val_ + 1)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[0], val_tok - 1)
                    return 1

            else:
                print("There are not enough tokens to buy")
                return 0

        elif len(tkns) == 3:
            # get 3 tokens of different color

            if total_number_of_tokens + 3 > 10:
                print('Your total tokens exceeds 10')
                return 0
            else:
                val_tok_0 = getattr(self.tokens, tkns[0])
                val_tok_1 = getattr(self.tokens, tkns[1])
                val_tok_2 = getattr(self.tokens, tkns[2])

                if val_tok_0 > 0 and val_tok_1 > 0 and val_tok_2 > 0:
                    # token 0
                    # increment players number of tokens
                    val_ = getattr(player, COLOR_TO_TOKEN[tkns[0]])
                    setattr(player, COLOR_TO_TOKEN[tkns[0]], val_ + 1)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[0], val_tok_0 - 1)

                    # token 1
                    # increment players number of tokens
                    val_ = getattr(player, COLOR_TO_TOKEN[tkns[1]])
                    setattr(player, COLOR_TO_TOKEN[tkns[1]], val_ + 1)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[1], val_tok_1 - 1)

                    # token 2
                    # increment players number of tokens
                    val_ = getattr(player, COLOR_TO_TOKEN[tkns[2]])
                    setattr(player, COLOR_TO_TOKEN[tkns[2]], val_ + 1)

                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[2], val_tok_2 - 1)
                    return 1
                else:
                    print("There are not enough tokens to buy")
                    return 0

        elif len(tkns) == 2:
            if total_number_of_tokens + 2 > 10:
                print('Your total tokens exceeds 10')
                return 0
            else:

                for tk in tkns:
                    if getattr(self.tokens, tk)==0 or getattr(self.tokens, tk)==4:
                        print('Invalid token request')
                        return 0

                for color in list(COLOR_TO_TOKEN.keys()):
                    if color in tkns:
                        continue
                    if getattr(self.tokens, color) > 0:
                        print('Invalid token request')
                        return 0

                val_tok_0 = getattr(self.tokens, tkns[0])
                val_tok_1 = getattr(self.tokens, tkns[1])

                if val_tok_0 > 0 and val_tok_1>0:
                    # token 0
                    # increment players number of tokens
                    val_ = getattr(player, COLOR_TO_TOKEN[tkns[0]])
                    setattr(player, COLOR_TO_TOKEN[tkns[0]], val_ + 1)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[0], val_tok_0 - 1)

                    # token 1
                    # increment players number of tokens
                    val_ = getattr(player, COLOR_TO_TOKEN[tkns[1]])
                    setattr(player, COLOR_TO_TOKEN[tkns[1]], val_ + 1)
                    # decrement number tokens on the board
                    setattr(self.tokens, tkns[1], val_tok_1 - 1)
                    return 1
                else:
                    print("There are not enough tokens to buy")
                    return 0
        else:
            print('Please enter correct tokens')
            return 0

    def move(self, move):
        # action, player, tkns = None, card_id = None, gold_gem_use=False, gold_gem_used_as = None
        action = move[0]
        if action == 'Buy':
            action_result = self.buy_cards(move[1], move[2], move[3], move[4])
        elif action == 'Reserve':
            action_result = self.reserve_card(move[1], move[2])
        elif action == 'Get_tokens':
            action_result = self.get_tokens(move[1], move[2])
        elif action == 'Buy_reserve':
            action_result = self.buy_reserved_card(move[1], move[2], move[3], move[4])
        else:
            print("Please enter a valid move")
            action_result = 0
        if action_result == 0:
            return 0
        else:
            return 1

    def test_total_number_of_tokens(self, player):
        for color in COLOR_TO_TOKEN.keys():
           print('Total number of ', str(color), ' tokens: ',
                 getattr(self.tokens, str(color)) +
                 getattr(player, COLOR_TO_TOKEN[color]))

    def win(self, player):
        if player.score >= 15:
            self.game_state = 'Terminal'
            return True

    def getLegalMoves(self, player):
        legalMoves = []
        # card buying
        for lvl in list(self.cards_on_the_board.keys()):
            for card in self.cards_on_the_board[lvl]:
                if card == None:
                    continue
                # without using gold gems
                action_success, missing_tokens = self.test_buy_card(player, card.id, gold_gem_use=False, gold_gem_used_as=None)
                if action_success == 1:
                    legalMoves.append(['Buy', player,  card.id, False, None])
                else:
                    # try using gold if there are any available
                    total_missing = 0
                    for color in missing_tokens.keys():
                        total_missing += missing_tokens[color]

                    if total_missing > player.gold:
                        continue
                    gold_gem_used_as = []

                    for color in missing_tokens.keys():
                        for tk in range(missing_tokens[color]):
                            gold_gem_used_as.append(color)

                    action_success, missing_tokens = self.test_buy_card(player, card.id, gold_gem_use=True, gold_gem_used_as=gold_gem_used_as)
                    if action_success == 1:
                        legalMoves.append(['Buy', player, card.id, True, gold_gem_used_as])
        # reserve card
        for lvl in list(self.cards_on_the_board.keys()):
            for card in self.cards_on_the_board[lvl]:
                if card == None:
                    continue
                if card.points == 0:
                    continue
                action_success= self.test_reserve_card(player, card.id)
                if action_success == 1:
                    legalMoves.append(['Reserve', player, card.id])
        # buy reserved card
        if len(player.reserve)>0:
            for card in player.reserve:
                # without using gold gems
                action_success, missing_tokens = self.test_buy_reserved_card(player, card.id, gold_gem_use=False,
                                                                    gold_gem_used_as=None)
                if action_success == 1:
                    legalMoves.append(['Buy_reserve', player, card.id, False, None])
                else:
                    # try using gold if there are any available
                    total_missing = 0
                    for color in missing_tokens.keys():
                        total_missing += missing_tokens[color]

                    if total_missing > player.gold:
                        continue
                    gold_gem_used_as = []
                    for color in missing_tokens.keys():
                        for tk in range(missing_tokens[color]):
                            gold_gem_used_as.append(color)
                    action_success, missing_tokens= self.test_buy_reserved_card(player, card.id, gold_gem_use=True,
                                                    gold_gem_used_as=gold_gem_used_as)
                    if action_success == 1:
                        legalMoves.append(['Buy_reserve',player, card.id, True, gold_gem_used_as])
        # get tokens
        # get 1 color
        for color in list(COLOR_TO_TOKEN.keys()):
            action_success = self.test_get_tokens(player, [color])
            if action_success == 1:
                legalMoves.append(['Get_tokens', player, [color]])
        # get 2 colors
        comb2 = combinations(list(COLOR_TO_TOKEN.keys()), 2)
        for comb in comb2:
            action_success = self.test_get_tokens(player, comb)
            if action_success == 1:
                legalMoves.append(['Get_tokens', player, comb])
        # get 3 colors
        comb3 = combinations(list(COLOR_TO_TOKEN.keys()), 3)
        for comb in comb3:
            action_success = self.test_get_tokens(player, comb)
            if action_success == 1:
                legalMoves.append(['Get_tokens', player, comb])
        """
        for color1 in list(COLOR_TO_TOKEN.keys()):
            action_success = self.test_get_tokens(player, [color1])
            if action_success == 1:
                legalMoves.append(['Get_tokens', player, [color1]])
            for color2 in list(COLOR_TO_TOKEN.keys()):
                if color1 == color2:
                    continue
                action_success = self.test_get_tokens(player, [color1, color2])
                if action_success == 1:
                    legalMoves.append(['Get_tokens', player, [color1, color2]])
                for color3 in list(COLOR_TO_TOKEN.keys()):
                    if color3 == color2 or color3 == color1:
                        continue
                    action_success = self.test_get_tokens(player, [color1, color2, color3])
                    if action_success == 1:
                        legalMoves.append(['Get_tokens', player, [color1, color2, color3]])
        """

        return legalMoves

    def SimulateMove(self, move):
        if move[0] == "Buy" or move[0] == "Reserve":
            game_states = []
            dummy1, lvl, dummy2 = self.find_requested_card(move[2])
            #for i in range(len(self.decks["level_" + str(lvl)])):
            #    game1 = copy.deepcopy(self)
            #    move2 = copy.deepcopy(move)
            #    move2[1] = move[1].copyPlayer()
            #    tmp = game1.decks["level_" + str(lvl)][i]
            #    game1.decks["level_" + str(lvl)][i] = game1.decks["level_" + str(lvl)][0]
            #    game1.decks["level_" + str(lvl)][0] = tmp
            #    game1.move(move2)
            #    game_states.append(game1)
            game1 = copy.deepcopy(self)
            game1.decks["level_" + str(lvl)][0] = None
            game1.move(move)
            return [game1]

        else:
            game = copy.deepcopy(self)
            game.move(move)
            return [game]


