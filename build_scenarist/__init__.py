__version__ = "1.0.1"
from .info import Info
from .utility import getScriptsVariants, chooseScenarioName, splitTargetCallToNameAndParams
from .runner import runTargets
from .config import bcolors, defaultScenarioNameEnding, defaultScenarioDir
