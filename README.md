# Prime-Generating Machine

This project explores **prime-generating trajectories in Collatz dynamics**.  
For a given starting integer \( n \), we iterate the Collatz map:

\[
T(n) = 
\begin{cases}
n/2, & n \text{ even}, \\[4pt]
3n+1, & n \text{ odd},
\end{cases}
\]

until reaching the terminal cycle \(1 \to 4 \to 2 \to 1\).

During the process, we track all prime numbers encountered along the path and record the **maximal prime function**:

\[
P_{\max}(n) = \max \{ x_k : x_k \ \text{is prime in the trajectory of } n \}.
\]

---

## Features

- Classical Collatz iteration (step-by-step).
- Compressed Collatz operator  
  \[
  T(n) = \frac{3n+1}{2^r}, \quad r = v_2(3n+1),
  \]
  which jumps directly to odd iterates.
- Primality testing with a simple deterministic check.
- Computes \( P_{\max}(n) \), the largest prime on each path.
- Example trajectories exported as plain text.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/cisumchen/prime-generating-machine.git
cd prime-generating-machine

# Run analysis for a single n
python src/collatz_prime_path.py --n 41 --export examples/trajectory_41.txt

# Batch over a range
python src/collatz_prime_path.py --range 1 100 --csv results.csv

