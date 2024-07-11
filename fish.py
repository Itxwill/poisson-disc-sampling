#poisson disc sampling

 
import pygame
import math


origin = (600,400) 

def poisson(radius,gridsize = [1200,800]): #return a list of poisson disc
  cellsize = radius/(2**(1/2))
  grid = [[0 for x in range(int(1200//cellsize))] for y in range(int(800//cellsize))]
  for y in grid:
    print(y)


poisson(5)


pygame.init()
 
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

while True:
  screen.fill((0, 0, 0))
  pygame.display.update()



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()