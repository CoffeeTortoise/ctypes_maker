# ctypes_maker

## Overview

**ctypes_maker** is a console utility designed to generate `ctypes` definitions from C header files. Written entirely in Python 2.7, this tool streamlines the process of creating Python bindings for C libraries, allowing developers to leverage C functionality directly within Python applications.

## Features

- **Automatic `ctypes` Generation**: Converts C header files into Python `ctypes` definitions.
- **Supports Multiple Data Types**: Handles a variety of C data types, ensuring accurate translations.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Installation

To install `ctypes_maker`, simply clone the repository and run the setup script:

```bash
git clone https://github.com/yourusername/ctypes_maker.git
cd ctypes_maker
python setup.py build
```

## Usage

To use ctypes_maker, run the following command in your terminal:

```bash
ctypes_maker [options] <header_file>
```

## Example

```bash
ctypes_maker -in=Rect.h -out=Rect.py -co=config_folder
```