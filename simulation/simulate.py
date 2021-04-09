import pybullet as p
import time 

p.loadSDF("box.sdf")
physicsClient = p.connect(p.GUI)

for x in range(1000):
    time.sleep(1/30)
    p.stepSimulation()

p.disconnect()