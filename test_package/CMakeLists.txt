cmake_minimum_required(VERSION 3.15)
project(test-package)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "${CMAKE_CURRENT_BINARY_DIR}/bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_CURRENT_BINARY_DIR}/bin")

find_package(double-share REQUIRED)

add_executable(test_pkg1 test_pkg1.cpp)
target_link_libraries(test_pkg1 PRIVATE double-share::pkg1)

add_executable(test_pkg2 test_pkg2.cpp)
target_link_libraries(test_pkg2 PRIVATE double-share::pkg2)
