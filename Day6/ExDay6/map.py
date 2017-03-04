from player import Player
class Map:
    def __init__(self, width, height):
        self.player = Player(3, 4)
        self.width = width
        self.height = height

    def print(self):
        for y in range(self.width):
            for x in range (self.height):
                if y == self.player.y and x == self.player.x:
                    print(self.player.text, end="")
                else:
                    print("- ", end="")
            print()
    def move_player(self, dx, dy):
        self.player.move(dx, dy)

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

        self.move_player(dx, dy)
    def loop(self):
        while True:
            move = input("Your move (W,A,S,D)?")
            self.process_input(move)
            self.print()


