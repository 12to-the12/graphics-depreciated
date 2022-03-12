# I'm sorry I didn't comment better
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
from Scene import Scene

from time import sleep
from time import time
from numba import jit

print('done importing')
#import scipy
Stop_Watch.timing_flag = True
#sleep(1) 
pygame.init()
size = 1000
size = width, height = (size,size)
speed = [1, 1]
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

#print(screen.get_size() )


camera = Camera(FOV=46.8,location=[0,0,0],pitch=90,yaw=90)# FOV 46.8

world = Scene(active_camera=camera)


#init_cubes()
init_obj('danny.obj', [0,5,3])
init_obj('text.obj', [0,5,0])
def main(): # this is the main loop where everything happens
    print('entering main loop')
    world.vertexes = world.raw_vertexes
    stamp = time() 
    #print('start epoch:',stamp)
    #time.sleep(0.5)
    sum = 0
    passed = 0

    move_forward = False
    move_backward = False
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    update_rotation = False
    sensitivity = 100
    while 1:
        if Stop_Watch.loops%Stop_Watch.frequency==0:
            print('.')
        delta  = time()-stamp # this thing allows you to track time per frame
        stamp  = time()
        
        #print('stamp',stamp)
        #print('delta',delta)
        sum += delta
        if passed>100: 
            passed = 0
            sum = 0
        
        #print(passed)
        #print(1/delta)
        #print('FPS:',(passed/(sum+0.01))  )
        #clock = pygame.time.Clock()
        # Limit to 60 frames per second
        #clock.tick(24)
        xyz = 2
        #Object.origin_list[:,xyz] = Object.origin_list[:,xyz] + 0.1
        amount = 0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_yaw = camera.yaw
                start_pitch = camera.pitch
                initial_pos = pygame.mouse.get_pos()
                update_rotation = True
            if event.type == pygame.MOUSEBUTTONUP:
                update_rotation = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()
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

        if move_forward:  camera.move(amount*+camera.y_vector)
        if move_backward: camera.move(amount*-camera.y_vector)
        if move_left:     camera.move(amount*-camera.x_vector)
        if move_right:    camera.move(amount*+camera.x_vector)
        if move_up:       camera.move([0,0,+amount])
        if move_down:     camera.move([0,0,-amount])
        if update_rotation:
            pos = pygame.mouse.get_pos()
            size = screen.get_size()
            x = (pos[0]-initial_pos[0]) / size[0]
            y = (pos[1]-initial_pos[1]) / size[1]
            
            camera.set_yaw( x*sensitivity + start_yaw )
            camera.set_pitch( -y*sensitivity + start_pitch )
        
        
        render(screen, camera)
        Stop_Watch.loops += 1



main()

















