import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script=r"C:\Users\shubham\PycharmProjects\PyQt\codechef_app.py",
    base="Win32GUI",
    )

setup(
    name = "CPC",
    version = "0.1",
    options = {"build_exe":{"include_files":["favicon.ico","logo.png"]}},
    description = "Codechef Progress Calculator",
    executables = [exe]
    )
