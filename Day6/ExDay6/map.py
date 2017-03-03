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
                    print("P ", end="")
                else:
                    print("- ", end="")
            print()

map = Map(7, 7)
map.print()