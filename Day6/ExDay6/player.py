class Player:
    def __init__(self, x, y): #constructure
        self.x = x
        self.y = y
        self.text = "P "

    def print(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y
    def calc_next(self, dx, dy):
        return (self.x + dx),(self.y + dy)
    def match(self, x, y):
        return self.x == x and self.y == y