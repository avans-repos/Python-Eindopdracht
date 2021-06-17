import random
from models.Color import Color
from models.Game import Game


class Mastermind:

    def __init__(self, Game):
        self.Game = Game

    def make_code(self):
        secret_code = []
        for x in range(self.Game.number_of_colors):
            color = self.get_random_color()

            if not self.Game.duplicate_color:
                while color in secret_code:
                    color = self.get_random_color()

            secret_code.append(color)

        Game.code = secret_code
        return secret_code

    def get_random_color(self):
        return Color(random.randint(0, self.Game.number_of_colors - 1))

    def guess_the_code(self, guessed_code):
        result = {
            "in_but_not_correct": 0,
            "correct": 0,
        }

        # ToDo: fix bug with duplicate colors
        for guessed_colors in range(len(guessed_code)):
            for color in range(len(self.Game.code)):
                if self.Game.code[color] == guessed_code[guessed_colors]:
                    if guessed_colors == color:
                        result["correct"] += 1
                    else:
                        result["in_but_not_correct"] += 1
                    break
        return result
