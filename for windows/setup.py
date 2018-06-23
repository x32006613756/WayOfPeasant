from cx_Freeze import setup, Executable

setup(
    name = "start",
    version = "1.2",
    description = "wayofpeseant",
    executables = [Executable("wc.py")]
)