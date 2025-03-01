import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
pacman_size = 50
pacman_speed = 5
pacman_pos = [WIDTH / 2, HEIGHT / 2]
pacman_vx, pacman_vy = 0, 0

# Set up the food dots
food_dot_size = 20
food_dots = []
for _ in range(10):
    x = random.randint(0, WIDTH - food_dot_size)
    y = random.randint(0, HEIGHT - food_dot_size)
    food_dots.append([x, y])

# Set up the ghosts
ghost_size = 30
ghosts = []
for _ in range(5):
    x = random.randint(0, WIDTH - ghost_size)
    y = random.randint(0, HEIGHT - ghost_size)
    ghosts.append([x, y])
pacman_vx, pacman_vy = 0, 0

# Set up the lives
lives = 3

def main():
    level = 1
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman_vy -= pacman_speed
                elif event.key == pygame.K_DOWN:
                    pacman_vy += pacman_speed
                elif event.key == pygame.K_LEFT:
                    pacman_vx -= pacman_speed
                elif event.key == pygame.K_RIGHT:
                    pacman_vx += pacman_speed

        # Move the player
        pacman_pos[0] += pacman_vx
        pacman_pos[1] += pacman_vy

        # Collision with food dots
        for i, dot in enumerate(food_dots):
            if (dot[0] < pacman_pos[0] + pacman_size and
                    dot[0] + food_dot_size > pacman_pos[0] and
                    dot[1] < pacman_pos[1] + pacman_size and
                    dot[1] + food_dot_size > pacman_pos[1]):
                food_dots.pop(i)
                lives += 1

        # Collision with ghosts
        for i, ghost in enumerate(ghosts):
            if (ghost[0] - pacman_speed < pacman_pos[0] < ghost[0] + pacman_speed and
                    ghost[1] - pacman_speed < pacman_pos[1] < ghost[1] + pacman_speed):
                lives -= 1

        # Level progression
        if len(food_dots) == 0:
            level += 1
            if level > 5:
                break
            for dot in food_dots:
                x = random.randint(0, WIDTH - food_dot_size)
                y = random.randint(0, HEIGHT - food_dot_size)
                food_dots.append([x, y])
            pacman_speed += 1
        else:
            for i, dot in enumerate(food_dots):
                if level > 2:
                    x = random.randint(pacman_pos[0], pacman_pos[0] + pacman_speed) if random.random() < 0.5 else random.randint(pacman_pos[0] - pacman_speed, pacman_pos[0])
                    y = random.randint(dot[1], dot[1] + pacman_speed) if random.random() < 0.5 else random.randint(dot[1] - pacman_speed, dot[1])

        # Draw everything
        screen.fill(WHITE)
        for dot in food_dots:
            pygame.draw.rect(screen, (0, 255, 0), (dot[0], dot[1], food_dot_size, food_dot_size))
        for ghost in ghosts:
            pygame.draw.ellipse(screen, RED, (ghost[0], ghost[1], ghost_size, ghost_size))
        pygame.draw.circle(screen, YELLOW, pacman_pos, pacman_size)
        text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        screen.blit(text, [10, 10])
        pygame.display.flip()

        # Cap the framerate
        clock.tick(60)

if __name__ == "__main__":
    main()