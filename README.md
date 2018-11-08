# scenarist.py

[![Build Status](http://sogimu.fvds.ru:8080/buildStatus/icon?job=scenarist.py/Astralinux_1.11)](http://sogimu.fvds.ru:8080/job/scenarist.py/job/Astralinux_1.11/) Astralinux 1.11, master

Make-подобная утилита для выполнения платформозависимых сценариев на Python 2.7. Сценарии состоят из целей

Страница pip-пакета: https://pypi.python.org/pypi/build_scenarist
## Для установки или обновления
```
# pip install -U build_scenarist
```

## Похожие утилиты
* [dapp](https://github.com/flant/dapp)

### Scenario have targets like [target_name]. Every target can be run with syntax like
```bash
scenarist run target_name
```

If run scenarist like that:
```bash
scenarist run target_name0 target_name1
```
The Scenarist will choose more sutable scenario for current platform and run targets ```target_name0``` ```target_name1``` if they exist in the scenario

# Example
## Targets from scenario with name Linux.scenario
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
