cmake_minimum_required(VERSION 3.10)
project(hello-lib VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)

# Add project source files
add_library(greet_lib src/greet.cpp)

# Add the "include" folder as a header search directory
target_include_directories(greet_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Configura la instalación de la biblioteca
install(TARGETS greet_lib DESTINATION lib)
install(FILES src/greet.h DESTINATION include/hello-lib)



