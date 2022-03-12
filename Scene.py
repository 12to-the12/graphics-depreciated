
import numpy as np

class Scene:
    active_scene = None
    def __init__(self):
        Scene.active_scene = self
        # none of these  change during runtime
        self.pointers     = np.array([])#(-1,3)
        self.raw_vertexes = np.array([])#(-1,3) these exist in object space
        self.vertex_normals=np.array([])#(-1,3)
        self.uv_coords    = np.array([])#(-1,2)
        self.face_normals = np.array([])#(-1,3)
        self.origin_list  = np.array([])#(-1,3)

        self.world_update_flag  = True

        self.active_camera = None

    def calc_cam_space(self):# calculates vectors relative to the camera
        if self.world_update_flag:
            self.world_space_vertexes = self.raw_vertexes + self.origin_list
            self.world_update_flag = False
        if self.camera.update_flag: # refers to location only
            self.camera_space_vertexes = self.world_space_vertexes - self.active_camera.location
            self.camera.update_flag = False
    