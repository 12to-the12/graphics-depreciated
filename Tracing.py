import numpy as np
import pygame
import numba
from Vector_Math import polar_to_cartesian
from Camera import Camera


#x = np.array([1,10,100,1000])
#y = np.array([5,6,7,8])

#a = np.array ( np.meshgrid(x,y, indexing='xy')   )
#a = np.dstack(a)


#print(a)

class Tracer():
    


    def __init__ (self, camera, res):
        self.camera = camera
        self.res = res
        self.xres, self.yres = res # the number of rays to cast horizontally and vertically
        print('created a tracer')
        self.polar_coords = self.generate_polar_rays() # this generates the coordinates of the points in polar rays
        print(self.polar_coords)

    def generate_polar_rays (self):
        pass
        #np.apply_along_axis  polar_to_cartesian 
        xdelta = self.camera.FOV / self.xres
        multiplier = np.arange(0,self.xres) # thing to multiply the x width by
        xpolar = ( ( (multiplier * xdelta)   ) + ( 0.5 * xdelta) + self.camera.yaw )  - self.camera.HFOV

        ydelta = self.camera.FOV / self.yres
        multiplier = np.arange(0,self.yres) # thing to multiply the x width by
        ypolar = ( ( (multiplier * ydelta)   ) + ( 0.5 * ydelta) + self.camera.pitch )  - self.camera.HFOV

        polar_coords = np.meshgrid(xpolar, ypolar, indexing='xy')

        polar_coords = np.dstack( polar_coords ).reshape(-1,2)

        magnitude = np.ones( polar_coords.shape[0]  ).reshape(-1,1)
        polar_coords = np.append(magnitude, polar_coords, axis=1)



        return polar_coords # in the format ( magnitude, yaw, pitch)


        #cartesian = np.apply_along_axis( polar_to_cartesian,  0, polarcoords)

    
    def trace():
        image = np.apply_along_axis(self.trace_ray, 0, self.pixel_vectors):
        


camera = Camera(FOV=90,location=[0,0,0],pitch=90,yaw=90)# FOV 46.8

tracer = Tracer(camera, [3,3])#screen.get_size()  )

