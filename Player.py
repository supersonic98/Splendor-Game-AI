import numpy as np
import copy

class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0
        self.emerald = 0
        self.sapphire = 0
        self.ruby = 0
        self.diamond = 0
        self.onyx = 0
        self.gold = 0
        self.bonus_emerald = 0
        self.bonus_sapphire = 0
        self.bonus_ruby = 0
        self.bonus_diamond = 0
        self.bonus_onyx = 0
        self.lvl_1 = []
        self.lvl_2 = []
        self.lvl_3 = []
        self.noble = []
        self.reserve = []


    def count_bonus(self):
        self.bonus_emerald = 0
        self.bonus_sapphire = 0
        self.bonus_ruby = 0
        self.bonus_diamond = 0
        self.bonus_onyx = 0

        for card_lvl_1 in self.lvl_1:
            if card_lvl_1.color == 'green':
                self.bonus_emerald +=1
            if card_lvl_1.color == 'blue':
                self.bonus_sapphire +=1
            if card_lvl_1.color == 'red':
                self.bonus_ruby +=1
            if card_lvl_1.color == 'white':
                self.bonus_diamond +=1
            if card_lvl_1.color == 'black':
                self.bonus_onyx +=1

        for card_lvl_2 in self.lvl_2:
            if card_lvl_2.color == 'green':
                self.bonus_emerald +=1
            if card_lvl_2.color == 'blue':
                self.bonus_sapphire +=1
            if card_lvl_2.color == 'red':
                self.bonus_ruby +=1
            if card_lvl_2.color == 'white':
                self.bonus_diamond +=1
            if card_lvl_2.color == 'black':
                self.bonus_onyx +=1

        for card_lvl_3 in self.lvl_3:
            if card_lvl_3.color == 'green':
                self.bonus_emerald +=1
            if card_lvl_3.color == 'blue':
                self.bonus_sapphire +=1
            if card_lvl_3.color == 'red':
                self.bonus_ruby +=1
            if card_lvl_3.color == 'white':
                self.bonus_diamond +=1
            if card_lvl_3.color == 'black':
                self.bonus_onyx +=1

    def getTotalTokens(self):
        return self.diamond + self.onyx + self.sapphire + self.ruby + self.emerald + self.gold

    def reset_bonus(self):
        self.bonus_emerald = 0
        self.bonus_sapphire = 0
        self.bonus_ruby = 0
        self.bonus_diamond = 0
        self.bonus_onyx = 0


    def print_player_cards(self):
        print('Player ID: ', self.id)
        print("Player Cards:")
        print("\t Level 1: ",)
        for card in self.lvl_1:
            print("\t", card.make_dict())
        print("\t Level 2: ")
        for card in self.lvl_2:
            print("\t", card.make_dict())
        print("\t Level 3: ")
        for card in self.lvl_3:
            print("\t", card.make_dict())
        print("\t Reserve: ")
        for card in self.reserve:
            print("\t", card.make_dict())

    def make_dict_tokens(self):
        return {
            'green': self.emerald,
            'blue': self.sapphire,
            'red': self.ruby,
            'white': self.diamond,
            'black': self.onyx,
            'gold': self.gold
        }
    def make_dict_bonus(self):
        return {
            'green': self.bonus_emerald,
            'blue': self.bonus_sapphire,
            'red': self.bonus_ruby,
            'white': self.bonus_diamond,
            'black': self.bonus_onyx,
        }
    def copyPlayer(self):
        return copy.deepcopy(self)