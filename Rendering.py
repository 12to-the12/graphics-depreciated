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
    
    pygame.gfxdraw.aapolygon(surface,coordinates,color)
    #pygame.gfxdraw.filled_polygon(surface,coordinates,pygame.Color('darkgrey'))



def project(camera, vertex_data): # plots 3d points in 2d
    assert vertex_data.shape[1] == 3
    
    polar = xcartesian_to_polar(vertex_data)
    #print('polar:',polar)
    #polar = np.apply_along_axis(cartesian_to_polar, 1, vertex_data )
    

    Stop_Watch.take_time('project')
    
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


    
def clip_outside(projected):  # incomplete
    a = (-0.5<a[0]<0.5) & (-0.5<a[0]<0.5)

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

def transfer_pointers(pointers): # takes pointers and transfers the indexes to the surviving polygons
    pass

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
def filter_pointers(surviving, pointers):#
    mask = np.isin(pointers,surviving)
    mask = mask.reshape(-1,3)
    any = np.any(mask, axis=0)

    
def build_polygons(coords, source_vertices, indexed_vertices, object_data): # this also checks for missing and discards the polygons if they're not all there
    surviving = indexed_vertices[:,3].astype('int')
    pointers = object_data[:, 0,0].reshape(-1,1).astype('int')
    # TODO filtered_pointers = filter_pointers(surviving, pointers)
    filtered_pointers = pointers
    source_vertices = source_vertices.reshape(-1,3)
    polygons = source_vertices[filtered_pointers]
    polygons = polygons.reshape(-1,3,3)
    #print(polygons.shape)
    #print('object data',object_data[:,0].shape)
    

    object_data[:, 0] = polygons
    return object_data




    quit()

def draw_polygons(surface, built):
    for a in built:
        wireframe_draw(surface, a)


def render(surface, camera, Obj):
    # the best way to organize the data is just to have a massive list of all the object data that can be culled and sorted each run, lots of references to immutable data too, like textures
    #  [     [[verts](referencing verts), [uvcoords], normal, barycenter]
    Stop_Watch.take_time('starting render')
    
    if camera.update_flag:
        #print('updating...')
        Obj.vertex_data  = Obj.calc_relative_to_camera(camera, Obj.raw_vertex_data)
        camera.update_flag = False

    absolute = Obj.calc_absolute() # converts object local coordinates to world coordinates
    #print(absolute)
    Stop_Watch.take_time('absolute') # the class not the module
    
    #print('absolute:',absolute)
    
    
    # here we have the relative vertex data
    x = np.arange(absolute.shape[0]).reshape(-1,1) # basically a list of each index along absolute
    indexed_vertices = np.append(absolute, x, axis=1 ) # list of vertices with their index
    #print('indexed vertices',indexed_vertices.shape)
    # we don't need to map vertexes that are occluded, ones facing away, or ones not within the cubic frustrum
    
    # so actually implement that stuff
    # TODO cube frustrum cull
    # TODO distance cull
    #x = cube_cull(camera, indexed_vertices)
    #quit()
    #x = distance_cull(x, distance=20)
    
    projected = project(camera, absolute) # returns -0.5 to 0.5  takes list of vertexes (-1,3), returns list of coordinates(-1,2)
    
    Stop_Watch.take_time('post project')
    scaled = screensize(surface, projected)
    # at this point they're still just pointers
    #coords, polygons = build_polygons(scaled, absolute,indexed_vertices, Obj.object_data) #returns the 3d coords

    # TODO clip if all points are outside
    built = build_coords(scaled, Obj.object_data[:,0,0])
    #print(built)
    
        
    # TODO cull backfaces
    #culled = cull_backfaces(clipped)
    
    
    '''
    scaled = scaled.reshape(-1,2)
    for a in scaled:
        #print('a:',a)
        pass
        draw_circle(surface, a)
        #wireframe_draw(surface, a)
    '''
    #print('built',built)
    #print('xxxxxxxxxxxxx')
    
    Stop_Watch.take_time('draw')
    epoch = time()
    
    draw_polygons(surface, built)
    # should now only include faces that will show up and are facing the camera
    
    # TODO sort by barycenter distance for occlusion
    #
    # TODO shade
    
    # TODO draw
    
    

            
            




























#
