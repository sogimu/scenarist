__version__ = "0.11.0-dirty"
from .info import Info
from .utility import getScriptsVariants, chooseScriptVariant, splitTargetCallToNameAndParams
from .runner import executeTargets, getTargets
from .config import bcolors, scriptNameEnding, scriptsDir, global_vars
