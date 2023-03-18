import pygame, random
from pygame. constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

screen = width, heigth = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((15, 15))
ball.fill(WHITE)
bal_rect = ball.get_rect()
ball_speed = 1

is_working = True

while is_working:
   for event in pygame.event.get():
      if event.type == QUIT:
         is_working = False  
   
   pressed_keys = pygame.key.get_pressed()

   main_surface.fill(BLACK)
   
   main_surface.blit(ball, bal_rect)
   if pressed_keys[K_DOWN]:
      bal_rect = bal_rect.move(0, ball_speed)
      
   if pressed_keys[K_UP]:
      bal_rect = bal_rect.move(0, -ball_speed)
      
   if pressed_keys[K_LEFT]:
      bal_rect = bal_rect.move(-ball_speed, 0)
      
   if pressed_keys[K_RIGHT]:
      bal_rect = bal_rect.move(ball_speed, 0)
          
   pygame.display.flip()