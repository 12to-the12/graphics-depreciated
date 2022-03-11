# I'm sorry I didn't comment better. Just remember Object.object_data is the important thing
#
import sys, pygame
from pygame import gfxdraw
import random
import math
from math import atan
from math import sin
from math import cos
from math import degrees
from math import radians
import numpy as np

from Object import *
from Camera import *
from Vector_Math import *
from Rendering import *
from Objects import *
from Stop_Watch import *
from time import sleep
from time import time
from numba import jit

print('done importing')
#import scipy
Stop_Watch.timing_flag = False
#sleep(1) 
pygame.init()
size = width, height = (1000,1000)
speed = [1, 1]
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

#print(screen.get_size() )


camera = Camera(FOV=46.8,location=[0,0,0],pitch=90,yaw=90)# FOV 46.8


pygame.mouse.set_visible(False)

#boxa = Object(mesh,location=[0,5,0] )
a = np.array([ [ -1,0,0],[0,0,-1],[2,2,-1]])

#print( xcartesian_to_polar(a) )

#print(Object.object_data[:,0])


#Object.object_data = Object.fetch_vectors(Object.object_data, Object.vertex_data)

#print(Object.object_data[:,0])
delta = 0

x = np.array( [  [0,5,0],[-1,5,0], [2,2,2]    ] )
y = np.array( [  [1,0,0],[1,0,0],[0,-1,-3]  ]    )
#print(dot_product(x, y))
#print(angle(x, y))
#print( normal_vector(x))
#print('origins:',Object.origin_list)
#print( xcartesian_to_polar(x))
#print(         '3d to 2d:', project(camera, x)    )

init_cubes()
def main(): # this is the main loop where everything happens
    stamp = time() 
    print('start epoch:',stamp)
    #time.sleep(0.5)
    sum = 0
    passed = 0

    move_forward = False
    move_backward = False
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    while 1:
        camera.FOV += 0.1
        if passed%300==0:print('.')
        #print(passed)
        delta  = time()-stamp # this thing allows you to track time per frame
        stamp  = time()
        
        #print('stamp',stamp)
        #print('delta',delta)
        sum += delta
        if passed>100: 
            passed = 0
            sum = 0
        passed += 1
        #print(1/delta)
        #print('FPS:',(passed/(sum+0.01))  )
        #clock = pygame.time.Clock()
        # Limit to 60 frames per second
        #clock.tick(24)
        xyz = 2
        #Object.origin_list[:,xyz] = Object.origin_list[:,xyz] + 0.1
        amount = 0.5
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_forward = True

                elif event.key == pygame.K_s:
                    move_backward = True

                elif event.key == pygame.K_a:
                    move_left = True

                elif event.key == pygame.K_d:
                    move_right = True    

                elif event.key == pygame.K_UP:
                    move_up = True

                elif event.key == pygame.K_DOWN:
                    move_down = True   

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_forward = False

                elif event.key == pygame.K_s:
                    move_backward = False

                elif event.key == pygame.K_a:
                    move_left = False

                elif event.key == pygame.K_d:
                    move_right = False  

                elif event.key == pygame.K_UP:
                    move_up = False

                elif event.key == pygame.K_DOWN:
                    move_down = False    

        if move_forward:  camera.move(dy= +amount)
        if move_backward: camera.move(dy= -amount)
        if move_left:     camera.move(dx= -amount)
        if move_right:    camera.move(dx= +amount)
        if move_up:       camera.move(dz= +amount)
        if move_down:     camera.move(dz= -amount)
        
    
        screen.fill((0, 0, 0))
        render(screen, camera, Object)
        #cruiser.location[1] += 0.1
        #box.location[2] += 0.01
        #camera.location[2] += 0.05
        #camera.pitch += 0.1
        
        #camera.location[2] += 0.1
        
        #pygame.gfxdraw.aapolygon(screen, [[300, 300], [i, i],[100, 300]],(255, 0, 0))
        #screen.blit(bouncer, (rect.x, rect.y))
        
        #print(i)
        
        pygame.display.flip()
        #time.sleep(50000000000000000)
        #print(Object.object_data[:,0,0])
        #print('\n\n\n\n')
        #sleep(0.5)
        #print('total:',(time()-stamp)*1000)
        #print()
        


main()

















