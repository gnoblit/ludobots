import pybullet as p
import time 

physicsClient = p.connect(p.GUI)

for x in range(1000):
    time.sleep(1/30)
    p.stepSimulation()

p.disconnect()