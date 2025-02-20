import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if player.collision(obj) == True:
                print("Game over!")
                sys.exit()
        
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot) == True:
                    shot.kill()
                    obj.split()

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()