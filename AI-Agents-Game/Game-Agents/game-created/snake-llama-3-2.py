import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.food = self.generate_food()
        self.score = 0
        self.high_score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and (0, 1) not in [(-y, x) for x, y in self.snake]:
            new_head = (self.snake[-1][0], self.snake[-1][1] - BLOCK_SIZE)
        elif keys[pygame.K_DOWN] and (0, 1) not in [(-y, x) for x, y in self.snake]:
            new_head = (self.snake[-1][0], self.snake[-1][1] + BLOCK_SIZE)
        elif keys[pygame.K_LEFT] and (1, 0) not in [(-y, x) for x, y in self.snake]:
            new_head = (self.snake[-1][0] - BLOCK_SIZE, self.snake[-1][1])
        elif keys[pygame.K_RIGHT] and (1, 0) not in [(-y, x) for x, y in self.snake]:
            new_head = (self.snake[-1][0] + BLOCK_SIZE, self.snake[-1][1])

        if self.check_collision(new_head):
            return False
        self.snake.append(new_head)
        if self.snake[-1] == self.food:
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.generate_food()
        else:
            self.snake.pop(0)

        return True

    def check_collision(self, new_head):
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in self.snake[:-1]):
            return True
        return False

    def run(self):
        while True:
            running = self.update()
            if not running:
                print("Game Over!")
                pygame.quit()
                sys.exit()
            self.draw()
            self.clock.tick(FPS)

    def draw(self):
        screen.fill((0, 0, 0))
        for pos in self.snake:
            pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (*self.food, BLOCK_SIZE, BLOCK_SIZE))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}, High Score: {self.high_score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))
        pygame.display.flip()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()