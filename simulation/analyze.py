import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("C:/Users/Graham/Desktop/ludobots/data/back leg.npy")
frontLegSensorValues = numpy.load("C:/Users/Graham/Desktop/ludobots/data/front leg.npy")
print(backLegSensorValues)

plt.plot(backLegSensorValues, label = 'Back Leg')
plt.plot(frontLegSensorValues, label = 'Front Leg')
plt.legend()
plt.show()