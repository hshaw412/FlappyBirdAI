import pygame
import random

class Pipe:
    def __init__(self, color:str, screen:pygame.Surface, initial_y):
        self.screen = screen
        self.pos = pygame.Vector2(self.screen.get_width(), initial_y)
        self.speed = -100
        self.color = color

    def show(self):
        rect = pygame.Rect(self.pos, (80, self.screen.get_height()))
        pygame.draw.rect(self.screen, self.color, rect)

    def updatePose(self, framerate):
        self.pos.x += self.speed / framerate

class PipePair:
    def __init__(self, color:str, screen:pygame.Surface):
        self.screen = screen
        self.color = color
        self.width_between = 180
        self.pair_y = random.uniform(self.width_between, self.screen.get_height() - self.width_between)
        self.bottom_pipe = Pipe(color, screen, self.pair_y)
        self.top_pipe = Pipe(color, screen, self.pair_y - self.width_between - self.screen.get_height())

    def show(self):
        self.bottom_pipe.show()
        self.top_pipe.show()

    def updatePose(self, framerate):
        self.bottom_pipe.updatePose(framerate)
        self.top_pipe.updatePose(framerate)