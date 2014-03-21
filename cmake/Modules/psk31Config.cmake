INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PSK31 psk31)

FIND_PATH(
    PSK31_INCLUDE_DIRS
    NAMES psk31/api.h
    HINTS $ENV{PSK31_DIR}/include
        ${PC_PSK31_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PSK31_LIBRARIES
    NAMES gnuradio-psk31
    HINTS $ENV{PSK31_DIR}/lib
        ${PC_PSK31_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PSK31 DEFAULT_MSG PSK31_LIBRARIES PSK31_INCLUDE_DIRS)
MARK_AS_ADVANCED(PSK31_LIBRARIES PSK31_INCLUDE_DIRS)

