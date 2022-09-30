from conan import ConanFile
from conan.tools.cmake import CMake

class DoubleShareConan(ConanFile):
    name = "double-share"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = [
        "CMakeLists.txt",
        "pkg1/*",
        "pkg2/*",
        "main.cpp",
    ]

    generators = "CMakeDeps", "CMakeToolchain"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    def package(self):
        cmake = CMake(self)
        cmake.install()
    
    def package_info(self):
        self.cpp_info.components["pkg1"].includedirs = ["pkg1"]
        self.cpp_info.components["pkg1"].libs = ["lib1"]

        self.cpp_info.components["pkg2"].includedirs = ["pkg2"]
        self.cpp_info.components["pkg2"].libs = ["lib2"]
        self.cpp_info.components["pkg2"].requires = ["pkg1"]
