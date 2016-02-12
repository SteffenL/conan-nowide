cmake_minimum_required(VERSION 3.4 FATAL_ERROR)

project(nowide)
set(TARGET_NAME nowide)


#
# Third-party setup
#

# Setup Conan
include(conanbuildinfo.cmake)
# FIXME: The following workaround is used due to a bug in Conan 0.6.
#        See: https://github.com/conan-io/conan/issues/118
conan_output_dirs_setup()
conan_flags_setup()
set(CMAKE_MODULE_PATH ${CONAN_CMAKE_MODULE_PATH} ${CMAKE_MODULE_PATH}) 
#conan_basic_setup()


#
# Setup our target
#

file(GLOB_RECURSE Sources
    "nowide/src/*.cpp"
)

add_library(${TARGET_NAME} STATIC ${Sources})

target_include_directories(${TARGET_NAME}
    PUBLIC "nowide"
)
