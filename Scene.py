
import numpy as np

class Scene:
    # none of these  change during runtime
    pointers     = np.array([])#(-1,3)
    raw_vertexes = np.array([])#(-1,3) these exist in object space
    vertex_normals=np.array([])#(-1,3)
    uv_coords    = np.array([])#(-1,2)
    face_normals = np.array([])#(-1,3)
    origin_list  = np.array([])#(-1,3)

    world_update_flag  = True

    active_camera = None

def calc_cam_space():# calculates vectors relative to the camera
    if Scene.world_update_flag:
        Scene.world_space_vertexes = Scene.raw_vertexes + Scene.origin_list
        Scene.world_update_flag = False
    if Scene.camera.update_flag: # refers to location only
        Scene.camera_space_vertexes = Scene.world_space_vertexes - Scene.active_camera.location
        Scene.camera.update_flag = False
    