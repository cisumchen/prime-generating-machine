# src/collatz_prime_path.py
import argparse

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
    return max(pmax, 2)  # every path eventually meets 2 or 5


def collatz_pmax_compressed(n: int) -> int:
    """Compute P_max(n) under the compressed Collatz operator (odd-core)"""
    # remove initial powers of 2
    while n % 2 == 0:
        n //= 2

    pmax = 0
    while n != 1:
        if is_prime(n) and n > pmax:
            pmax = n
        m = 3 * n + 1
        # compute r = v2(m)
        r = 0
        while m % 2 == 0:
            m //= 2
            r += 1
        n = m
    return max(pmax, 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collatz Prime Generator")
    parser.add_argument("--n", type=int, required=True, help="starting integer n")
    parser.add_argument("--compressed", action="store_true",
                        help="use the compressed Collatz operator (odd-core)")
    args = parser.parse_args()

    if args.compressed:
        result = collatz_pmax_compressed(args.n)
        print(f"[Compressed] P_max({args.n}) = {result}")
    else:
        result = collatz_pmax(args.n)
        print(f"[Classical] P_max({args.n}) = {result}")
