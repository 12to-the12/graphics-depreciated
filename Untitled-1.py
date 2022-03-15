



import numpy as np

n = np.array([0,1,0])

v = np.array([0,0,0])

x = np.array([0,2,1])

c = ([-2,0,0])

w = c - x


k = np.dot(w, n) / np.dot(v, n)

from Vector_Math import ray_plane_intersection

print(  ray_plane_intersection( x, v, c, n))