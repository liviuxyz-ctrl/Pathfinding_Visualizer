import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A* Visualizer",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["icon.jpg"]}},
    executables = executables

    )