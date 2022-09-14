import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,BIRD
from dino_runner.components.obstacles.Cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import bird
class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                cactus = SmallCactus(SMALL_CACTUS)
                self.obstacles.append(cactus) 
            elif random.randint(0, 2) == 1:
                Lcactus = LargeCactus(LARGE_CACTUS)
                self.obstacles.append(Lcactus)
            elif random.randint(0, 2) == 2:
                Bird = bird(BIRD)
                self.obstacles.append(Bird)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Murio")
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

