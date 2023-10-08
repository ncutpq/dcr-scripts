cmake_minimum_required(VERSION 3.16)
project(demo C CXX ASM)


set(CMAKE_C_STANDARD 17)

add_executable(demo hello.cpp)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${PYTHON_LIBRARIES})



