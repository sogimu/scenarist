__version__ = "0.9.0-dirty"
from .info import Info
from .utility import getScriptsVariants, chooseScriptVariant, splitTargetCallToNameAndParams
from .runner import executeTargets
from .config import bcolors, scriptNameEnding, scriptsDir, global_vars
