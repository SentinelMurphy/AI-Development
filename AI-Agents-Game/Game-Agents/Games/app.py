import random
import os
import time
import pygame
import sys

# Direction constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.food = (random.randint(0, width - 1), random.randint(0, height - 1))
        self.direction = RIGHT
        self.score = 0
        pygame.init()
        self.display = pygame.display.set_mode((self.width * 10, self.height * 20))
        pygame.display.set_caption('Snake Game')
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        self.display.fill((0, 0, 0))
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) == self.food:
                    pygame.draw.rect(self.display, (255, 0, 0), (x * 10, y * 20, 10, 20))
                else:
                    pygame.draw.rect(self.display, (255, 255, 255), (x * 10, y * 20, 10, 20))

    def move_snake(self):
        new_head = self.snake[-1][0] + self.direction[0], self.snake[-1][1] + self.direction[1]
        if new_head in self.snake:
            return False
        self.snake.append(new_head)
        if new_head == self.food:
            self.score += 10
            self.generate_new_food()
            return True
        else:
            self.snake.pop(0)

    def generate_new_food(self):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if (x, y) not in self.snake and (x, y) != self.food:
                self.food = (x, y)
                break

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

        if not self.move_snake():
            return False

        # Collision with boundaries or self
        if (self.snake[-1][0] < 0 or self.snake[-1][0] >= self.width or 
            self.snake[-1][1] < 0 or self.snake[-1][1] >= self.height):
            return False

        for x, y in self.snake[:-1]:
            if (x, y) == self.snake[-1]:
                return False

        self.display.fill((0, 0, 0))
        self.draw_grid()

        text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.display.blit(text, (10, 10))

        pygame.display.flip()
        self.clock.tick(5)

    def play(self):
        while True:
            if not self.update():
                break
            time.sleep(0.05)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()