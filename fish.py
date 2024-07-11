#poisson disc sampling

 
import pygame
import math

pygame.init()
width, height = 1200, 800
surface = pygame.display.set_mode((width, height))

class Point:
  def __init__(self,pos,rad = 2,color=(255,255,255),width=1):
    self.rad = rad
    self.pos = pos
    self.color = color
    self.width=width
  def draw(self):
    pygame.draw.circle(surface, self.color,self.pos,self.rad,self.width)


objects = []

def poisson(radius, origin = (600,400),gridsize = [1200,800], trials = 30): #return a list of poisson disc
  cellsize = radius/(2**(1/2))
  grid = [[False for x in range(int(origin[0]//2))] for y in range(int(origin[-1]//2))]

  objects.append(Point(origin))
  #grid[y][x]
  grid[int(origin[-1]//cellsize)][int(origin[0]//cellsize)] = True

  
  return grid



poisson(5)

# while True:
#   surface.fill((0, 0, 0))
#   for object in objects:
#     object.draw()

#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       exit()

#   pygame.display.update()