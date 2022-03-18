



import numpy as np





x = np.array([0,0,0])

v = np.array([0,5,3.9])

c = ([0,5,0])

n = np.array([0,-1,0])

polygon = [ [0,5,4], [-3,5,0], [3,5,0]]
polygon = np.array(polygon)


#(ray_origin, ray_vector, plane_origin, plane_normal)

from Vector_Math import ray_plane_intersection
from Vector_Math import barycentric

i =   ray_plane_intersection( x, v, c, n)


print(i)

jj  = barycentric(polygon, i)

print(jj)



