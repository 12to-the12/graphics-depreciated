import numpy as np

class Mesh:  # parent class,   basically defines geometry
    def __init__(self, polygons):
        self.polygons = polygons 

class Linked_Mesh(Mesh):   # special type of mesh where instead of just having coordinates, the polygons reference a table of coordinates
    
    def __init__(self, points, linked_polygons):
        self.points = np.array( points )
        self.linked_polygons = np.array( linked_polygons )# just references the points
        self.polygons = np.array( self.compile() )
        assert len( self.polygons[0] ) == 3
    def compile(self):
        
        polygons = []
        for polygon in self.linked_polygons: #for every polygon 
            
            a = self.points[ polygon[0]]
            b = self.points[ polygon[1]]
            c = self.points[ polygon[2]]
            
            polygons.append (  [a, b, c])
            
        return polygons

class Wavefront(Linked_Mesh): # don't even touch this mess, it's supposed to read .obj files
    def __init__(self, verts, faces):
        #verts = verts.split('\n')
        #faces = faces.split('\n')
        print(len(verts))
        print(len(faces))
        self.verts = list( map(self.read_verts, verts) )
        self.faces = list( map(self.read_faces, faces) )
        print(len(self.verts))
        print(len(self.faces))
    
        
    def read_verts(self, vert):
        vert = vert[2:]
        vert = vert.split()
        return vert
    def read_faces(self, face):
        face = face[2:]
        face = face.split()
        return face
    def compile(self):
        pass
