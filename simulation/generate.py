from os import X_OK
import pyrosim.pyrosim as pyrosim

def Create_World():
    return
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [1,1,1])
    pyrosim.Send_Joint(name = 'Torso_Front_Leg', parent = "Torso", child = "Front_Leg", type = "revolute", position = "2 0 1")
    pyrosim.Send_Joint(name = 'Torso_Back_Leg',  parent = "Torso", child = "Back_Leg", type = "revolute", position = "1 0 1")

    pyrosim.Send_Cube(name = "Front_Leg", pos = [.5, 0, -.5], size = [1.0, 1.0 ,1.0])
    pyrosim.Send_Cube(name = "Back_Leg",  pos = [-.5, 0, -.5], size = [1.0, 1.0 ,1.0])
    pyrosim.End()

Create_World()
Create_Robot()

pyrosim.Start_SDF("world.sdf")


#pyrosim.Send_Cube(name = "box", pos = [0, 0, .5], size = [1,1,1])



    
pyrosim.End()