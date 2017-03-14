# -*- coding: UTF-8 -*-
 
import sys
import argparse
import re
import os
import platform

from subprocess import call
import subprocess
import shlex

from os.path import exists
from os import makedirs

from src.utility import bcolors, cd, run
from src.info import Info

class Runner:
    def __init__(self, scriptsDir):
        self.scriptsDir = scriptsDir
    def targets(self, pathToScript):
        with open(pathToScript) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        # content = [x.strip() for x in content]
        # for i in content:
            # print i

        targetPositions = []
        for i, val in enumerate(content):
            # print i, val
            if bool(re.match("^(\[+.*\]+)$", val)):
                targetPositions.append(i)
        targetPositions
        # print targetPositions

        targets = {}
        fro=0
        to=0
        targetName="None"
        for i, val in enumerate(targetPositions):
            fro = targetPositions[i]+1
            if i+1 < len(targetPositions):
                to = targetPositions[i+1]
            else:
                to = len(content)
            targetName = content[targetPositions[i]][1:-2]
            targetCode = '\n'.join(content[fro:to])
            targets[targetName] = targetCode
        # print targets
        return targets

    def run(self, targets, scriptName):
        if scriptName ==None:
            info = Info()
            scriptName = info.defaultScriptName()
        pathToScript = os.path.join(self.scriptsDir, scriptName)
        print "run targets " + ' '.join(targets) + " from script " + pathToScript

        targetsCode = self.targets(pathToScript)
        for target in targets:
            if target in targetsCode:
                print bcolors.OKGREEN + "\nTarget " + target + " ..." + bcolors.ENDC
                exec(targetsCode[target])
            else:
                print bcolors.WARNING + "Warning: Target " + target + " not found." + bcolors.ENDC

    scriptsDir="./scripts/"