import numpy as np
from numba import jit

@jit(nopython=True)
def _chung_reynolds_function(x):
    r = np.sum(x**2)**2
    return r

class ChungReynoldsFunction:
    def __init__(self):
        self.x_min = -100
        self.x_max = 100
        self.num_dimensions = 30

    def compute(self,x):
        return _chung_reynolds_function(x)
