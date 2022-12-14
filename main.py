import pygame, sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        pygame.mixer.Sound.play(pong_sound)

    if ball.left <=0:
        score_time = pygame.time.get_ticks()
        player_score += 1
        pygame.mixer.Sound.play(score_sound)
    elif ball.right >= screen_width:
        score_time = pygame.time.get_ticks()
        opponent_score +=1
        pygame.mixer.Sound.play(score_sound)


    if ball.colliderect(player) or ball.colliderect((opponent)):
        ball_speed_x *= -1
        pygame.mixer.Sound.play(pong_sound)

def playeranimation():
    player.y += player_speed

    if player.top<= 0:
        player.top = 0
    if player.bottom>=screen_height:
        player.bottom = screen_height

def opponent_ai():

    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.top > ball.y:
        opponent.y -= opponent_speed

    if opponent.top<= 0:
        opponent.top = 0
    if opponent.bottom>=screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x,ball_speed_y, ball_moving, score_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        countdown = basic_font.render("3", False, light_grey)
        screen.blit(countdown, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        screen.blit(basic_font.render("2", False, light_grey), (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        screen.blit(basic_font.render("1", False, light_grey), (screen_width / 2 - 10, screen_height / 2 + 20))
    if current_time - score_time < 2100:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_x = 7* random.choice((1, -1))
        ball_speed_y = 7* random.choice((1, -1))
        score_time = None;




#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode(size=(screen_width, screen_height))
pygame.display.set_caption("Pong")

#background colours
light_grey = (200,200,200)
bg_colour = pygame.Color('grey12')

#Game objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(20, screen_height/2 - 70, 10, 140 )

#Game variables
ball_speed_x = 4 * random.choice((1,-1))
ball_speed_y = 4 * random.choice((1, -1))
player_speed = 0
opponent_speed = 4
ball_moving = False
score_time = True


#Score text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32 )

#Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed +=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -=7

    #Visuals
    screen.fill(bg_colour)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height)  )

    #Game Logic
    ball_animation()
    playeranimation()
    opponent_ai()

    player_text = basic_font.render(f'{player_score} ' , False, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = basic_font.render(f'{opponent_score} ', False, light_grey)
    screen.blit(opponent_text, (605, 470))

    if score_time:
        ball_start()

#HW create opponent text score
    #Updating frame rate

    pygame.display.flip()
    clock.tick(60)
