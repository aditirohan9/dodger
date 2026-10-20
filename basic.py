import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player
player_x = 250
player_y = 150
player_size = 50
speed = 5

# Enemy settings
enemy_size = 50
enemy_speed = 5
num_enemies = 5

# Create enemies
enemies = []
for i in range(num_enemies):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(-300, 0)
    enemies.append([x, y])

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # Keep player inside screen
    player_x = max(0, min(player_x, WIDTH - player_size))
    player_y = max(0, min(player_y, HEIGHT - player_size))

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

        if enemy[1] > HEIGHT:
            enemy[1] = 0
            enemy[0] = random.randint(0, WIDTH - enemy_size)

    # Collision detection
    for enemy in enemies:
        if (player_x < enemy[0] + enemy_size and
            player_x + player_size > enemy[0] and
            player_y < enemy[1] + enemy_size and
            player_y + player_size > enemy[1]):

            print("GAME OVER")
            running = False

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))

    pygame.display.update()

pygame.quit()
sys.exit()