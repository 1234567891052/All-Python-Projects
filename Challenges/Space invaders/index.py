import pygame
import random
pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

pygame.display.set_caption('Space Invaders')
player_width, player_height = 100, 10
player_x, player_y = WIDTH / 2 - player_width / 2, HEIGHT - player_height
player_color = (0, 0, 255)
player_velocity = 5

bullets = []
bullet_velocity = 15
enemies = []
enemy_limit = 10

for i in range(enemy_limit):
    enemy = pygame.Rect(random.random() * WIDTH, random.randint(0, HEIGHT/2), 20, 20) 
    enemies.append(enemy)

def draw():
    WIN.fill(BACKGROUND_COLOR)
    for bullet in bullets:
        pygame.draw.rect(WIN, (255, 255, 255), bullet)
        bullet.y -= bullet_velocity
    pygame.draw.rect(WIN, player_color, (player_x, player_y, player_width, player_height))
    for enemy in enemies:
        pygame.draw.rect(WIN, (255, 0, 0), enemy)

clock = pygame.time.Clock() 
run = True
while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                bullet = pygame.Rect(player_x + player_width/2, player_y, 5, 10) 
                bullets.append(bullet) 
    draw()
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_a] and player_x > 0:
        player_x -= player_velocity
    if keypressed[pygame.K_d] and player_x + player_width < WIDTH:
        player_x += player_velocity        
    pygame.display.update()
pygame.quit() 