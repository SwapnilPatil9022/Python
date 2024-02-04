
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BIRD_SIZE = 40
GRAVITY = 1
JUMP_HEIGHT = 5
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 100
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy car")

# Load bird image
bird_image = pygame.image.load("Fly2.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_SIZE, BIRD_SIZE))

# Load pipe image
pipe_image = pygame.image.load("pipe2.png")
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))

# Clock to control the frame rate
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 5
        self.y = HEIGHT // 2
        self.velocity = 0
    def jump(self):
        self.velocity = -JUMP_HEIGHT

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)

    def move(self):
        self.x -= 5

    def draw(self):
        screen.blit(pipe_image, (self.x, 0), (0, 0, PIPE_WIDTH, self.height))
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP), (0, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Main game loop
def game():
    bird = Bird()
    pipes = [Pipe(WIDTH + i * (WIDTH // 2)) for i in range(2)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        bird.move()

        for pipe in pipes:
            pipe.move()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH))

            if bird.x < pipe.x < bird.x + BIRD_SIZE and (bird.y < pipe.height or bird.y + BIRD_SIZE > pipe.height + PIPE_GAP):
                # Bird hit a pipe, game over
                return

        screen.fill(BLACK)

        for pipe in pipes:
            pipe.draw()

        bird.draw()

        pygame.display.flip()
        clock.tick(FPS)

# Run the game
game()

