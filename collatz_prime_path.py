# src/collatz_prime_path.py
import argparse
import csv

def is_prime(x: int) -> bool:
    """Simple primality test"""
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def collatz_pmax(n: int) -> int:
    """Compute P_max(n) under the classical Collatz iteration"""
    pmax = 0
    while n != 1:
        if is_prime(n) and n > pmax:
            pmax = n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return max(pmax, 2)


def collatz_pmax_compressed(n: int) -> int:
    """Compute P_max(n) under the compressed Collatz operator (odd-core)"""
    # remove initial powers of 2
    while n % 2 == 0 and n > 1:
        n //= 2

    pmax = 0
    while n != 1:
        if is_prime(n) and n > pmax:
            pmax = n
        m = 3 * n + 1
        # compute r = v2(m)
        while m % 2 == 0:
            m //= 2
        n = m
    return max(pmax, 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collatz Prime Generator")
    parser.add_argument("--n", type=int, help="single starting integer n")
    parser.add_argument("--list", nargs="+", type=int, help="list of starting values")
    parser.add_argument("--compressed", action="store_true",
                        help="use the compressed Collatz operator (odd-core)")
    parser.add_argument("--csv", type=str, help="output CSV filename")

    args = parser.parse_args()

    # choose function
    f = collatz_pmax_compressed if args.compressed else collatz_pmax

    rows = []
    if args.n is not None:
        rows.append((args.n, f(args.n)))
    if args.list is not None:
        for n in args.list:
            rows.append((n, f(n)))

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fcsv:
            writer = csv.writer(fcsv)
            writer.writerow(["n", "P_max"])
            writer.writerows(rows)
        print(f"Results written to {args.csv}")
    else:
        for n, pmax in rows:
            mode = "Compressed" if args.compressed else "Classical"
            print(f"[{mode}] n={n}, P_max={pmax}")


