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
python src/collatz_prime_path.py --list 15 25 35 45 48 55 85 90 --csv results.csv
This produces a CSV table with the maximal prime function P_max(n) for each input:
| n  | P\_max |
| -- | ------ |
| 15 | 53     |
| 25 | 29     |
| 35 | 53     |
| 45 | 17     |
| 48 | 5      |
| 55 | 1619   |
| 85 | 2      |
| 90 | 17     |

Remarks:
48, 85 reach the anchor primes {2,5}.
90 behaves like 45, with P_max=17.
This set was chosen to cover all three residue classes mod 6 (“three-bucket” test).
## Quick Start

```bash
# Clone the repository
git clone https://github.com/cisumchen/prime-generating-machine.git
cd prime-generating-machine

# Run analysis for a single n
python src/collatz_prime_path.py --n 41 --export examples/trajectory_41.txt

# Batch over a range
python src/collatz_prime_path.py --range 1 100 --csv results.csv

