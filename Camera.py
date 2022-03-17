import numpy as np
from Vector_Math import *
class Camera:
    def __init__(self, FOV=90, location=[0,0,0], pitch=90,yaw=90):
        self.FOV = FOV
        self.HFOV = self.FOV/2 # half FOV
        self.location = np.array(location)
        self.pitch = pitch
        self.yaw = yaw
        self.update_flag = True
        self.update_view_vectors()
        #self.update_cubecull()
    def update_view_vectors(self):
        self.x_vector = polar_to_cartesian(np.array([1, self.yaw+270, self.pitch]))
        self.y_vector = polar_to_cartesian(np.array([1, self.yaw, self.pitch]))
        #self.z_vector = polar_to_cartesian([1, self.yaw, self.pitch])
    def set_yaw(self, yaw):
        self.yaw = yaw
        self.update_view_vectors()
    def set_pitch(self, pitch):
        self.pitch = pitch
        self.update_view_vectors()
    def move(self, vector):
        self.location = self.location + vector
        self.update_flag = True
    def update_cubecull(self):# cube culling discards positive and negative coords based on their relation to the camera angle
        self.cube_mask = np.full(  (2,2,2), False, dtype='bool')
        # positive is culled, negative is kept
        if ( (0<self.yaw<90-self.HFOV) or (270+self.HFOV<self.yaw<360) ): # culls negative x
            self.cube_mask[0,:,:] = True
        if ( 90+self.HFOV<self.yaw<270-self.HFOV ): # culls positive x
            self.cube_mask[1,:,:] = True
        
        if ( self.HFOV<self.yaw<180-self.HFOV ): # culls negative y
            self.cube_mask[:,0,:] = True
        if ( 180+self.HFOV<self.yaw<360-self.HFOV ): # culls negative y
            self.cube_mask[:,1,:] = True#idk
            
        if ( 90+self.HFOV<self.yaw<180 ): # culls negative z 
            self.cube_mask[:,:,0] = True
        if ( 0<self.yaw<90-self.HFOV ): # culls positive z
            self.cube_mask[:,:,1] = True
