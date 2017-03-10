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
player_image = pygame.image.load("images/mario.png")
square_image = pygame.image.load("images/plattform.jpg")
box_image = pygame.image.load("images/box.png")
key_image = pygame.image.load("images/door_win.png")

x = 100
y = 100

SQUARE_SIZE = 40