import math
from msilib.schema import Error
import numpy as np
from math import sin, cos, tan
from math import acos, atan
from math import degrees, radians
import time

from pandas import array
from Stop_Watch import *
from numba import jit
def clean(x):
    return round(x*1000)/1000
def barycenter(polygon): # returns the center of the polygon, useful for the painter's algorithm
    a, b, c = polygon
    x1, y1, z1 = a
    x2, y2, z2 = b
    x3, y3, z3 = c
    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3
    z = (z1 + z2 + z3) / 3
    return (x, y, z)


def hypotenuse(coor):
    x, y = coor
    x = abs(x)
    y = abs(y)
    return math.sqrt( x**2 + y**2)

def magnitude(vector_list): # operates on array of vectors
    #print( vector_list.shape )
    assert vector_list.shape[1] == 3
    return np.linalg.norm(vector_list,axis=1)
    
    
def normalize(vector_list): # operates on array of vectors
    assert vector_list.shape[1] == 3
    mag_list = magnitude(vector_list)
    return vector_list / mag_list[:,None]

@jit(nopython=True, parallel=True)
def xcartesian_to_polar(vertex_list):# works
    # yaw starts from positive x, counter clockwise
    # pitch starts from positive z, moves down from there
    
    x = vertex_list[:,0]
    y = vertex_list[:,1]
    z = vertex_list[:,2]

    #r = magnitude(vertex_list)
    r = np.sqrt((x**2 + y**2 + z**2))
    yaw = np.arctan2(y, x,) # smart arctan works for any angle
    yaw = np.where(yaw<0, np.deg2rad(360)+yaw, yaw) # adds to negative
    pitch = np.arccos(z/r)

    r = r.reshape(-1,1)
    yaw = np.rad2deg(yaw).reshape(-1,1)
    pitch = np.rad2deg(pitch).reshape(-1,1)
    polar = np.concatenate( (r, yaw, pitch), axis=1 )
    return polar


def cartesian_to_polar(vector): # starts from positive x, counter clockwise
    #stamp = time.time()
    x, y, z = vector
    r = magnitude(vector)
    try: theta = atan(y/x)#doesnt work if x is zero, means point is on y-z plane
    except: 
        if y>0: theta = radians(90)
        elif y<0: theta = radians(270)
        else: theta = 0
    
    hyp = hypotenuse( (x,y) )
    #phi = acos(z/r)) used instead if we want the angle from the z axis instead of the xy plane
    try: phi = acos(z/r)#phi = atan(hyp / z)
    except: phi = 0
    
    theta = degrees(theta)
    if x<0: theta += 180
    phi = degrees(phi)
    return (r, theta, phi)


def polar_to_cartesian(vector):# only operates on single vector
    assert type(vector) is type(np.array([]))
    # operates on degrees not radians
    # this took hours jesus, now it's outdated
    r, theta, phi = vector
    theta %= 360
    phi %= 360
    assert theta>=0 # you know what you have to do
    assert phi>0
    #if theta <0: theta += 180
    theta = radians(theta)
    phi = radians(phi)
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)
    x = round(x, 5)
    y = round(y, 5)
    z = round(z, 5)
    return np.array([x, y, z]) 
    
    
def normal_vector(polygon_list): # finds the normal of a list of polygons
    # takes an array of shape(-1,3,3)
    p1 = polygon_list[:,0]
    p2 = polygon_list[:,1]
    p3 = polygon_list[:,2]
    normals = np.cross(p2-p1, p3-p1)
    normals = normalize(normals)
    return normals


def dot_product(a, b): #return np.multiply(a, b).sum(1)
    # takes two (-1,3) shaped lists and returns a one dimensional list
    assert a.shape[0] == 3
    assert b.shape[0] == 3
    
    return np.einsum('ij, ij->i', a, b)

def angle(a, b):# finds the angle between two (lists of) vectors
    # takes two (-1,3) shaped lists and returns a one dimensional list
    assert a.shape[0] == 3
    assert b.shape[0] == 3
    
    a = normalize(a)
    b = normalize(b)
    dot = dot_product(a, b)
    angle = np.arccos( dot )
    return angle*57.295779513


def ray_plane_intersection(ray_origin, ray_vector, plane_origin, plane_normal):
    # this operates on one vector at a time
    # keep in mind the ray vector does not have to be normalized
    w = plane_origin - ray_origin # from the ray origin to the plane origin
    magnitude = np.dot(w, plane_normal) / np.dot(ray_vector, plane_normal)
    # error if there is no ray vector or plane normal, which is to be expected
    if magnitude < 0: return None # there is no intersection
    elif magnitude == 0: assert 0==1 #the point lies on the surface
    else: return  ray_origin + magnitude*ray_vector # there is an intersection

def project( original, target):
    numerator = np.dot(original, target)
    denominator = np.dot(target, target)
    return (numerator / denominator) * target

def barycentric(polygon, point):
    # https://www.youtube.com/watch?v=EZXz-uPyCyA
    # calculates from cartesian worldspace to barycenteric coordinates for point
    # assumes every point lies on the same plane
    I = point
    A, B, C = polygon # the three corners of the polygon
    
    CB = B - C
    AB = B - A

    v = AB - project(AB, CB)
    

    AI = I - A

    numerator = np.dot( v, AI )
    denominator = np.dot( v, AB )
    a = 1 - (numerator / denominator )

    

    AC = C - A
    BC = C - B
    v = BC - project(BC, AC)
    BI = I - B

    numerator = np.dot( v, BI )
    denominator = np.dot( v, BC )

    b = 1 - (numerator / denominator )

    

    BA = A - B
    CA = A - C
    v = CA - project(CA, BA)
    CI = I - C

    numerator = np.dot( v, CI )
    denominator = np.dot( v, CA )

    c = 1 - (numerator / denominator)

    

    a = round(a, 5)
    b = round(b, 5)
    c = round(c, 5)

    return  (0<a<1) and (0<b<1) and (0<c<1) # things on the edge don't count as landed


































#
