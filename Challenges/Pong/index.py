import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60
GAME_ENDED = False

player1_width, player1_height = 100, 10
player1_x, player1_y = WIDTH / 2 - player1_width / 2, HEIGHT - player1_height
player1_color = (0, 0, 255)
player1_vel = 7
player1_lost = False
 
player2_width, player2_height = player1_width, player1_height
player2_x, player2_y = WIDTH / 2 - player2_width / 2, 0
player2_color = (255, 0, 0)
player2_vel = 7
player2_lost = False

ball_center_x = WIDTH / 2
ball_center_y = HEIGHT / 2
ball_xvel, ball_yvel = 0, 0
ball_radius = 10 
ball_color = (255, 255, 255) 

def draw():
    WIN.fill(BACKGROUND_COLOR)
    if player1_lost != True: 
        pygame.draw.rect(WIN, player1_color, (player1_x, player1_y, player1_width, player1_height))
    if player2_lost != True:
        pygame.draw.rect(WIN, player2_color, (player2_x, player2_y, player2_width, player2_height))
    if GAME_ENDED != True:
        pygame.draw.circle(WIN, ball_color, (ball_center_x, ball_center_y), ball_radius)

run = True
clock = pygame.time.Clock() 
while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ball_xvel = -5
                ball_yvel = 2
    
    ball_center_x += ball_xvel
    ball_center_y += ball_yvel
    
    if ball_center_x + ball_radius >= WIDTH:
        ball_xvel *= (-1)
    if ball_center_x - ball_radius <= 0:
        ball_xvel *= (-1)
    if ball_center_y + ball_radius >= player1_y and ball_center_x + ball_radius <= player1_x + player1_width and ball_center_x - ball_radius >= player1_x:
        ball_yvel *= (-1)
    if ball_center_y - ball_radius <= player2_y and ball_center_x + ball_radius <= player2_x + player2_width and ball_center_x - ball_radius >= player2_x:
        ball_yvel *= (-1)

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_a] and player1_x > 0:
        player1_x -= player1_vel
    if keypressed[pygame.K_d] and player1_x + player1_width < WIDTH:
        player1_x += player1_vel
    
    if keypressed[pygame.K_LEFT] and player2_x > 0:
        player2_x -= player2_vel
    if keypressed[pygame.K_RIGHT] and player2_x + player2_width < WIDTH:
        player2_x += player2_vel

    if GAME_ENDED != True:
        if ball_center_y < 0:
            player2_lost = True
            GAME_ENDED = True
        if ball_center_y > HEIGHT:
            player1_lost = True
            GAME_ENDED = True

    draw() 
    pygame.display.update()
    
pygame.quit() 