import os
import random
import time
import sys
import pygame
pygame.init()

# Add comments explaining functions, variables, and classes
class Snake:
    def __init__(self, size=(400, 400), color=pygame.Color('green')):
        self.size = size
        self.color = color
        self.segments = [pygame.Vector2(size[0] // 2, size[1] // 2)]
        self.direction = pygame.Vector2(0, 1)

    # ... (Other methods remain the same)

class Food:
    def __init__(self, size, color=pygame.Color('red')):
        self.size = size
        self.color = color
        self.pos = pygame.Vector2(random.randrange(size[0]), random.randrange(size[1]))

    # ... (Other methods remain the same)

def game_loop():
    clock = pygame.time.Clock()
    speed = 5
    game_over = False
    screen = pygame.display.set_mode((400, 400))
    snake = Snake(screen.get_size())
    food = Food(screen.get_size())

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            keys = pygame.key.get_pressed()
            if any([keys[pygame.K_UP], keys[pygame.K_w]]) and snake.direction != pygame.Vector2(0, -1):
                snake.direction = pygame.Vector2(0, -1)
            elif any([keys[pygame.K_DOWN], keys[pygame.K_s]]) and snake.direction != pygame.Vector2(0, 1):
                snake.direction = pygame.Vector2(0, 1)
            elif any([keys[pygame.K_LEFT], keys[pygame.K_a]]) and snake.direction != pygame.Vector2(-1, 0):
                snake.direction = pygame.Vector2(-1, 0)
            elif any([keys[pygame.K_RIGHT], keys[pygame.K_d]]) and snake.direction != pygame.Vector2(1, 0):
                snake.direction = pygame.Vector2(1, 0)
        if not snake.segments:
            game_over = True
        else:
            snake.move(snake.direction)
            snake.check_collision()
            screen.fill((30, 30, 30))
            pygame.draw.rect(screen, food.color, pygame.Rect(food.pos, food.size))
            for segment in snake.segments:
                pygame.draw.rect(screen, snake.color, pygame.Rect(segment, (2, 2)))
            pygame.display.update()
            clock.tick(speed)
    pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--menu":
        main_menu()
    else:
        game_loop()