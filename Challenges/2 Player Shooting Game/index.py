import pygame
import os
pygame.init()

WIDTH, HEIGHT = 500, 700 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COL = (0, 0, 0)
FPS = 60 

player_w, player_h = 100, 10
player_x, player_y = WIDTH / 2 - player_w / 2, HEIGHT - player_h
player_col = (0, 0, 255)
player_vel = 5
player_bullets = []

opponent_w, opponent_h = 100, 10
opponent_x, opponent_y = WIDTH / 2 - player_w / 2, 0
opponent_col = (255, 0, 0)
opponent_vel = player_vel
opponent_bullets = []

bullet_vel = 10
opponent_bullet_vel = 11

player_health = 15
opponent_health = 10

def draw(): 
    WIN.fill(BACKGROUND_COL)
    if player_health > 0 :
        pygame.draw.rect(WIN, player_col, (player_x, player_y, player_w, player_h))
        for i in player_bullets:
            pygame.draw.rect(WIN, player_col, i)
            i.y -= bullet_vel
    if opponent_health > 0 :
        pygame.draw.rect(WIN, opponent_col, (opponent_x, opponent_y, opponent_w, opponent_h))            
        for i in opponent_bullets:
            pygame.draw.rect(WIN, opponent_col, i) 
            i.y += opponent_bullet_vel

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                bullet = pygame.Rect(player_x + player_w/2, player_y, 5, 10)
                player_bullets.append(bullet)
            if event.key == pygame.K_RCTRL:
                bullet = pygame.Rect(opponent_x + opponent_w/2, opponent_y, 5, 10)
                opponent_bullets.append(bullet)
            
    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_a] and player_x > 0:
        player_x -= player_vel

    if keypressed[pygame.K_d] and player_x + player_w < WIDTH:
        player_x += player_vel

    if keypressed[pygame.K_LEFT] and opponent_x > 0:
        opponent_x -= opponent_vel

    if keypressed[pygame.K_RIGHT] and opponent_x + opponent_w < WIDTH:
        opponent_x += opponent_vel        

    for i in player_bullets:
        if i.colliderect((opponent_x, opponent_y, opponent_w, opponent_h)):
            opponent_health -= 1.5
    for i in opponent_bullets:
        if i.colliderect((player_x, player_y, player_w, player_h)):
            player_health -= 1

    draw() 
    pygame.display.update() 