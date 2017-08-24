#!/bin/bash -x
hasPython2=$(dpkg --get-selections | grep -c -e "^python2.7\s.")
hasPythonSetuptools=$(dpkg --get-selections | grep -c -e "^python-setuptools\s.")
hasPipPackage=$(dpkg --get-selections | grep -c -e "^python-pip\s.")
hasPip=$(which pip | grep -c pip)
hasScenarist=$(pip freeze | grep -c build-scenarist)

if [ "$hasPython2" == 0 ]; then
    echo "Packge Python2 installing ..."
    apt-get -y install python2.7
fi

if [ "$hasPythonSetuptools" == 0 ]; then
    echo "Packge python-setuptools installing ..."
    apt-get -y install python-setuptools
fi

if [ "$hasPip" == 0 ]; then
    if [ "$hasPipPackage" == 0 ]; then
        echo "Packge python-pip installing ..."
        apt-get -y install python-pip
    else
        echo "Utility pip installing ..."
        easy_install pip
    fi
fi

if [ "$hasScenarist" == 0 ]; then
    echo "Utility build_scenarist installing ..."    
    pip install build_scenarist
fi
