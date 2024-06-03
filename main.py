import pygame
from bird import Bird

def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 800))
    clock = pygame.time.Clock()
    game_running = True
    framerate = 60
    #time = 0

    flappy_bird = Bird("yellow", screen)

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        screen.fill("green")

        # Flap bird
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            flappy_bird.flap()

        # Update Pose based on physics and show
        flappy_bird.updatePose(framerate)
        flappy_bird.show()

        pygame.display.flip()

        clock.tick(framerate)

if __name__ == "__main__":
    main()