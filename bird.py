import pygame

class Bird:
    def __init__(self, color:str, screen:pygame.Surface):
        self.screen = screen
        self.pos = pygame.Vector2(self.screen.get_width()/3, self.screen.get_height()/2)
        self.velocity = pygame.Vector2(0,0)
        self.gravity = 1000
        self.color = color

    def show(self):
        # repeatedly called to show bird
        #pygame.draw.circle(self.screen, "red", self.pos, 40)
        pygame.draw.circle(self.screen, self.color, self.pos, 30)

    def flap(self):
        self.velocity.y = -300

    def updatePose(self, framerate):
        self.pos.y += self.velocity.y / framerate
        if self.pos.y >= self.screen.get_height():
            self.velocity.y = 0
        else:
            self.velocity.y += self.gravity / framerate