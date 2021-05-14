import pybullet as p
import pybullet_data
import time 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)


planeID = p.loadURDF("plane.urdf")
bodyID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for x in range(1000):
    time.sleep(1/30)
    p.stepSimulation()

p.disconnect()