from os import X_OK
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")




for i in range(6):
    for j in range(6):
        y0 = 0
        length = 1
        width = 1
        height = 1
        z0 = .5
        for k in range(10):
            pyrosim.Send_Cube(name="box", pos=[i, j, z0] , size=[length,width, height])
            z0 += 1
            length *= .9
            height *= .9
            width *=.9
    
pyrosim.End()