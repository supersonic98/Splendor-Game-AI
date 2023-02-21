import itertools

class Card:
    newID = itertools.count()
    def __init__(self, c, p, w=0, bl=0, g=0, r=0, ch=0):
        self.color = c
        self.level = None
        self.points = p
        self.cost = {
            'white': w,
            'blue': bl,
            'green': g,
            'black': ch,
            'red': r,
        }
        self.id = next(Card.newID)

    def make_dict(self):
        return {
            'ID': self.id,
            'color': self.color,
            'points': self.points,
            'cost': self.cost
        }

    def print_card(self):
        print(self.make_dict())

class Tokens:
    def __init__(self):
        self.white = 4
        self.black = 4
        self.green = 4
        self.red = 4
        self.blue = 4
        self.gold = 5

    def make_dict(self):
        return {
            "white": self.white,
            "black": self.black,
            "green": self.green,
            "red": self.red,
            "blue": self.blue,
            "gold": self.gold
        }

    def print_tokens(self):
        print(self.make_dict())