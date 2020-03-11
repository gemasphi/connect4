CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(CONNECT4)
SET(CONNECT4_VERSION_MAJOR 0)
SET(CONNECT4_VERSION_MINOR 9)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++14 -W -Wall -O3 -DNDEBUG")

ADD_LIBRARY(c4solver_dependencies STATIC
	Solver.cpp
	Solver.hpp
	Position.hpp
	TranspositionTable.hpp
        OpeningBook.hpp
	MoveSorter.hpp)

ADD_EXECUTABLE(c4solver
	main.cpp)

ADD_EXECUTABLE(c4generator
        generator.cpp)

TARGET_LINK_LIBRARIES(c4solver c4solver_dependencies)
TARGET_LINK_LIBRARIES(c4generator c4solver_dependencies)

INSTALL(TARGETS c4solver_dependencies DESTINATION lib)
INSTALL(TARGETS c4generator DESTINATION bin)
INSTALL(TARGETS c4solver DESTINATION bin)


include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG        v2.4.3
)

FetchContent_GetProperties(pybind11)
if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
endif()

pybind11_add_module(perfect_player pybind.cc)
target_link_libraries(perfect_player PUBLIC c4solver_dependencies)
set_target_properties(c4solver_dependencies PROPERTIES POSITION_INDEPENDENT_CODE TRUE)