import pygame
from bird import Bird
from pipe import PipePair
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 800))
    clock = pygame.time.Clock()
    game_running = True
    framerate = 60
    time = 0

    flappy_bird = Bird("yellow", screen)
    pipe_pairs = []
    cooldown = False

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        screen.fill("blue")

        # Flap bird
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            flappy_bird.flap()

        # Update Pose based on physics and show
        flappy_bird.updatePose(framerate)
        flappy_bird.show()

        # Spawn new pipe every 5 seconds
        if math.floor(time) % 5 == 0 and not cooldown:
            cooldown = True
            pipe_pairs.append(PipePair("green", screen))
        if (math.floor(time) - 1) % 5 == 0:
            cooldown = False

        # Show and update all pipes   
        for pair in pipe_pairs:
            pair.show()
            pair.updatePose(framerate)

        # Remove old pipes
        if len(pipe_pairs) > 10:
            pipe_pairs.pop(0)

        pygame.display.flip()

        time += clock.tick(framerate) / 1000

if __name__ == "__main__":
    main()