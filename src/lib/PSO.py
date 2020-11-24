import numpy as np
import pandas as pd
import yaml
from tqdm import tqdm
import logging

import math
import random
import argparse
import collections
import sys
from pathlib import Path
import os
import copy
import re

from lib.constants import *

import lib.utils as utils
import lib.objectives as objectives
from lib.Particle import Particle

class PSO:
    def __init__(self, w, c_1, c_2,num_particles,num_iterations, objective_name, eid):
        self.w = w
        self.c_1 = c_1
        self.c_2 = c_2
        self.num_iterations = num_iterations
        self.objective_name = objective_name
        self.num_particles = num_particles
        self.eid = eid

    def run(self):
        objective = eval(f"objectives.{self.objective_name}()")
        self.x_min= objective.x_min
        self.x_max= objective.x_max
        self.num_dimensions = objective.num_dimensions
        particles = []
        for i in range(self.num_particles):
            particles.append(Particle(objective.x_min,objective.x_max))
            particles[-1].init_values(self.num_dimensions,objective)
        
        global_best_particle = np.argmin([p.objective_value for p in particles])
        
        columns = ['#Iterations','Best global fitness','Best fitness','Mean fitness', 'Median fitness', 'Worst fitness']
        df = pd.DataFrame([],columns = columns)
        df = df.set_index(columns[0])

        logger = logging.getLogger('default')
        if logger.level <= logging.INFO:
            progress_bar = tqdm
        else:
            progress_bar = lambda x: x
            
        for i in progress_bar(range(1,self.num_iterations+1)):
            for j, particle in enumerate(particles):
                r_1 = np.random.rand(self.num_dimensions)
                r_2 = np.random.rand(self.num_dimensions)
                particle.velocity=self.w*particle.velocity+\
                    self.c_1*r_1*(particle.best_position - particle.position)+\
                    self.c_2*r_2*(particles[global_best_particle].best_position - particle.position)
                particle.position = particle.position + particle.velocity
                particle.objective_value = objective.compute(particle.position)

                if particle.objective_value < particle.best_objective_value:
                    particle.best_objective_value = particle.objective_value
                    particle.best_position = particle.position
                    if particle.objective_value < particles[global_best_particle].best_objective_value:
                        global_best_particle = j
            
            objective_values = [p.objective_value for p in particles]
            df.loc[i] = [f'{particles[global_best_particle].best_objective_value:.4E}',f'{np.min(objective_values):.4E}',f'{np.mean(objective_values):.4E}',f'{np.median(objective_values):.4E}',f'{np.max(objective_values):.4E}']

        logger.info(f"\n{df}")
        self.save_results(df)

    def __str__(self):
        string=""
        for k, v in self.__dict__.items():
            string+=f"{k} = {v}\n"
        return string

    def get_name(self):
        name = f"{DIRS['RESULTS']}"+utils.get_parameters_name(self.__dict__,num_dirs=3)+".json"
        l = name.split('/')
        for i in range(2,len(l)):
            directory = '/'.join(l[:i])
            logger = logging.getLogger('default')
            logger.debug(directory)
            Path(directory).mkdir(parents=True, exist_ok=True)
        return name

    def save_results(self, df):
        f = open(self.get_name(),'w')
        f.write(df.to_json(orient='records',lines=False))
        f.close()

    def load_results(self):
        string = self.get_name()
        return pd.read_json(string)
