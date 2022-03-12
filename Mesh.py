import numpy as np

class Mesh:  # parent class,   basically defines geometry
    def __init__(self, polygons):
        self.polygons = polygons 

class Linked_Mesh(Mesh):   # special type of mesh where instead of just having coordinates, the polygons reference a table of coordinates
    
    def __init__(self, points, linked_polygons):
        self.points = np.array( points )
        self.linked_polygons = np.array( linked_polygons )# just references the points

