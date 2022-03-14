import numpy as np
import Vector_Math

from Mesh import *
from Scene import Scene




            
class Object:
    x = np.array([])
    def __init__(self, mesh, shader = None, name='untitled', location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], uv_map = None, shadow_map = None):
        self.mesh = mesh
        self.shader = shader
        self.name = name
        self.location = np.array( location )
        
        self.rotation = rotation
        self.scale = scale
        #Scene.object_list.append(self)
        
        self.vertex_count = self.mesh.points.shape[0]
        self.index = Scene.active_scene.raw_vertexes.shape[0]
        #print(vertex_count)
        self.scene = Scene.active_scene

        Object.x = np.append(Object.x, self)

        self.scene.extend_pointers(self.mesh.linked_polygons)

        #print('self.mesh.points[:,0].shape: ', self.mesh.points[:,0].shape)
        self.scene.extend_raw_vertexes(self.mesh.points[:,0])
        #print('vertex_count: ',vertex_count)
        #print('np.full((vertex_count,3),self.location).shape: ', np.full((vertex_count,3),self.location).shape)
        self.scene.extend_origin_list(  np.full((self.vertex_count,3),self.location)  )
    
    def get_raw_vertexes(self):
        return self.scene.raw_vertexes[self.index:self.index+self.vertex_count]

    def get_vertexes(self):
        return self.scene.vertexes[self.index:self.index+self.vertex_count]

    def scale_mesh(self, factor): # transformations
        scaled = self.get_vertexes() * factor
        self.scene.update_vertexes(scaled, self.index)
    
    def rotate_z(self, rotation):# rotates counter clockwise looking down
        # TODO

        self.scene.update_vertexes(xxxxx, self.index)
        

    def rotate_mesh(self, axis, degrees):
        pass

        

    


























'''
    def compile(self):# I'm going to leave this here as a testament to how shitty this code used to be
        #print('here')
        elements = self.mesh.linked_polygons.shape[0]
        polygon_data = np.zeros((elements,2,3,3))
        polygon_data[:,0,0] = self.mesh.linked_polygons
        
        s = Object.vertex_data.shape[0] # number of vertices in this shape
        polygon_data[:,0] += s # adds the number of vertexes already in the list to each index so it'll correspond to the correct one
        self.origin_index = Object.origin_list.shape[0]-1
        polygon_data[:,1,0] =  self.origin_index# sets the non uv thing to the correct origin index for this object
        # [vert pointers],dummy, dummy  [uv coords] [normal], [barycenter]
        
        
        
        #print('polygon_data:',polygon_data.shape)
        
        return polygon_data
'''



















#
