import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    roids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (roids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #player.shoot(dt)
         
        for sprite in updatable:
            sprite.update(dt)   

        for roid in roids:
            if player.collide(roid):
                print("Game over!")
                return
            
        for shot in shots:
            for roid in roids:
                if shot.collide(roid):
                    shot.kill()
                    print("Hit!")
            
        screen.fill("Black")
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()