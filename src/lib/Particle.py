import numpy as np
import copy

class Particle:
    def __init__(self, x_min, x_max, position=None, velocity=None, objective_value=None):
        self.x_min = x_min
        self.x_max = x_max
        self.position= position
        self.velocity= velocity
        self.objective_value= objective_value
    
    def init_values(self,num_dimensions,objective):
        self.position = np.random.rand(num_dimensions)*(self.x_max-self.x_min)+self.x_min
        self.velocity = np.zeros(num_dimensions)
        self.objective_value=objective.compute(self.position)
        self.best_position = copy.copy(self.position)
        self.best_objective_value = self.objective_value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self,value):
        self._position = value
        if isinstance(value,np.ndarray):
            self._position = np.maximum(self._position,self.x_min)
            self._position = np.minimum(self._position,self.x_max)
        
        
