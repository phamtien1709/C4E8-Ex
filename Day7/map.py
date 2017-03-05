from player import Player
from box import Box
from gate import Gate
class Map:
    def __init__(self, width, height):
        self.player = Player(3, 4)
        self.box = Box(3, 3)
        self.gate = Gate(6,6)
        self.width = width
        self.height = height

    def print(self):
        for y in range(self.width):
            for x in range (self.height):
                if y == self.player.y and x == self.player.x:
                    print(self.player.text, end="")
                elif y == self.box.y and x == self.box.x:
                    print(self.box.text, end="")
                elif x == self.gate.x and y == self.gate.y:
                    print(self.gate.text, end="")
                else:
                    print("- ", end="")
            print()

    def move_player(self, dx, dy):
        self.player.move(dx, dy)


    def check_win(self):
        return self.box.x == self.gate.x and self.box.y == self.gate.y

    def process_input(self, move):
        dirtection = move.upper()
        if dirtection == "W":
            dx, dy = 0, -1
        elif dirtection == "S":
            dx, dy = 0, 1
        elif dirtection == "A":
            dx, dy = -1, 0
        elif dirtection == "D":
            dx, dy = 1, 0
        else:
            dx, dy = 0, 0
        if self.check_in_map(self.player.calc_next(dx, dy)[0], self.player.calc_next(dx, dy)[1]):
            if self.box.x == self.player.calc_next(dx, dy)[0] and self.box.y == self.player.calc_next(dx, dy)[1]:
                if self.check_in_map(self.box.calc_next(dx, dy)[0], self.box.calc_next(dx, dy)[1]):
                    self.box.move(dx, dy)
                    self.move_player(dx, dy)
            else:
                self.move_player(dx, dy)

    def check_in_map(self, x, y):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return True
        return False

    def loop(self):
        while True:
            move = input("Your move (W,A,S,D)?")
            self.process_input(move)
            self.print()
            if self.check_win():
                print("YOU WIN!!")
                break



