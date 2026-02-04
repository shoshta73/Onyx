#!/usr/bin/env python3

import sys
import pathlib
import subprocess

UTILS_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = UTILS_DIR.parent
BUILD_DIR = ROOT_DIR / "build"


DEFAULT_BUILD_MODE = "Debug"

if sys.platform == "win32":
    DEFAULT_GENERATOR = "Visual Studio 17 2019"
elif sys.platform == "linux":
    DEFAULT_GENERATOR = "Unix Makefiles"


if sys.platform == "win32":
    print(f"Select the CMake generator to use (default:{DEFAULT_GENERATOR})")
    print("1. Visual Studio 17 2019")
    print("2. Ninja")
    print("3. Ninja Multi-Config")
    print("4. Default")

    user_input = int(input("Enter your choice: "))
    if user_input not in [1, 2, 3, 4]:
        print("Invalid choice")
        print(f"Defaulting to {DEFAULT_GENERATOR}")
        generator = DEFAULT_GENERATOR
    else:
        if user_input == 1:
            generator = "Visual Studio 17 2019"
        elif user_input == 2:
            generator = "Ninja"
        elif user_input == 3:
            generator = "Ninja Multi-Config"
        else:
            generator = DEFAULT_GENERATOR


if sys.platform == "linux":
    print(f"Select the CMake generator to use (default:{DEFAULT_GENERATOR})")
    print("1. Unix Makefiles")
    print("2. Ninja")
    print("3. Ninja Multi-Config")
    print("4. Default")

    user_input = int(input("Enter your choice: "))
    if user_input not in [1, 2, 3, 4]:
        print("Invalid choice")
        print(f"Defaulting to {DEFAULT_GENERATOR}")
        generator = DEFAULT_GENERATOR
    else:
        if user_input == 1:
            generator = "Unix Makefiles"
        elif user_input == 2:
            generator = "Ninja"
        elif user_input == 3:
            generator = "Ninja Multi-Config"
        else:
            generator = DEFAULT_GENERATOR

user_input = input("Do you want to generate compile_commands.json? (y/n) ")
if user_input.lower() == "y" or user_input.lower() == "yes":
    generate_compile_commands = True
else:
    generate_compile_commands = False

print("Available build modes: ")
print("1. Debug")
print("2. Release")
print("3. RelWithDebInfo")
print("4. MinSizeRel")
user_input = int(input("Enter your choice: "))
if user_input not in [1, 2, 3, 4]:
    print("Invalid choice")
    print("Defaulting to Debug")
    build_mode = DEFAULT_BUILD_MODE
else:
    if user_input == 1:
        build_mode = "Debug"
    elif user_input == 2:
        build_mode = "Release"
    elif user_input == 3:
        build_mode = "RelWithDebInfo"
    else:
        build_mode = "MinSizeRel"

command = [
    "cmake",
    "-S",
    str(ROOT_DIR),
    "-B",
    str(BUILD_DIR),
    "-G",
    generator,
    f"-DCMAKE_EXPORT_COMPILE_COMMANDS={'ON' if generate_compile_commands else 'OFF'}",
    f"-DCMAKE_BUILD_TYPE={build_mode}",
]

print(f"Would run following command: {' '.join(command)}")
print("Permission to run the command? (y/n)")
user_input = input()
if user_input.lower() == "y" or user_input.lower() == "yes":
    print(" ".join(command))
    result = subprocess.run(command, check=True)

    if result.returncode != 0:
        print("Failed to generate project")
        sys.exit(1)

else:
    print("Aborting")
    sys.exit(1)
