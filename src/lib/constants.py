from pathlib import Path
import matplotlib

DIRS = {'DATA': '../data/', 'IMG': '../img/'}
DIRS['RESULTS'] = DIRS['DATA']+'results/'
DIRS['INPUT'] = DIRS['DATA']+'input/'
DIRS['CONFIGS'] = DIRS['DATA']+'configs/'
for d in DIRS.values():
    Path(d).mkdir(parents=True, exist_ok=True)

# Execution parameters

NUM_EXECUTIONS = 10

matplotlib.rc('xtick', labelsize=14) 
matplotlib.rc('ytick', labelsize=14) 
matplotlib.rc('font', size=14) 
matplotlib.rc('axes', labelsize=14) 
matplotlib.rc('lines', linewidth=3)
