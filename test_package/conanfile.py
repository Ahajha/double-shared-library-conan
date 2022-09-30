from conan import ConanFile
from conan.tools.build.cross_building import cross_building
from conan.tools.cmake import CMake
import os

class DoubleShareTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not cross_building(self):
            self.run(os.path.join("bin", "test_pkg1"))
            self.run(os.path.join("bin", "test_pkg2"))
