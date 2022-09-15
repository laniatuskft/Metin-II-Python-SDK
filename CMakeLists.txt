cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(Diamas)

message(STATUS "CMake version: ${CMAKE_VERSION}")

# Default build type
if(NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE "Debug" CACHE STRING
		"Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

if("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
	set(DEBUG_POSTFIX "_d")
endif()

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")

if (MSVC)
	message(STATUS "MSVC: ${MSVC_VERSION}")
else()
	message(STATUS "Compiler: ${CMAKE_SYSTEM_NAME}")
endif()

# Version
file (STRINGS "VERSION.txt" MAJOR_VERSION)
message(STATUS "VERSION: ${MAJOR_VERSION}")

# Build options
option(BUILD_UTILITIES "Build the common utilities" ON)
option(BUILD_CLIENT "Build the client binaries" ON)
option(BUILD_SERVER "Build the server binaries" ON)
option(BUILD_TOOLS "Build the tool binaries" OFF)
option(ENABLE_STATIC_ANALYSIS "Enable static code analysis with PVS Studio" OFF)
option(ENABLE_AUTO_RELEASE "Enable auto release create in git repo" OFF)
option(ENABLE_CYTHON "Cythonize python scripts" OFF)
option(DIAMAS_STATIC_BUILD "Static linking for serverside" ON)
if (CI_BUILD)
	set(DIAMAS_STATIC_BUILD OFF)
endif()

# Output dir
set(OUTPUT_DIR ${PROJECT_SOURCE_DIR}/Bin)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_MINSIZEREL ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELWITHDEBINFO ${OUTPUT_DIR})

# Colored output configration
SET(CMAKE_COLOR_MAKEFILE ON)

# CMake modules
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/extern/cmake")
add_definitions(-DCMAKE_BUILD_SYSTEM)
if (ENABLE_STATIC_ANALYSIS)
	include(${CMAKE_MODULE_PATH}/PVS-Studio.cmake)
endif()

# C++ options
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Global definations
add_definitions(-DJM_XORSTR_DISABLE_AVX_INTRINSICS) # xorstr
add_definitions(-DCRYPTOPP_ENABLE_NAMESPACE_WEAK=1) # cryptopp
add_definitions(-DASIO_STANDALONE) # websocketpp
add_definitions(-DUSE_BOOST_ASIO=0) # amy
add_definitions(-DFMT_HEADER_ONLY) # fmt
if (CI_BUILD)
	add_definitions(-DCI_BUILD=1)
	message(STATUS "CI Build mode detected.")
endif()

# Platform defination
if (CMAKE_SIZEOF_VOID_P EQUAL 8)
	add_definitions(-DTARGET_ARCH=64)
	set(TARGET_ARCH_STR "64")
	message(STATUS "Arch: x64")
else() 
	add_definitions(-DTARGET_ARCH=86)
	set(TARGET_ARCH_STR "86")
	message(STATUS "Arch: x86")
endif()

# Additional languages
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
	enable_language(RC)
endif()

# Git
execute_process ( COMMAND git rev-list HEAD OUTPUT_VARIABLE GIT_REV_LIST_OUTPUT ERROR_VARIABLE GIT_REV_LIST_OUTPUT RESULT_VARIABLE GIT_REV_LIST_RESULT WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} )

if( NOT ${GIT_REV_LIST_RESULT} EQUAL 0 )
	message( FATAL_ERROR "get_git_revision(): can not get git revision. log followed: ${GIT_REV_LIST_OUTPUT}")
endif()

string(STRIP ${GIT_REV_LIST_OUTPUT} GIT_REV_LIST_OUTPUT)
string(REPLACE "\n" ";" GIT_REV_LIST ${GIT_REV_LIST_OUTPUT} )

list(LENGTH GIT_REV_LIST gitVersion )

add_definitions(-D_GIT_VERSION_="${gitVersion}")
MESSAGE(STATUS "GitREV=${gitVersion}")

if (WIN32)
	add_definitions(-D_HOSTNAME_="${USERNAME}")
	MESSAGE(STATUS "USERNAME=${USERNAME}")
else()
	add_definitions(-D_HOSTNAME_="${HOSTNAME}")
	MESSAGE(STATUS "HOSTNAME=${HOSTNAME}")
endif()

add_definitions(-D_DIRECTORY_="${CMAKE_SOURCE_DIR}")
MESSAGE(STATUS "DIRECTORY=${CMAKE_SOURCE_DIR}")

add_definitions(-D__MAJOR_VERSION__="${MAJOR_VERSION}")
add_definitions(-D__PRODUCT_VERSION__="${MAJOR_VERSION}.${gitVersion}")
add_definitions(-D__FILE_VERSION__=${MAJOR_VERSION},${gitVersion},0,0)
add_definitions(-D__DIAMAS_VERSION__=${MAJOR_VERSION}${gitVersion})

file(MAKE_DIRECTORY "Bin_public/${MAJOR_VERSION}.${gitVersion}")

# Until to build client x64 3rd libs, Disable client build for x64.
if (CMAKE_SIZEOF_VOID_P EQUAL 8)
	set(BUILD_CLIENT OFF)
endif()

# Compiler subdir for MySQL libs
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
	set(COMPILER_SUBDIR "clang")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
	set(COMPILER_SUBDIR "gcc")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
	set(COMPILER_SUBDIR "msvc")
endif()

if(NOT WIN32)
	MESSAGE(STATUS "Non-Win32 system detected")

	# Disable client build for non win32
	set(BUILD_CLIENT OFF)
endif()

# Check enabled projects
if("${BUILD_UTILITIES}" STREQUAL "OFF" AND "${BUILD_TOOLS}" STREQUAL "OFF" AND
   "${BUILD_SERVER}" STREQUAL "OFF" AND "${BUILD_CLIENT}" STREQUAL "OFF")
	message(FATAL_ERROR "Nothing to build")
	return()
endif()

# MSVC specific settings ( MD -> MT, Multi processor, Disable SAFESH, Disable linking libci.lib )
if(MSVC)
    set(LIB_RT_SUFFIX "mt")
    set(LIB_RT_OPTION "/MT")

    foreach(flag_var  CMAKE_C_FLAGS  CMAKE_CXX_FLAGS)
         foreach(config_name  ""  DEBUG  RELEASE  MINSIZEREL  RELWITHDEBINFO)
            set(var_name "${flag_var}")

            if(NOT "${config_name}" STREQUAL "")
                set(var_name "${var_name}_${config_name}")
            endif()
            
            string(REPLACE "/MD" "${LIB_RT_OPTION}" ${var_name} "${${var_name}}")
            set(${var_name} "${${var_name}}" CACHE STRING "" FORCE)
        endforeach()
    endforeach()

	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")
	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /MP")

	set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO /NODEFAULTLIB:libci.lib")
endif()

# Register 3rd dependecies include paths
include_directories(${PROJECT_SOURCE_DIR}/extern/include)
include_directories(${PROJECT_SOURCE_DIR}/extern/include/cef)

# Register 3rd dependecies precompiled library path
link_directories(${PROJECT_SOURCE_DIR}/Bin/Utilities)
if (WIN32)
	link_directories(${PROJECT_SOURCE_DIR}/extern/lib_win_x${TARGET_ARCH_STR})
	if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_win_x${TARGET_ARCH_STR}/cef/debug)
	else()
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_win_x${TARGET_ARCH_STR}/cef/release)
	endif()
else()
	if (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_bsd_x${TARGET_ARCH_STR}/cryptopp/${COMPILER_SUBDIR})
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_bsd_x${TARGET_ARCH_STR}/devil/${COMPILER_SUBDIR})
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_bsd_x${TARGET_ARCH_STR}/mysql)
	elseif (CMAKE_SYSTEM_NAME MATCHES ".*Linux")
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_ubuntu_x${TARGET_ARCH_STR}/cryptopp/${COMPILER_SUBDIR})
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_ubuntu_x${TARGET_ARCH_STR}/devil/${COMPILER_SUBDIR})
		link_directories(${PROJECT_SOURCE_DIR}/extern/lib_ubuntu_x${TARGET_ARCH_STR}/mysql)
	else()
		message(FATAL_ERROR "Unknown OS: ${CMAKE_SYSTEM_NAME}")
	endif()
	link_directories(${PROJECT_SOURCE_DIR}/extern/lib_bsd_x${TARGET_ARCH_STR})
endif()

# Sub-projects
add_subdirectory(${PROJECT_SOURCE_DIR}/source/common)

#if(BUILD_UTILITIES)
	add_subdirectory(${PROJECT_SOURCE_DIR}/source/utilities)
#endif()

if(BUILD_SERVER)
	add_subdirectory(${PROJECT_SOURCE_DIR}/source/server)
endif()

if(WIN32)
	if(BUILD_CLIENT)
		add_subdirectory(${PROJECT_SOURCE_DIR}/source/client)
	endif()
	if(BUILD_TOOLS)
		add_subdirectory(${PROJECT_SOURCE_DIR}/tools)
	endif()
endif()
