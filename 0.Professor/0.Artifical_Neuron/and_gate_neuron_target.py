from __future__ import print_function
import numpy as np
import random
import math

class GateNeuron:
    def __init__(self):
        self.w = np.array([random.random(), random.random()])   # weight of one input
        self.b = random.random()   # bias
        print("Initial w: {0}, b: {1}".format(self.w, self.b))

    def u(self, input):
        return np.dot(self.w, input) + self.b

    def f(self, u):
        return max(0.0, u)

    def z(self, input):
        u = self.u(input)
        return self.f(u)

    def squared_error(self, input, z_target):
        return 1.0 / 2.0 * math.pow(self.z(input) - z_target, 2)

class Data:
    def __init__(self):
        self.training_input_value = np.array([(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0)])
        self.training_z_target = np.array([0.0, 0.0, 0.0, 1.0])
        self.numTrainData = len(self.training_input_value)

if __name__ == '__main__':
    n = GateNeuron()
    d = Data()
    for idx in xrange(d.numTrainData):
        input = d.training_input_value[idx]
        z = n.z(input)
        z_target = d.training_z_target[idx]
        error = n.squared_error(input, z_target)
        print("x: {0}, z: {1}, z_target: {2}, error: {3}".format(input, z, z_target, error))