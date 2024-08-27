import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frames = pygame.time.Clock()
    dt = 0
    
    player = PlayerShape(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        pygame.Surface.fill(screen,(0,0,0))
        player.draw(screen)
        player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # print("Starting asteroids!")
        # print(f"Screen width: {SCREEN_WIDTH}")
        # print(f"Screen height: {SCREEN_HEIGHT}")
        pygame.display.flip()
        dt = frames.tick(60) / 1000

if __name__ == "__main__":
    main()
