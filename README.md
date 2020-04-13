# scenarist.py

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
### How to use
```bash
scenarist.py run install_deps init build run_unit-tests
```

## Similar utilities
* [dapp](https://github.com/flant/dapp)
