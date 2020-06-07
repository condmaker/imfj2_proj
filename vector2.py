# Ficheiro Vector2 pego do professor Diogo Andrade

import math
import random
import numpy as np

class InvalidOperationExceptionVec2(Exception):
    def __init__(self, op, type1, type2):
        self.op = op
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return "Invalid operation (" + self.op + ") between " + str(self.type1) + " and " + str(self.type2)

class vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, v):
        if (isinstance(v, vector2)):
            return vector2(self.x + v.x, self.y + v.y)
        else:
            raise(InvalidOperationExceptionVec2("add", type(self), type(v)))

    def __sub__(self, v):
        if (isinstance(v, vector2)):
            return vector2(self.x - v.x, self.y - v.y)
        else:
            raise(InvalidOperationExceptionVec2("sub", type(self), type(v)))

    def __mul__(self, v):
        if (isinstance(v, (int, float))):
            return vector2(self.x * v, self.y * v)
        else:
            raise(InvalidOperationExceptionVec2("mult", type(self), type(v)))

    def __truediv__(self, v):
        if (isinstance(v, (int, float))):
            return vector2(self.x / v, self.y / v)
        else:
            raise(InvalidOperationExceptionVec2("mult", type(self), type(v)))

    def __eq__(self, v):
        if (isinstance(v, vector2)):
            return (((self - v).magnitude()) < 0.0001)
        else:
            raise(InvalidOperationExceptionVec2("eq", type(self), type(v)))

    def __ne__(self, v):
        if (isinstance(v, vector2)):
            return (((self - v).magnitude()) > 0.0001)
        else:
            raise(InvalidOperationExceptionVec2("neq", type(self), type(v)))

    def __isub__(self, v):
        return self - v

    def __iadd__(self, v):
        return self + v

    def __imul__(self, v):
        return self * v

    def __idiv__(self, v):
        return self / v

    def __neg__(self):
        return vector2(-self.x, -self.y)

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def magnitude_squared(self):
        return self.dot(self)

    def dot(self, v):
        if (isinstance(v, vector2)):
            return self.x * v.x + self.y * v.y
        else:
            raise(InvalidOperationExceptionVec2("dot", type(self), type(v)))

    def normalize(self):
        d = 1.0 / self.magnitude()
        self.x *= d
        self.y *= d

    def normalized(self):
        d = 1.0 / self.magnitude()
        return vector2(self.x * d, self.y * d)

    def to_np2(self):
        return np.array([self.x, self.y])

    def to_np3(self, w = 1):
        return np.array([self.x, self.y, w])

    @staticmethod
    def from_np(np_array):
        return vector2(np_array[0], np_array[1])

def dot_product(v1, v2):
    return v1.dot(v2)