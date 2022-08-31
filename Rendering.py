from cmath import nan
import sys, pygame
from pygame import gfxdraw

from time import sleep
from time import time
import numpy as np
import math
from math import tan
from math import degrees
from Vector_Math import *
from Stop_Watch import *
from Scene import Scene

    
def draw_point(surface, coor, color = pygame.Color('lightblue'), radius=5, line_weight=1):
    pygame.draw.circle(surface, color, coor, radius, line_weight)

def draw_points(surface, coordinates):
    for x in coordinates:
        draw_point(surface, x)
    

def wireframe_draw(surface, coordinates, color = pygame.Color('lightblue')): # draws a wireframe polygon
    pygame.gfxdraw.aapolygon(surface,coordinates,color)
    #pygame.gfxdraw.filled_polygon(surface,coordinates,pygame.Color('darkgrey'))

def draw_polygons(surface, built):
    for x in built:
        wireframe_draw(surface, x)







def project(camera, vertex_data): # plots 3d points in 2d
    assert vertex_data.shape[1] == 3
    
    polar = xcartesian_to_polar(vertex_data)
    #print('polar:',polar)
    #polar = np.apply_along_axis(cartesian_to_polar, 1, vertex_data )
    

    Stop_Watch.take_time('projection')

    polar = polar[:,1:] # this line discards the magnitude
    
    
    #print(polar)
    
    camera_direction = np.array( [camera.yaw, camera.pitch] )
    #print('camera direction:',camera_direction )
    camera.yaw %= 360
    assert 0<=camera.yaw<360
    assert 0<=camera.pitch<360
    #print()
    relative = polar-camera_direction
    #print(relative.reshape(-1,3,2))
    #print(camera.HFOV)
    fractional = relative/camera.HFOV
    #fractional[:,0] = fractional[:,0]*-1
    #fractional[:,1] = fractional[:,1]*-1 # inverts the yaw because for some reason it's necessary
    #print(fractional)
    return fractional

def cull_offscreen(vertex_list):
    onscreen = np.where(-1<vertex_list, np.where(vertex_list<1, nan), nan)
    any = np.any(onscreen)
    return np.where()
    

def screensize(surface, coords):# changes fractional coordinates to actual pixel numbers
    assert coords.shape[1] == 2
    coords = coords.reshape(-1,2)
    width, height = surface.get_size()
    coords[:,0] *= -1
    coords += 1
    coords /= 2
    coords[:,0] *= width
    coords[:,1] *= height# this method doesn't avoid distortion
    return coords



def build_coords(projected, pointers): #this assumes all vertices are present and none have been culled
        assert pointers.shape[1] == 3
        assert projected.shape[1] == 2
        #print('projected:',projected.shape)
        #print('pointers:',pointers.shape)
        projected = projected.reshape(-1,2)
        pointers = pointers.reshape(-1,1).astype('int')
        try: built = projected[pointers]
        except:
            for x in pointers:
                pass
                #print(x)
            assert 1==2

        #print('built:',built.shape)
        built = built.reshape(-1,3,2)
        #print('rebuilt:',built.shape)
        return built




def render(surface, camera):
    surface.fill((0, 0, 0))

    scene = Scene.active_scene
    camera_space_vertexes = scene.calc_cam_space()

    

    # we don't need to map vertexes that are occluded, or ones facing away
    
    # TODO distance cull
    ##Stop_Watch.take_time('relativity')
    projected = project(camera, camera_space_vertexes) # returns -0.5 to 0.5  takes list of vertexes (-1,3), returns list of coordinates(-1,2)
    
    ##Stop_Watch.take_time('post projection')

    #projected = cull_offscreen(projected)
    scaled = screensize(surface, projected)

    # TODO clip if all points are outside
    built = build_coords(scaled, scene.pointers)
    
    # TODO cull backfaces
    ##Stop_Watch.take_time('building')
    #draw_points(surface, built.reshape(-1,2))
    #print('built:',built.shape[0])
    draw_polygons(surface, built)

    ##Stop_Watch.take_time('drawing')

    pygame.display.flip()
    
    

            
            





























