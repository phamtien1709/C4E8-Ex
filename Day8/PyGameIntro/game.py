import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

done = False
game_finished = False
game_lose = False

# draw background
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# draw image
player_image = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("box.png")
key_image = pygame.image.load("key.png")
win_image = pygame.image.load("win.png")
lose_image = pygame.image.load("lose.png")

x = 100
y = 100

SQUARE_SIZE = 32

class Key:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self, dx, dy):
        return self.x + dx, self.y + dy

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self, dx, dy):
        return self.x + dx, self.y + dy

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(1, 1)
        self.box = Box(6, 6)
        self.key = Key (11, 13)

    def move_player(self, dx, dy):
        [next_player_x, next_player_y] = self.player.calc_next_position(dx, dy)
        [next_box_x, next_box_y] = self.box.calc_next_position(dx, dy)
        if self.check_inside(next_player_x, next_player_y):
            if next_player_x == self.box.x and next_player_y == self.box.y:
                if self.check_inside(next_box_x, next_box_y):
                    self.box.move(dx, dy)
                    self.player.move(dx, dy)
            else:
                self.player.move(dx, dy)

    def check_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def check_win(self):
        if self.box.x == self.key.x and self.box.y == self.key.y:
            return True
        return False
    def check_lose(self):
        if [self.box.x, self.box.y] == [0, 0] or [self.box.x, self.box.y] == [0, self.width-1] or [self.box.x, self.box.y] == [self.height - 1, 0] or [self.box.x, self.box.y] == [self.width - 1, self.height -1]:
            return True
        return False

map = Map(25, 18)


while not done:

    key_arrow = None

    # Get events
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1


    # Process game events
    if dx != 0 or dy != 0:
        map.move_player(dx, dy)
        if map.check_win():
            print("YOU WIN!")
            game_finished = True
        if map.check_lose():
            print("YOU LOSE!")
            game_lose = True


    # Repaint
    screen.fill(COLOR_WHITE)

    for x in range(map.width):
        for y in range(map.height):
            screen.blit(square_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

    screen.blit(key_image, (map.key.x * SQUARE_SIZE, map.key.y * SQUARE_SIZE))

    screen.blit(box_image, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))

    screen.blit(player_image, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))

    if game_finished == True:
        screen.blit(win_image, (250, 200))
        # done = True
    if game_lose == True:
        screen.blit(lose_image, (250, 200))

    pygame.display.flip()