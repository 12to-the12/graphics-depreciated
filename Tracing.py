import numpy as np
import pygame
import numba
import Vector_Math


x = np.array([1,10,100,1000])
y = np.array([5,6,7,8])

a = np.array ( np.meshgrid(x,y, indexing='xy')   )
a = np.dstack(a)


print(a)

class Tracer():
    


    def __init__ (self, camera, res):
        self.camera = camera
        self.res = res
        self.x, self.y = res


    def generate_rays (self):
        pass 
    
    def trace():
        size = width, height = (2000,2000)
        screen = pygame.display.set_mode(size)


