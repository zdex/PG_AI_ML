# NumPy sample project

This small sample demonstrates basic NumPy usage in `main.py`.

Files created:

- `main.py` - Example functions using NumPy and a small demo when run as script.
- `test_main.py` - Unit tests (skip if NumPy isn't installed).
- `requirements.txt` - Lists NumPy as dependency.

How to run (Windows, cmd.exe):

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```cmd
pip install -r requirements.txt
```

3. Run the demo script:

```cmd
python main.py
```

4. Run tests (unittest):

```cmd
python -m unittest test_main.py
```

Notes:

- The tests will be skipped if NumPy is not installed, so importing the package is safe.
- If you can't (or don't want to) install NumPy, you can still open and read `main.py` for examples of typical NumPy code.
