pip_library(
    name = "cffi",
    version = "1.14.6",
    deps = [':pycparser']
)

pip_library(
    name = "pycparser",
    version = "2.20",
)

pip_library(
    name = "cryptography",
    version = "36.0.1",
    deps = [':cffi'],
    visibility = ["PUBLIC"],
)
