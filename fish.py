#poisson disc sampling

 
import pygame
import math
import random

pygame.init()
width, height = 1200, 800
surface = pygame.display.set_mode((width, height))

class Point:
  def __init__(self,pos,rad = 2,color=(255,255,255),width=1,id = -1):
    self.rad = rad
    self.pos = pos
    self.color = color
    self.width=width
    self.id = id #for debug
  def draw(self):
    pygame.draw.circle(surface, self.color,self.pos,self.rad,self.width)

origin = (600,400)
actives = [Point(origin)]
working = []
inactives = []

def inbounds(coords,bounds):
  if 0<=coords[0]<=bounds[0] and 0<=coords[1]<=bounds[1]:
    return True
  return False

def dist(p1,p2):
  if p1 == None or p2 == None:
    return 0
  return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)

def relocate(index,l1,l2):
  l1.remove(index)
  l2.append(index)

def drawall():
  for object in sum([inactives,actives,working],[]):
    if object in inactives:
      object.color = (255,0,0)
    if object in actives:
      object.color = (0,255,0)
    if object in working:
      object.color = (0,0,255)
    object.draw()

def poisson(radius,gridsize = [width,height], trials = 30,max=2,min=1): #return a list of poisson disc
  global actives
  global inactives
  global working
  global origin

  if len(actives)>=0: #replace with while after
    for active_point in actives.copy():
      for trial_num in range(trials):
        angle = random.randint(1,360)
        depth = random.randint(radius*min,radius*max)
        new_location = (math.cos(math.radians(angle))*depth+active_point.pos[0],math.sin(math.radians(angle))*depth+active_point.pos[1])
        if inbounds(new_location,gridsize):
          current_working = Point(new_location,id = trial_num)
          working.append(current_working)
          for other_point in working+actives+inactives:
            if current_working!=other_point and dist(current_working.pos, other_point.pos)<radius:
              working.remove(current_working)
              break
      
          #check if the new location is a minumum distance from other points
      actives.extend(working)
      working = []
      relocate(active_point,actives,inactives)

while True:
  surface.fill((0, 0, 0))
  drawall()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        poisson(20,[width,height])

  pygame.display.update()