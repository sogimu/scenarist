# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os
import re

# from scenarist import version

def read(*names, **kwargs):
      with io.open(os.path.join(os.path.dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fp:
            return fp.read()

def find_version(*file_paths):
      version_file = read(*file_paths)
      version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
      if version_match:
            return version_match.group(1)
      raise RuntimeError("Unable to find version string.")

long_description = """
# scenarist.py

[![Build Status](http://sogimu.fvds.ru:8080/buildStatus/icon?job=scenarist.py/Astralinux_1.11)](http://sogimu.fvds.ru:8080/job/scenarist.py/job/Astralinux_1.11/) Astralinux 1.11, master

## Description
Make-like utility to execute platform-dependent scripts (scenarios) written in Python 2.7. Format of scenario-name consist information about platform it written. Scenarios consist of targets.

* **Automatic script (scenario) selection for the current platform**
    File names of scenarios may consists up to three parts joined by '_' (underscore).
    Parts:
    * OS name - mandatory part. It can be Linux or Windows
    * Distrib name - not a mandatory part. It specify distribution name. Example: Ubuntu
    * Distrib version - not a mandatory part. It specify distribution version. Example: 16.04
    Examples of scenarios names:
    * Linux_Ubuntu_16.04.scenario
    * Linux_Ubuntu.scenario
    * Linux.scenario
    Name of scenario gives ability to choose most suitabe scenario for current platform through comparison scenario name and platform properties.

* **Target-body shifting**
    Body of target may shifted to right by tabs of spacies.

* **Target inheritance**
    If calling target not decribed in most suitable scenario for current platform, target will be searched in more general scenario.
    Example: if Linux_Ubuntu_16.04.scenario not consist target 'build' scenarist will try search 'build' in scenario Linux_Ubuntu.scenario.

## To install or upgrade
Pip package page: https://pypi.python.org/pypi/build_scenarist
```
# pip install -U build_scenarist
```

## Example
### Linux.scenario
```python
[install_deps]
run("apt-get update")
run("apt-get -y install git cmake build-essential freeglut3-dev freeglut3 libxmu-dev libxi-dev")

[init]
run("git submodule update --init --recursive")

[build]
if not exists("./build"):
    makedirs("./build")
with cd("./build"):
    run("cmake ..")
    run("make -j 2")

[run_unit-tests]
with cd("./build/tests/"):
    run("./unit-tests/tests")
```
### How use
```bash
scenarist.py run install_deps init build run_unit-tests
```

## Similar utilities
* [dapp](https://github.com/flant/dapp)

"""

setup(name='build_scenarist',
      version=find_version("build_scenarist", "__init__.py"),
      description="Make-like utility to execute platform-dependent scripts (scenarios) written in Python 2.7. Format of scenario-name consist information about platform it written. Scenarios consist of targets",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/sogimu/scenarist',
      author='Aleksandr Lizin',
      author_email='sogimu@nxt.ru',
      license='MIT',
      packages=['build_scenarist'],
      scripts=['scenarist.py'],
      package_data={'build_scenarist': ['src/*']},
      zip_safe=True)
