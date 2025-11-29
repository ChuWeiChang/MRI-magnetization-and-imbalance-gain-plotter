MRI magnetization plotter
=========================

A tiny Python script that computes and plots simple longitudinal (M_z) and transverse (M_xy) magnetization curves using exponential T1 recovery and T2 decay.

What this does
--------------
- Computes normalized magnetization over multiple TR intervals using simple exponential models.
- Shows a matplotlib plot of M_z (longitudinal) and M_xy (transverse) vs time.

Install dependencies
--------------------
Run in a terminal (Windows cmd.exe):

```
pip install -r requirements.txt
```

How to run
----------
From the project root (where `1.py` lives), run:

```
python 1.py
```

This will open a matplotlib window showing the magnetization curves.

Configuration
-------------
`1.py` includes a `config` dict in `main()` where you can tweak:
- `duration`: number of TR intervals to compute
- `t1`: longitudinal relaxation time (T1)
- `t2`: transverse relaxation time (T2)
- `tr`: repetition time (TR) (time between excitations)
- `M0`: equilibrium magnetization (only affects absolute values; the plot uses normalized values)
- `sample_num`: how many samples per TR (higher -> smoother curves)

Notes
-----
- The code normalizes magnetization to M0, so changing `M0` won't change the plotted curve shapes.
- The code contains comments explaining the T1/T2 calculations, time array construction, and normalization logic for clarity.
