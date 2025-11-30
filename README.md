# MRI magnetization and k-space imbalance plotter

A small set of Python scripts to demonstrate simple MRI concepts:
- `magnitude_plotter.py`: plots simple longitudinal (M_z) and transverse (M_xy) magnetization curves using T1/T2 exponential models.
- `imbalanced_gain_simulator.py`: generates a Shepp-Logan phantom, modifies k-space by scaling real/imaginary parts, and shows the original and reconstructed magnitude images.

Requirements
------------

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
python -m pip install -r requirements.txt
```

Quick start
-----------
- To run the magnetization plot (script `magnitude_plotter.py`):

```
python magnitude_plotter.py
```

- To run the k-space phantom example (script `imbalanced_gain_simulator.py`):

```
python imbalanced_gain_simulator.py --real_scaler 1.0 --im_scaler 1.0 --size 256
```

Notes
-----
- `imbalanced_gain_simulator.py` shows how changing real and imaginary gains in k-space affects the reconstructed image magnitude. The file contains short comments explaining the FFT and reconstruction steps.

License
-------
This repository is provided as-is for learning and experimentation.
