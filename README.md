# scenarist.py
[![Build Status](http://sogimu.fvds.ru:8080/job/scenarist.py/job/build/badge/icon)](http://sogimu.fvds.ru:8080/job/scenarist.py/job/build/)

Make-подобная утилита для выполнения платформозависимых сценариев на Python 2.7. Сценарии состоят из целей

Страница pip-пакета: https://pypi.python.org/pypi/build_scenarist

### Script have targets like [target_name]. Every target can be run with syntax like
```bash
scenarist run target_name
```

If run scenarist like that:
```bash
scenarist run target_name0 target_name1
```
The Scenarist will choose more sutable script for current platform and run targets ```target_name0``` ```target_name1``` if they exist in the script

# Example
## Targets from script with name Linux.script
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
## Can be run:
### if current platform is Linux
```bash
scenarist run install_deps init build run_unit-tests
```
### or you can specify script manualy
```bash
scenarist run -script Linux.script install_deps init build run_unit-tests
```
