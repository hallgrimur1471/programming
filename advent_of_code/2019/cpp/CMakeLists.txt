cmake_minimum_required(VERSION 3.13.0)

project(advent_of_code LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(RUNTIME_OUTPUT_DIRECTORY bin)

file(GLOB DAY_SRC "src/*.cpp")

add_executable(advent_of_code src/main.cpp ${DAY_SRC})
target_include_directories(advent_of_code PUBLIC include)

install(TARGETS advent_of_code RUNTIME DESTINATION ${PROJECT_SOURCE_DIR})
