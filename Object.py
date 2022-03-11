import numpy as np
import Vector_Math

from Mesh import *
#from Material import *

def vector_add(a,b):
    #print(a)
    #print(b)
    x1, y1, z1 = a
    x2, y2, z2 = b
    x = x1+x2
    y = y1+y2
    z = z1+z2
    return [x, y, z]


            
class Object:
    object_list = []
    object_data = np.array([]).reshape(0,2,3,3)#first dimension separates objects, second separates vertex references,then uv coords, normals, material reference
    raw_vertex_data = np.array([]).reshape(0,2,3)
    vertex_data = np.array([]).reshape(0,2,3) # mutable
    origin_list = np.array([]).reshape(0,3) # one entry for each vertex, not each object, better for quick multiplication
    material_list = []
    def __init__(self, mesh, shader = None, name='untitled', location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], uv_map = None, shadow_map = None):
        self.mesh = mesh
        self.shader = shader
        self.name = name
        self.location = np.array( location )
        
        self.rotation = rotation
        self.scale = scale
        Object.object_list.append(self)
        
        self.vertex_data = self.get_scale(self.scale, self.vertex_data)
        vertex_count = self.mesh.points.shape[0]
        #print(vertex_count)
        Object.origin_list = np.append( Object.origin_list, np.full((vertex_count,3),self.location), axis=0)
        Object.object_data = np.append(Object.object_data, self.compile(), axis = 0 )
        Object.raw_vertex_data = np.append(Object.raw_vertex_data, self.mesh.points,axis=0) 
        Object.vertex_data = np.append(Object.vertex_data, self.mesh.points,axis=0) 
    
    def calc_absolute(): # returns the relative coordinates of the vertex data
        # input is shape (-1,3), vertex_data
        
        assert Object.vertex_data.shape[2]==3
        x = Object.vertex_data[:,0]+Object.origin_list
        return  x # shape = (-1,3)
        
    def calc_relative_to_camera(camera, subject): # returns the relative coordinates of the object data
        # input is shape (-1,3), vertex_data
        assert subject.shape[1:]==(2,3)
        #return mesh - camera
        #print(subject[:,0,:])
        x = subject - camera.location
        return x # shape = (-1,3)
    
    def fetch_vectors(obj_data, v_data): # wtf is my life. ndimensional arrays leave me absolutely in awe, using an array as an indice??!!
        assert 1==2# Logan why are you using this function
        assert obj_data.shape[3]==3
        assert v_data.shape[1]==2
        x = obj_data[:,0,0].reshape(-1).astype('int') # list of vertex positions
        vertices = v_data[:,0]
        d = vertices[x]
        obj_data[:,0] = d.reshape(-1,3,3)
        assert obj_data.shape[3]==3
        #print('obj_data:',obj_data.shape)
        return obj_data
    
    def translate(self, vector): # outdated
        self.location = self.location + vector
        Object.origin_list[self.origin_index:self.vertex_count] = self.location
     
    def global_rotate():
        pass
    
    def translate_origin(self, vector):
            self.vertex_list -= vector

    def get_scale(self, x, vertex_list):
        vertex_list[:,0] = vertex_list[:,0] * x
        return vertex_list
    
    def compile(self):
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



















#
