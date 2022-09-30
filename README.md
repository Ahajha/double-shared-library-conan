Ubuntu 22.04
Python 3.10
Conan 1.52 (seems to have the same behavior since 1.46)
GCC 11 (10 has the same behavior)

To trigger the failure, run `conan create . 0.0.1@test/test`. It will fail to find liblib1.so.

This only happens if both libraries are set to SHARED. If you set either to STATIC, the test package succeeds.
