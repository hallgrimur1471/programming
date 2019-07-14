# Download and unpack googletest at configure time
configure_file(CMakeLists.txt.in googletest-download/CMakeLists.txt)
execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" .
  RESULT_VARIABLE result
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/googletest-download )
if(result)
  message(FATAL_ERROR "CMake step for googletest failed: ${result}")
endif()
execute_process(COMMAND ${CMAKE_COMMAND} --build .
  RESULT_VARIABLE result
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/googletest-download )
if(result)
  message(FATAL_ERROR "Build step for googletest failed: ${result}")
endif()

# Prevent overriding the parent project's compiler/linker
# settings on Windows
#set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add googletest directly to our build. This defines
# the gtest and gtest_main targets.
add_subdirectory(${CMAKE_BINARY_DIR}/googletest-src
  ${CMAKE_BINARY_DIR}/googletest-build)

# The gtest/gtest_main targets carry header search path
# dependencies automatically when using CMake 2.8.11 or
# later. Otherwise we have to add them here ourselves.
if (CMAKE_VERSION VERSION_LESS 2.8.11)
  include_directories("${gtest_SOURCE_DIR}/include")
endif()

# create a libraries for our program
add_library(factorial_lib src/factorial.cpp)
add_library(myString_lib src/myString.cpp)

# build executable for the project
add_executable(factorial src/main.cpp src/factorial.cpp)
#target_link_libraries(factorial factorial_lib)

# build executable for the tests and add links to the libraries it uses
add_executable(runUnitTests src/factorial_unittest.cpp src/myString_unittest.cpp)
target_link_libraries(runUnitTests gtest gtest_main factorial_lib myString_lib)

# This is so you can do 'make test' to see all your tests run, instead of
# manually running the executable runUnitTests to see those specific tests
enable_testing()
add_test(NAME FactorialTest2 COMMAND runUnitTests)

#target_link_libraries(factorial gtest_main)
#add_test(NAME factorial_test COMMAND factorial)
