cmake_minimum_required(VERSION 3.15)
project(double-share)

add_compile_options(-fpic)

add_library(lib1 SHARED "${CMAKE_SOURCE_DIR}/pkg1/lib1.cpp")
target_include_directories(lib1 PUBLIC pkg1)

add_library(lib2 SHARED "${CMAKE_SOURCE_DIR}/pkg2/lib2.cpp")
target_include_directories(lib2 PUBLIC pkg2)
target_link_libraries(lib2 PUBLIC lib1)

add_executable(test main.cpp)
target_link_libraries(test PRIVATE lib2)

install(DIRECTORY "${CMAKE_SOURCE_DIR}/pkg1" DESTINATION .)
install(DIRECTORY "${CMAKE_SOURCE_DIR}/pkg2" DESTINATION .)
install(TARGETS lib1 DESTINATION lib)
install(TARGETS lib2 DESTINATION lib)
