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

    
def draw_circle(surface, coor, color = pygame.Color('lightblue'), radius=1, line_weight=1):
    pygame.draw.circle(surface, color, coor, radius, line_weight)
    
def wireframe_draw(surface, coordinates, color = pygame.Color('lightblue')): # draws a wireframe polygon
    #pygame.gfxdraw.filled_polygon(surface,coordinates,pygame.Color('darkgrey'))
    pygame.gfxdraw.aapolygon(surface,coordinates,color)



def project(camera, vertex_data): # plots 3d points in 2d
    assert vertex_data.shape[1] == 3
    
    polar = xcartesian_to_polar(vertex_data)
    
    #polar = np.apply_along_axis(cartesian_to_polar, 1, vertex_data )
    
    
    Stop_Watch.take_time('project')
    
    polar = polar[:,1:] # this line discards the magnitude
    
    #print(polar)
    
    camera_direction = np.array( [camera.yaw, camera.pitch] )
    assert 0<=camera.yaw<360
    assert 0<=camera.pitch<360
    #print()
    relative = polar-camera_direction
    #print(relative.reshape(-1,3,2))
    #print(camera.HFOV)
    fractional = relative/camera.HFOV
    fractional[:,0] = fractional[:,0]*-1 # inverts the yaw because for some reason it's necessary
    #print(fractional)
    return fractional


    
def clip_outside(projected):  # incomplete
    a = (-0.5<a[0]<0.5) & (-0.5<a[0]<0.5)

def screensize(surface, coords):# changes fractional coordinates to actual pixel numbers
    assert coords.shape[1] == 2
    coords = coords.reshape(-1,2)
    width, height = surface.get_size()
    coords += 1
    coords /= 2
    coords[:,0] *= width
    coords[:,1] *= height# this doesn't method avoids distortion
    return coords

def sort_vertices(vertex_list):# takes an indexed list and sorts it
    # take shape (-1,4)
    pass
    
def build_polygons(vertices, pointers): # this also checks for missing and discards the polygons if they're not all there
    surviving = vertices[:,3].astype('int')
    print('surviving indexes:', surviving)
    #object_data = object_data[:,0]
    #present = np.any(object_data,axis=1,where =(object_data[:,0] in surviving_vertices) )
    print(surviving.shape)
    print(pointers.shape)
    print(pointers)
    #pointers = pointers.reshape(-1)
    in_list =  np.isin(pointers, surviving)#.reshape(-1,3)
    print('if the pointers in the list:', pointers)
    polygons = np.any(in_list, axis=1   )
    #polygons = (polygons in surviving)
    print()
    print('any:',polygons)
    #print(polygons.shape)
    print(pointers[polygons].shape)
    #assert polygons.shape[1:] == (3, 3)
    #np.isin(object_data, surviving_vertices)
    print(in_list)

def render(surface, camera, Obj):
    # the best way to organize the data is just to have a massive list of all the object data that can be culled and sorted each run, lots of references to immutable data too, like textures
    #  [     [[verts](referencing verts), [uvcoords], normal, barycenter]
    Stop_Watch.take_time('starting render')
    
    
    absolute = Obj.calc_absolute() # converts object local coordinates to world coordinates
    
    Stop_Watch.take_time('absolute') # the class not the module
    
    #print('absolute:',absolute)
    if camera.update_flag:
        absolute  = Obj.calc_relative_to_camera(camera.location, absolute)
    
    # here we have the relative vertex data
    x = np.arange(absolute.shape[0]).reshape(-1,1) # basically a list of each index along absolute
    indexed_vertices = np.append(absolute, x, axis=1 ) # list of vertices with their index
    
    
    # we don't need to map vertexes that are occluded, ones facing away, or ones not within the cubic frustrum
    
    # so actually implement that stuff
    # TODO cube frustrum cull
    # TODO distance cull
    #x = cube_cull(camera, indexed_vertices)
    #quit()
    #x = distance_cull(x, distance=20)
    np.TooHardError
    
    projected = project(camera, absolute) # returns -0.5 to 0.5  takes list of vertexes (-1,3), returns list of coordinates(-1,2)
    
    Stop_Watch.take_time('post project')
    #print(projected)
    indexed_vertices = indexed_vertices[0:1]
    #print(indexed_vertices)
    #print(Obj.object_data[:,0,0])
    #print(Obj.object_data)
    # at this point they're still just pointers
    #polygons = build_polygons(indexed_vertices, Obj.object_data[:,0,0]) #(-1,4) & (-1,3)
    # TODO clip if all points are outside
    
    #print(projected.shape)
    
    #clipped_verts = clip_outside(projected)
    
    
    #print(clipped_verts)
    
        
    # TODO cull backfaces
    #culled = cull_backfaces(clipped)
    scaled = screensize(surface, projected)
    Stop_Watch.take_time('scale')
    scaled = scaled.reshape(-1,2)
    
    for a in scaled:
        #print('a:',a)
        pass
        draw_circle(surface, a)
        #wireframe_draw(surface, a)
    '''
    for a in scaled.reshape(-1,3,3):
        wireframe_draw(surface, a)
    '''
    Stop_Watch.take_time('draw')
    epoch = time()
    
    # should now only include faces that will show up and are facing the camera
    
    # TODO sort by barycenter distance for occlusion
    #
    # TODO shade
    
    # TODO draw
    
    

            
            




























#
