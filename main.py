import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
import sys

def main():
    pygame.init()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.contaniers = (shots, updatables, drawables)

    clock = pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    # game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit(0)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()