# NOMICC 2026 Exercises

This repository contains four of the exercises for the 2026 edition of the Summer School on Nonlinear Optimization with Mixed Integer and Complementarity Constraints.
These exercises are:

- Implementing the sparsity promoting $\ell_0$ norm penalty for a classical portfolio optimization problem.
- Implementing state-triggered constraints for a 3-dimensional docking problem.
- Extending an energy optimal longitudinal control example for a truck with a gearbox.
- Extending complementarity-based planning through contact manipulation problem.

The exercises are written in python, if you are unfamiliar with python, you can pair up with a participant who is, or ask the instructors for help.
Each exercise will be provided in its own directory as a subdirectory of `/exercises` and you will find a more detailed description of each exercise there.

## Pre-requisite software

The following software is required to run the examples:

- `python` versions `>=3.12`.
  - On Windows, the "Microsoft Store" based installation methods will not work.
- `CasADi` version `>=3.8`, an open-source tool for nonlinear optimization and algorithmic differentiation. 
  - Installation: Follow instructions on [this page,](https://web.casadi.org/get/)
- [`CAMINO`](github.com/minlp-toolbox/CAMINO) a software package providing a Python/CasADi-based implementation of several algorithms for solving mixed-integer nonlinear programs (MINLPs). We primarily use this for the `Description` interface which is used to model two of the exercises.
  - Installation: `pip install caminopy`
- [`libMad`](https://github.com/madsuite-org/libMad), a shared library which contains a c interface for [`CCOpt.jl`](https://github.com/madsuite-org/CCOpt.jl) and [`MadNLP.jl`](https://github.com/madsuite-org/MadNLP.jl).
  - Installation: Download and untar the correct [built release](https://github.com/madsuite-org/libMad/releases/tag/v0.0.12-casadi). Follow instructions in the README for your particular platform. This mostly involves adding the path to `libMad.<soext>`, to the dynamic library load path on your platform (`LD_LIBRARY_PATH` on linux systems, `DYLIB_LIBRARY_PATH` on apple systems, and `PATH` on windows systems).
- [`nosnoc`](https://github.com/nosnoc/nosnoc_py) an open source Python software package for NOnSmooth Numerical Optimal Control. We only use `nosnoc` for its [`vdx`](https://github.com/apozharski/vdx_py) based tracking.
  - Installation: Clone `git@github.com:nosnoc/nosnoc_py.git`, checkout the branch `v1.0.0-rc`, and install via `pip install -e .`

### Optional Packages
Additionally, there is some optional software which you can additionally use:

- [`gurobi`](https://www.gurobi.com), which allows you to use the specialized solvers in `CAMINO`.
  - To install `gurobi`, acquire an [academic licence](https://www.gurobi.com/academics), and follow the installation instructions provided.
- [`LibHSL`](https://licences.stfc.ac.uk/product/libhsl-2025_7_21), which allows you to use the sparse linear system solvers `MA27`, `MA57`, and `MA97` in `CCOpt.jl` which can significantly speed up solve times.
  - To install `LibHSL` acquire an academic licence, download the libraries, un-compress them, and set the `JULIA_HSL_LIBRARY_PATH` environment variable. It can be useful to add this as well to the virtual environment activation if you so choose.

We advise to use your favorite virtual environment manager ([`virtualenv`](https://virtualenv.pypa.io/en/latest/), [`venv`](https://docs.python.org/3/library/venv.html), etc.) to set up your exercise environment.

## Installation on Linux (x86-64) Systems:
The shell script `install_linux.sh` should provide you with a functioning environment on a linux-x86-64 based machine with `git`, `curl`, `virtualenv`, and `tar` available.
Roughly the installation script does:
1. Clones and checks out the correct versions of this repository and `nosnoc`.
2. Downloads and untars the `libMad` binaries.
3. Creates and populates a virtual environment with the necessary python dependencies.
4. Adds the required `exports` to the `activate` script in the virtual environment
5. Runs a test python script which should run with no errors if your system is correctly set up.

## Installation on Macos (aarch64) Systems:
The shell script `install_macos_aarch64.sh` should provide you with a functioning environment on a macos-aarch64 based machine with `git`, `curl`, `virtualenv`, and `tar` available.
It follows the same general steps as the linux script.

## Installation on Windows (x86-64) Systems:
On windows you can follow roughly the same steps as in the case of linux but no script is provided (run commands in `powershell`):

0. Install Git and Python

- If needed, install [Git for Windows](https://git-scm.com/install/windows), keeping the option to use Git from the command line.
- Install [64-bit Python](https://www.python.org/downloads/windows/) using the Windows installer and enable **Add python.exe to PATH**. Avoid the Microsoft Store version for libMad.

1. Clone the repositories

```powershell
git clone https://gitlab.syscop.de/armin.nurkanovic/nomicc26_exercise.git
git clone --branch v1.0.0-rc --recurse-submodules https://github.com/nosnoc/nosnoc_py.git
```

2. Download and extract the (non-cuda) [windows build libMad](https://github.com/madsuite-org/libMad/releases/download/v0.0.12-casadi/libMad-windows-x86_64-v0.0.12-casadi.tar.gz)

```powershell
tar -xzf .\libMad-windows-x86_64-v0.0.12-casadi.tar.gz
```

3. Add the libMad `bin` directory to the `PATH` environment variable. If you don't know how, use [this tutorial](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

4. Create and activate the local environment

```powershell
cd .\nomicc26_exercise
python -m venv venv
.\venv\Scripts\Activate.ps1
```

5. Install CasADi, CAMINO, and `nosnoc`

```powershell
python -m pip install casadi caminopy
python -m pip install -e ..\nosnoc_py
```

6. Verify the installation by running the test install script

```powershell
python .\test_install.py --ccopt --camino --nosnoc
```

## LLM Tutorial

You will need access to a coding agent with a configured model. Ensure you have the required subscription or API access before the tutorial.

If you do not have access, pair with a local organizer or another participant.