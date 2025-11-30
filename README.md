# MRI magnetization and k-space imbalance plotter

A small set of Python scripts to demonstrate simple MRI concepts:
- `1.py`: plots simple longitudinal (M_z) and transverse (M_xy) magnetization curves using T1/T2 exponential models.
- `2.py`: generates a Shepp-Logan phantom, modifies k-space by scaling real/imaginary parts, and shows the original and reconstructed magnitude images.

Requirements
------------
Install dependencies with pip (use your Python environment):

```
python -m pip install -r requirement.txt
```

Use a virtual environment (recommended)
-------------------------------------
It's best to run these scripts inside an isolated Python virtual environment so dependencies don't affect your system Python or other projects.

For Windows (cmd.exe):

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirement.txt
```

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirement.txt
```

For macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirement.txt
```

Quick start
-----------
- To run the magnetization plot (script `1.py`):

```
python 1.py
```

- To run the k-space phantom example (script `2.py`):

```
python 2.py
```

Notes
-----
- `2.py` uses the `phantominator` package to create a Shepp-Logan phantom image. If you don't have it installed, install it with `pip` or replace the phantom call with another image array.
- `2.py` shows how changing real and imaginary gains in k-space affects the reconstructed image magnitude. The file contains short comments explaining the FFT and reconstruction steps.

License
-------
This repository is provided as-is for learning and experimentation.
