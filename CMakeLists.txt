cmake_minimum_required (VERSION 2.8.11)

project("scenarist")

set (Scenarist_VERSION_MAJOR 0)
set (Scenarist_VERSION_MINOR 5)
set (Scenarist_VERSION_PATCH 2)

INSTALL(DIRECTORY "Scenarist/"  DESTINATION "bin/Scenarist")
INSTALL(PROGRAMS "scenarist" DESTINATION "bin/")

# build a CPack driven installer package
# include (InstallRequiredSystemLibraries)
set (CPACK_PACKAGE_VERSION_MAJOR "${Scenarist_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Scenarist_VERSION_MINOR}")
set (CPACK_PACKAGE_VERSION_PATCH "${Scenarist_VERSION_PATCH}")
set (CPACK_PACKAGE_VERSION "${CPACK_PACKAGE_VERSION_MAJOR}.${Scenarist_VERSION_MINOR}.${Scenarist_VERSION_PATCH}")
set (CPACK_PACKAGE_VENDOR "Aleksandr Lizin <sogimu@nxt.ru>")
set (CPACK_PACKAGE_DESCRIPTION_SUMMARY "Utility for running platform depended scripts. Lang of scripts is Python 2.7. Scripts have targets.")
set (CPACK_SOURCE_GENERATOR "ZIP")

if(CMAKE_SYSTEM_NAME STREQUAL "Linux" AND NOT ANDROID)
    set(CPACK_GENERATOR "DEB")
    set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Aleksandr Lizin <sogimu@nxt.ru>")
    set(CPACK_DEBIAN_PACKAGE_DEPENDS "python2.7 (>= 2.7.6-8)")
endif()

if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    set(CPACK_GENERATOR "NSIS")
    set(CPACK_NSIS_CONTACT "Aleksandr Lizin <sogimu@nxt.ru>")
    set(CPACK_NSIS_PACKAGE_NAME "Scenarist")
    set(CPACK_NSIS_DISPLAY_NAME "Scenarist")
    set(CPACK_NSIS_MODIFY_PATH ON)
    set(CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL ON)

endif()

include (CPack)
