# README
---
**Autor:** *CoderLotl - 19/3/2023*

## Intro

Sencilla función que tiene por finalidad la importación automática de clases en una sola línea, evitando múltiples líneas y pathing a través de diversas carpetas o fuentes de recursos.
Esta función tiene 2 requerimientos:
1. Que cada archivo tenga 1 clase, y solo 1 clase.
2. Que tanto el nombre del archivo como de la clase sean exactamente el mismo.


## 1- Código
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

El código es autoexplicativo:

Recibe un array de str con los nombres de los archivos/clases a cargar.
La función hará la búsqueda de las clases y las importará, añadiéndolas al módulo *builtins* para que posteriormente puedan utilizarse dichas clases de una manera más cómoda desde cualquier lado.

Esta idea fue concebida para emular un poco la utilidad del autoloader de PHP.

## 2- Estructura del repositorio

    [ROOT]
    ├── classes
    |       ├── Animal.py
    |       └── Person.py
    ├── services
    |       └── autoloader.py
    ├── hooks
    |       └── test.py
    └── main.py    

## 3- Ejemplo de uso

    from services.autoloader import autoloader
    from hooks.test import test

    autoloader(['Person', 'Animal'])

    test()

- - - 