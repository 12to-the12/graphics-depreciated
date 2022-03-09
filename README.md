# Graphics
this is my attempt at making a graphics program

ok, so the main file is where everything is coordinated from, the game loop resides there and subcontracts shit

the rendering file is responsible for turning all the geometry into two dimensional images, it's called from the game loop

the vector_math file is referenced by the rendering file and is responsible for doing all the damn vector math, like difference between two vectors

the camera, object mesh and  material  files contain their respective classes

the objects file actually builds some objects, a grid of cubs currently
