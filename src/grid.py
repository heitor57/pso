import os
from concurrent.futures import ProcessPoolExecutor
import itertools

import numpy as np

from lib.constants import *
from lib.utils import *

# parameters = {
#     "AntSystem_rho": [0.3,0.5,0.7],
#     "AntSystem_Q": [75, 100, 125],
#     "selection_beta": [3,5,7],
#     "instance_name": ['lau15','sgb128'],
#     "eid": list(range(1,NUM_EXECUTIONS+1)),
# }
# parameters_names = list(parameters.keys())
# combinations = itertools.product(*list(parameters.values()))
args = [(f'python pso.py -c {DIRS["CONFIGS"]}{entry.name}',)
        for entry in os.scandir(DIRS['CONFIGS'])]
# print(args)
run_parallel(os.system,args,chunksize=20)
