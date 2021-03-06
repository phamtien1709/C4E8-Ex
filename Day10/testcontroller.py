import pygame

from controllers.playercontroller import PlayerController, creat_player

pygame.init()
pygame.display.set_caption("Introduction to pygame")
screen = pygame.display.set_mode((400, 300))
done = False
BACK_GROUND = (148, 198, 153)

player_controller = creat_player(2, 3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player_controller.process(event.key)

    screen.fill(BACK_GROUND)

    player_controller.draw(screen)

    pygame.display.flip()
