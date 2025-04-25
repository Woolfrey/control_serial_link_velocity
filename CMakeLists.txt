cmake_minimum_required(VERSION 3.12)

project(software_template
        DESCRIPTION "This is a template for software projects."
        LANGUAGES CXX
        VERSION 1.0)

# Set default build type to Release if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build (Debug, Release, RelWithDebInfo, MinSizeRel)" FORCE)
endif()

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")

####################################################################################################
#                                          REQUIREMENTS                                            #
####################################################################################################

# Packages
# find_package(name REQUIRED)

# Location of header files
include_directories(include)
# include_directories(${NAME_INCLUDE_DIR})

####################################################################################################
#                                           EXECUTABLES                                            #
####################################################################################################

# Haiku
add_executable(haiku src/nodes/haiku_node.cpp
                     src/haiku.cpp)

# target_link_libraries(haiku PRIVATE Library::Library)
