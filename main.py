# I'm sorry I didn't comment better
#


'''
Moving away from an object oriented pipeline would allow me to speed things up significantly
'''
print('<START>')
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
from Tracing import Ray_Table

#from Tracing import Tracer

from time import sleep
from time import time
from numba import jit

print('done importing')
#import scipy
Stop_Watch.timing_flag = True
#sleep(1) 
pygame.init()
size = 200
size = width, height = (size,size)
speed = [1, 1]
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

#print(screen.get_size() )


camera = Camera(FOV=90,location=[0,0,0],pitch=90,yaw=90)# FOV 46.8

world = Scene(active_camera=camera)

#tracer = Tracer(camera, [3,3])#screen.get_size()  )

#init_cubes()
init_obj('Objects/suzanne.obj', [0,5,0])
#init_obj('danny.obj', [0,5,0])
#init_obj('danny.obj', [0,5,3-1])
#init_obj('Objects/text.obj', [0,5,0])



table  = Ray_Table(camera, world, size )# will be the screen resolution

table.trace()

table.display(screen)



pygame.display.flip()
print('done')

def main(): # this is the main loop where everything happens
    print('entering main loop\n\n')
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
    sensitivity = 250
    move_mult = 0.1
    Stop_Watch.frequency = 100
    Stop_Watch.epoch = time()
    while 1:
        if Stop_Watch.loops%Stop_Watch.frequency==1:
            print('total: ',(sum/Stop_Watch.loops)*1000)
            print('.')
            sum = 0
            Stop_Watch.breakpoints.clear()
            Stop_Watch.loops = 1
        delta  = time()-stamp # this thing allows you to track time per frame
        stamp  = time()
        sum += delta
        
        #clock = pygame.time.Clock()
        # Limit to 60 frames per second
        #clock.tick(24)
        i = 0
        for event in pygame.event.get():
            i += 1
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
        Stop_Watch.take_time('flag evaluation')
        #print(i,' events')
        if move_forward:  camera.move(move_mult*+camera.y_vector)
        if move_backward: camera.move(move_mult*-camera.y_vector)
        if move_left:     camera.move(move_mult*-camera.x_vector)
        if move_right:    camera.move(move_mult*+camera.x_vector)
        if move_up:       camera.move([0,0,+move_mult])
        if move_down:     camera.move([0,0,-move_mult])
        if update_rotation:
            pos = pygame.mouse.get_pos()
            size = screen.get_size()
            x = (pos[0]-initial_pos[0]) / size[0]
            y = (pos[1]-initial_pos[1]) / size[1]
            
            camera.set_yaw( x*sensitivity + start_yaw )
            camera.set_pitch( -y*sensitivity + start_pitch )
        
        Stop_Watch.take_time('input evaluation')
        

        Object.x[0].scale_mesh(1.001)

        render(screen, camera)
        Stop_Watch.loops += 1
        Stop_Watch.take_time('end')



#main()
sleep(100000)

















