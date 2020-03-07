import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 100, 10)
paddleA.rect.x = 350
paddleA.rect.y = 450

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddleA.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddleA.move_right(5)

    all_sprites_list.update()

    # if ball touch right wall
    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]

    # if ball touch left wall
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    
    # if ball touch bottom wall
    if ball.rect.y > 490:
        if scoreA != 0:
            scoreA -= 1
        ball.velocity[1] = -ball.velocity[1]
    
    # if ball touch top wall
    if ball.rect.y < 0:
        scoreA += 1
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA):
        ball.bounce()

    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    # display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (350, 10))

    pygame.display.flip()

    clock.tick(120)

pygame.quit()
