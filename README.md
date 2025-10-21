# Python Course 2: Object-Oriented Programming in Python
 
This repository contains the lecture slides and the source code used for the course.

## Requirements

To get the most out of this course, you’ll need the following:

### Essential

- **Python** (version 3.10 or higher recommended)
- **Visual Studio Code (VS Code)** as your code editor

### Recommended

- **VS Code Python extension** for syntax highlighting, code navigation, and debugging

### Optional (required only if you want to run the Pyomo optimization examples)

- **Pyomo-compatible solver** such as CBC, GLPK, CPLEX, or Gurobi

## Installation Overview

Below is a brief overview of how to install each requirement. For detailed, platform-specific instructions, please refer to the official documentation for each tool.

### 1. Python

- Download and install Python from the [official Python website](https://www.python.org/).
- Make sure Python is added to your system PATH.

### 2. VS Code

- Download Visual Studio Code from the [official VS Code website](https://code.visualstudio.com/).
- To install the Python extension (recommended):
    - Open VS Code.
    - Go to the Extensions view by clicking the square icon in the sidebar or pressing `Ctrl+Shift+X`.
    - Search for "Python" and install the extension published by Microsoft.

### 3. Pyomo-Compatible Solver (Optional)

- **CBC:** Available via [coin-or.org](https://coin-or.github.io/Cbc/) or installable with `conda install -c conda-forge coincbc`.
- **GLPK:** Download from [gnu.org/software/glpk](https://www.gnu.org/software/glpk/) or install with `conda install -c conda-forge glpk`.
- **CPLEX/Gurobi:** Commercial solvers, free academic licenses available. Refer to [IBM CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) or [Gurobi](https://www.gurobi.com/).
- Make sure the solver is accessible from your system's command line so Pyomo can use it.

## Repository Contents

- **Slides:** The lecture slides are located in `slides/`.
- **Source Code:** The Python scripts and code examples are located in `src/`.
- **Data:** The data used in the examples are located in `data/`.

---