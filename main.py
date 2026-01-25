"""
Sample Python program demonstrating basic NumPy usage.

Creates arrays, computes statistics, multiplies matrices, and solves a small linear system.
If NumPy is not installed, the script prints an instruction message.
"""

from typing import Optional

try:
    import numpy as np
except Exception:  # ImportError or other issues
    np = None


def create_linear_space(start: float, stop: float, num: int = 5):
    """Return a 1-D numpy array of evenly spaced numbers from start to stop.

    Raises:
        RuntimeError: if numpy is not available.
    """
    if np is None:
        raise RuntimeError("NumPy is required for create_linear_space. Install with: pip install numpy")
    return np.linspace(start, stop, num)


def compute_mean(array_like) -> float:
    """Compute the mean of a numpy array or array-like object."""
    if np is None:
        raise RuntimeError("NumPy is required for compute_mean. Install with: pip install numpy")
    arr = np.asarray(array_like)
    return float(arr.mean())


def matrix_multiply(a, b):
    """Multiply two 2-D arrays and return the result."""
    if np is None:
        raise RuntimeError("NumPy is required for matrix_multiply. Install with: pip install numpy")
    A = np.asarray(a)
    B = np.asarray(b)
    return A.dot(B)


def solve_linear_system(A, b):
    """Solve A x = b for x using NumPy linear algebra."""
    if np is None:
        raise RuntimeError("NumPy is required for solve_linear_system. Install with: pip install numpy")
    A_arr = np.asarray(A)
    b_arr = np.asarray(b)
    return np.linalg.solve(A_arr, b_arr)


def random_matrix(seed: Optional[int], n: int = 3):
    """Generate an n x n matrix of random numbers in [0, 1)."""
    if np is None:
        raise RuntimeError("NumPy is required for random_matrix. Install with: pip install numpy")
    rng = np.random.default_rng(seed)
    return rng.random((n, n))


def demo():
    """Run a short demonstration and print results to stdout."""
    if np is None:
        print("NumPy is not installed. To run the demo, install it with: pip install numpy")
        return

    print("== NumPy sample demo ==")

    xs = create_linear_space(0, 1, 5)
    print("linspace(0,1,5):", xs)

    arr_mean = compute_mean(xs)
    print("mean:", arr_mean)

    A = random_matrix(42, 3)
    B = random_matrix(7, 3)
    print("A:\n", A)
    print("B:\n", B)

    C = matrix_multiply(A, B.T)
    print("A @ B.T =\n", C)

    # Solve a small linear system
    M = np.array([[3.0, 1.0], [1.0, 2.0]])
    v = np.array([9.0, 8.0])
    x = solve_linear_system(M, v)
    print("Solve M x = v -> x:", x)


if __name__ == "__main__":
    demo()
