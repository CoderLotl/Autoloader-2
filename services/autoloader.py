import importlib
import builtins
import os
import sys

def autoloader(args):
    # Walk through all directories and add them to sys.path
    for root, dirs, files in os.walk('.'):  # Starts from the current directory
        sys.path.append(root)  # Add directory to sys.path

    for arg in args:
        try:
            # Dynamically import the module using the full path from sys.path
            module = importlib.import_module(arg)
            class_ref = getattr(module, arg.split('.')[-1])  # Extract class name from module
            setattr(builtins, arg.split('.')[-1], class_ref)  # Inject into builtins globally
        except ImportError as e:
            print(f"Failed to import {arg}: {e}")
        except AttributeError:
            print(f"Class {arg.split('.')[-1]} not found in module {arg}.")