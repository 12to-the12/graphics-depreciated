from Object import *
from Mesh import *
from numba import jit
points = [
    [[-1, 1,-1],[0,0,0]],
    [[ 1, 1,-1],[0,0,0]],
    [[-1,-1,-1],[0,0,0]],
    [[ 1,-1,-1],[0,0,0]],
    [[-1, 1, 1],[0,0,0]],
    [[ 1, 1, 1],[0,0,0]],
    [[-1,-1, 1],[0,0,0]],
    [[ 1,-1, 1],[0,0,0]]
    ]
polygons = [
    [2,1,0],
    [3,1,2],
    [7,4,5],
    [6,4,7],
    [6,3,2],
    [7,3,6],
    [5,0,1],
    [4,0,5],
    [4,2,0],
    [6,2,4],
    [7,1,3],
    [5,1,7]
    
    ]
mesh = Linked_Mesh(points, polygons)
y = 5
# *2 + 1
x = 5
#15 norm for 1k cubes ~1 ms to project
# 30 yields 61^2 or 29,768 vertices @3 ms projection
z = x
spacing = 4

def init_cubes():
    #Object(mesh, location=[0,5,0])
    
    # 1k  cubes projects in ~50 milliseconds
    for xx in range(-x, x+1):
        if xx%10==0: print(xx)
        for zz in range(-z, z+1):
            for yy in range(-y,y+1):
                Object(mesh, location=[xx*spacing, yy*spacing,zz*spacing])
    
'''
boxa = Object(mesh,location=[-5  ,y,0 ] )
boxb = Object(mesh,location=[-2.5,y,0 ] )
boxc = Object(mesh,location=[0   ,y,0 ] )
boxd = Object(mesh,location=[2.5 ,y,0 ] )
boxe = Object(mesh,location=[5   ,y,0 ] )
'''


meshdata =[
        #tails front
        [[-5,4,0],[-7.5,2,3],[-7.5,4,0]],
        [[-5,-4,0],[-7.5,-4,0],[-7.5,-2,3]],
        [[-5,-4,0],[-7.5,-2,-3],[-7.5,-4,0]],
        [[-5,4,0],[-7.5,4,0],[-7.5,2,-3]],
        #cockpit
        [[1,0,0.45454],[-2,-1,.5],[-2,0,1]],
        [[1,0,0.45454],[-2,0,1],[-2,1,.5]],
        [[-3,0,0.8],[-2,1,.5],[-2,0,1]],
        [[-3,0,0.8],[-2,0,1],[-2,-1,.5]],
        #body front
        [[3.5, 0, 0], [-2, 0, 1], [-2, 2, 0]], 
        [[3.5, 0, 0], [-2, -2, 0], [-2, 0, 1]], 
        #[[-2, 2, 0 ], [-2, 0, 1], [-2, -2, 0]], 
        [[3.5, 0, 0], [-2, 2, 0], [-2, 0, -1]], 
        [[3.5, 0, 0], [-2, 0, -1], [-2, -2, 0]], 
        #[[-2, 2, 0 ], [-2, -2, 0], [-2, 0, -1]]
        #body back
        [[-2, 0, 1],[-2,-2,0],[-9,0,0]],
        [[-2, 0, 1],[-9,0,0],[-2,2,0]],
        
        [[-2, 0, -1],[-9,0,0],[-2,-2,0]],
        [[-2, 0, -1],[-2,2,0],[-9,0,0]],
        
        #wing
        [[0,0,0],[-5,4,0],[-5,0,0]],
        [[0,0,0],[-5,0,0],[-5,-4,0]],
        [[-5,0,0],[-9,0,-0.1],[-5,6,0]],
        [[-5,0,0],[-5,-6,0],[-9,0,-0.1]],
        #wing bottom
        [[0,0,0],[-5,0,0],[-5,4,0]],
        [[0,0,0],[-5,-4,0],[-5,0,0]],
        [[-5,0,0],[-5,6,0],[-9,0,0.1]],
        [[-5,0,0],[-9,0,0.1],[-5,-6,0]],
        #tails inner
        [[-5,4,0],[-7.5,2,-3],[-7.5,4,0]],
        [[-5,-4,0],[-7.5,-4,0],[-7.5,-2,-3]],
        [[-5,-4,0],[-7.5,-2,3],[-7.5,-4,0]],
        [[-5,4,0],[-7.5,4,0],[-7.5,2,3]],
    ]

def init_obj(filename,loc):
    points = []
    pointers = []
    with open(filename) as f:
        for line in f:
            line = line.split()
            if line[0] == 'v':
                points.append([line[1:],[0,0,0]])
            if line[0] == 'f':
                a = line[1]
                b = line[2]
                c = line[3]
                a = a.split('/')[0]
                b = b.split('/')[0]
                c = c.split('/')[0]
                pointers.append([a, b, c])
    points = np.array(points,dtype='float64')
    pointers = np.array(pointers,dtype='int')
    pointers = pointers  # because wavefronts use indexing starting with 1
    #print(pointers)
    #print(points.shape)
    #print(pointers.shape)
    pointers -= 1
    x = pointers.reshape(-1)
    x = np.sort(x)
    #print(x)
    mesh = Linked_Mesh(points, pointers)
    Object(mesh, location = loc)
    
    '''
    suzanne_file = open("suzanne.obj", "r")
    suzanne = suzanne_file.read()
    suzanne_file.close()
    #suzanne = ''.split(suzanne)
    #print('index:', suzanne.index('o Suzanne'))
    index = suzanne.index('o Suzanne')
    suzanne =   suzanne[index:]  
    
    suzanne = suzanne.split('\n')
    print(suzanne)
    print( len(suzanne)) 
    '''
