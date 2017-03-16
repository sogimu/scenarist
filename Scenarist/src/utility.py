# -*- coding: UTF-8 -*-
 
import sys
import argparse
import re
import os
import platform

from subprocess import call
import subprocess
import shlex

from os.path import exists, isfile, join
from os import makedirs, listdir

from Scenarist.src.config import scriptNameEnding, bcolors

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        try:
            os.chdir(self.newPath)
        except OSError:
            raise Exception(bcolors.FAIL + "Path: {0}. No such file or directory!".format(self.newPath) + bcolors.ENDC)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def run(cmd):
    print bcolors.BOLD + "> " + cmd + bcolors.ENDC
    subprocess.call(shlex.split(cmd))

def chooseScriptVariant(systemName, scriptsNames):
    sizeOfMatch = {}
    for scriptsName in scriptsNames:
        match = re.match("^(" + scriptsName + ")", systemName)
        if bool(match):
            sizeOfMatch[scriptsName]=len(match.group())
    if len(sizeOfMatch) == 0:
        return None
    return max(sizeOfMatch, key=sizeOfMatch.get)

def getScriptsVariants(scriptsDir):
    onlyfiles = [f for f in listdir(scriptsDir) if isfile(join(scriptsDir, f))]
    scriptsNames = []
    for fileName in onlyfiles:
        match = re.match("^(.*" + scriptNameEnding + ")$", fileName)
        if bool(match):
            scriptsNames.append(fileName[:-1 * len(scriptNameEnding)])
    return scriptsNames