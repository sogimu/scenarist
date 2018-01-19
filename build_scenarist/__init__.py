__version__ = "0.10.1-3-gfedd-dirty"
from .info import Info
from .utility import getScriptsVariants, chooseScriptVariant, splitTargetCallToNameAndParams
from .runner import executeTargets
from .config import bcolors, scriptNameEnding, scriptsDir, global_vars
