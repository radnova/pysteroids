import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("Black")
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()