import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 15
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self.update_position()

    def update_position(self):
        x, y = self.positions[0]
        if self.direction == (-1, 0):  # Left
            new_head = (x - 1, y)
        elif self.direction == (1, 0):  # Right
            new_head = (x + 1, y)
        elif self.direction == (0, -1):  # Up
            new_head = (x, y - 1)
        elif self.direction == (0, 1):  # Down
            new_head = (x, y + 1)
        self.positions.insert(0, new_head)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif event.key == pygame.K_DOWN and self.direction != (-1, 0):
                    self.direction = (1, 0)
                elif event.key == pygame.K_LEFT and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif event.key == pygame.K_RIGHT and self.direction != (0, -1):
                    self.direction = (0, 1)

    def draw(self):
        for pos in self.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        while self.position in snake.positions:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    snake = Snake()
    food = Food(snake)
    score = 0

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        snake.move()
        snake.draw()

        food.update_position(food.position, snake.positions)

        if snake.positions[0] == food.position:
            score += 10
            food = Food(snake)
            snake.length += 1

        clock.tick(FPS)

        for pos in snake.positions:
            if pos[0] < 0 or pos[0] >= GRID_WIDTH or pos[1] < 0 or pos[1] >= GRID_HEIGHT:
                return
            if pos in snake.positions[:-1]:
                return

        food.draw()

        pygame.display.set_caption(f"Snake Game - Score: {score}")

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()