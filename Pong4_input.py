import pygame, sys

def ball_animation():
  global ball_speed_x, ball_speed_y 

  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1
  if ball.left <= 0 or ball.right >= screen_width:
     ball_speed_x *= -1

  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1

def player_animation():
  player.y += player_speed

  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

#General setup
pygame.init()
clock = pygame.time.Clock()

#Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#colors
light_gray = (200,200,200)
bg_color = pygame.Color('grey12')

#Game Rectangles
ball = pygame.Rect(screen_width / 2 -15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2-70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

#Game Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_speed -= 7
      if event.key == pygame.K_DOWN:
        player_speed += 7
      if event.type == pygame.KEYUP:
        player_speed += 7
      if event.key == pygame.K_DOWN:
        player_speed -= 7

#Game Logic
  ball_animation()
  player_animation()

#Visuals
  screen.fill(bg_color)
  pygame.draw.rect(screen, light_gray, player)
  pygame.draw.rect(screen, light_gray, opponent)
  pygame.draw.ellipse(screen, light_gray, ball)
  pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0),(screen_width / 2, screen_height))

  pygame.display.flip()
  clock.tick(60)