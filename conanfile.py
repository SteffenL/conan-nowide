from conans import ConanFile, CMake
import os

class NowideConan(ConanFile):
    name = "nowide"
    version = "master"
    url = "https://github.com/SteffenL/conan-nowide"
    license = "Boost"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt", "nowide/*"

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake . %s" % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy(pattern="*.hpp", dst="include/nowide", src="nowide/nowide")
        self.copy(pattern="*.lib", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["nowide"]
