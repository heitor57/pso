import argparse
import yaml
import re
import logging

import lib.utils as utils
from lib.PSO import PSO
from lib.constants import *


config, pso = utils.parameters_init()

logging.basicConfig()
logger = logging.getLogger('default')
logger.setLevel(eval(f"logging.{config['general']['logging_level']}"))
pso.run()
