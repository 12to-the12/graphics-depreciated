
import numpy as np

class Scene:
    active_scene = None
    def __init__(self, active_camera=None):
        Scene.active_scene = self
        # none of these  change during runtime
        self.pointers     = np.array([]).reshape(-1,3)
        # the following all have to be the same length
        self.raw_vertexes = np.array([]).reshape(-1,3) #these exist in object space
        self.vertex_normals=np.array([]).reshape(-1,3)
        self.uv_coords    = np.array([]).reshape(-1,2)
        # these may be modified during runtime
        self.vertexes     = np.array([]).reshape(-1,3) #this one is the one actually transformed
        self.face_normals = np.array([]).reshape(-1,3)
        self.origin_list  = np.array([]).reshape(-1,3)

        self.world_update_flag  = True

        self.active_camera = active_camera

    def calc_cam_space(self):# calculates vectors relative to the camera
        if self.world_update_flag:
            self.world_space_vertexes = self.vertexes + self.origin_list
            self.world_update_flag = False
        if self.active_camera.update_flag: # refers to location updates only
            self.camera_space_vertexes = self.world_space_vertexes - self.active_camera.location
            self.active_camera.update_flag = False
        return self.camera_space_vertexes

    # extend happens during build phase, update happens during runtime
    # extend creates the database, update modifies it
    # extends should never be called during runtime
    # updates assume they are operating within the bounds of the existing array
    def extend_pointers(self, x): 
        assert x.shape[1] == 3
        existing = self.raw_vertexes.shape[0] # this is the number of existing vertexes
        x = x + existing # this way the pointers line up correctly
        self.pointers = np.append(self.pointers, x, axis=0)
    
    def extend_raw_vertexes(self, x):
        assert x.shape[1] == 3
        self.raw_vertexes = np.append(self.raw_vertexes, x, axis=0)

    def extend_vertex_normals(self, x): # not needed until we get into phong shading
        assert x.shape[1] == 3
        self.vertex_normals = np.append(self.vertex_normals, x, axis=0)

    def extend_uv_coords(self, x):
        assert x.shape[1] == 3
        self.uv_coords = np.append(self.uv_coords, x, axis=0)

    def extend_origin_list(self, x):
        assert x.shape[1] == 3
        print('adding to origin list')
        self.origin_list = np.append(self.origin_list, x, axis=0)

    def update_vertexes(self, x, start):
        len = x.shape[0]
        self.vertexes[start:start+len] = x

    def update_face_normals(self, x, start):
        len = x.shape[0]
        self.face_normals[start:start+len] = x

    def update_origin_list(self, x, start):
        len = x.shape[0]
        self.origin_list[start:start+len] = x
    
    