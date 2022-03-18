import numpy as np
import pygame
from Scene import Scene
from Camera import Camera
from Tracing import Ray_Table

pygame.init()
size = 200
size = width, height = (size,size)
screen = pygame.display.set_mode(size)

camera = Camera(FOV=90,location=[0,0,0],pitch=90,yaw=90)# FOV 46.8
world = Scene(active_camera=camera)


table  = Ray_Table(camera, world, size )# will be the screen resolution

table.trace()

table.display(screen)


pygame.display.flip()
print('done')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        




