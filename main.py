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

    # Assign container for each sprite class
    Asteroid.containers = (roids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    # Create initial field and player
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # Uncomment the next lines if you have shoot functionality implemented
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE:
                    # player.shoot(dt)

        # Update all updatable sprites
        for sprite in updatable:
            sprite.update(dt)

        # Check for collisions between player and asteroids
        for roid in roids:
            if player.collide(roid):
                print("Game over!")
                return

        # Check for collisions between shots and asteroids
        for shot in shots:
            for roid in roids:
                if shot.collide(roid):
                    shot.kill()  # Remove the shot
                    print("Hit!")
                    roid.split()  # Split the asteroid

        # Clear the screen
        screen.fill("Black")
        
        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()