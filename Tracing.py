import numpy as np
from numba import jit
from Vector_Math import polar_to_cartesian
from Vector_Math import ray_plane_intersection
from Vector_Math import barycentric
from Camera import Camera
from Scene import Scene
import pygame


#x = np.array([1,10,100,1000])
#y = np.array([5,6,7,8])

#a = np.array ( np.meshgrid(x,y, indexing='xy')   )
#a = np.dstack(a)


#print(a)



class Ray():
    def __init__ (self, origin, ray, scene, bounces=0):
        self.origin = origin
        self.ray = ray
        self.scene = scene
        self.bounces = bounces

        
    
    def trace(self):
        polygon = [ [0,5,-3], [-3,5,0], [3,5,0]]
        polygon = np.array(polygon)
        plane_origin = np.array([0,5,0])
        plane_normal = np.array([0,-1,0])
        if self.intersection(polygon, plane_origin,  plane_normal):
            return [0,255,0]
        else:
            return [0,0,255]

    def intersection(self, polygon, polygon_origin, polygon_normal): # checks whether or not the ray intersects a given polygon
        intersection_coor = ray_plane_intersection(self.origin, self.ray, polygon_origin, polygon_normal) # the point where the ray and polygon plane intersect
        if intersection_coor.any() == None: return False
        intersect = barycentric(polygon, intersection_coor) # whether or not the point is within the polygon
        if intersect: return True


class Ray_Table():

    def __init__ (self, camera, scene, res):
        self.camera = camera
        self.scene = scene
        self.res = res
        self.xres, self.yres = res # the number of rays to cast horizontally and vertically

        print('created a table')
        self.rays = self.generate_camera_rays() # this generates the coordinates of the points in polar rays
        self.rays = np.flip(self.rays, 1)

    def generate_camera_rays (self):
        #np.apply_along_axis  polar_to_cartesian 
        xdelta = self.camera.FOV / self.xres
        multiplier = np.arange(0,self.xres) # thing to multiply the x width by
        #multiplier = np.flip(multiplier)
        xpolar = ( ( (multiplier * xdelta)   ) + ( 0.5 * xdelta) + self.camera.yaw )  - self.camera.HFOV

        ydelta = self.camera.FOV / self.yres
        multiplier = np.arange(0,self.yres) # thing to multiply the x width by
        #multiplier = multiplier.flip()
        ypolar = ( ( (multiplier * ydelta)   ) + ( 0.5 * ydelta) + self.camera.pitch )  - self.camera.HFOV

        polar_coords = np.meshgrid(xpolar, ypolar, indexing='xy')

        polar_coords = np.dstack( polar_coords ).reshape(-1,2)

        magnitude = np.ones( polar_coords.shape[0]  ).reshape(-1,1)
        polar_coords = np.append(magnitude, polar_coords, axis=1)

        rays = np.apply_along_axis( polar_to_cartesian, 1, polar_coords)



        return rays # in the format ( magnitude, yaw, pitch)


        #cartesian = np.apply_along_axis( polar_to_cartesian,  0, polarcoords)

    #@jit(nopython=True)
    def trace(self):
        print('starting trace')
        image = np.array([])
        for count, ray in enumerate(self.rays):
            if count%1000==0:print(f"{count:>5}" ) 
            x = Ray([0,0,0], ray, self.scene)

            image = np.append(image,  x.trace() )
        image = image.reshape( self.xres, self.yres, 3)
        self.image = image
        print('finished trace')
    
    def display(self, surface):
        
        surf = pygame.surfarray.make_surface(self.image)

        surface.blit(surf, (0, 0))

