import sys
import typing


class Rand48(object):
    def __init__(self, seed):
        self.n = seed

    def seed(self, seed):
        self.n = seed

    def srand(self, seed):
        self.n = (seed << 16) + 0x330e

    def next(self):
        self.n = (25214903917 * self.n + 11) & (2 ** 48 - 1)
        return self.n

    def drand(self):
        return self.next() / 2 ** 48

    def lrand(self):
        return self.next() >> 17

    def mrand(self):
        n = self.next() >> 16
        if n & (1 << 31):
            n -= 1 << 32
        return n


def isfloat(num: typing.Any) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


class CPUBurst:
    def __init__(self, ats: float, ate: float, cts: float, cte: float) -> None:
        self.arrv_t_start = ats
        self.arrv_t_end: ate
        self.comp_t_start: cts
        self.comp_t_end: cte


class Process:
    def __init__(self, p: str, s: str) -> None:
        self.pid = p
        self.state = s


class CPU:
    def __init__(self, n: int, ncpu: int, s: float, l: float, ub: int) -> None:
        self.num_proc = n
        self.num_proc_cpu = ncpu
        self.seed_val = s
        self.lambda_val = l
        self.up_bound = ub

    def debug_print(self):
        print("n: {}, ncpu: {}, seed: {}, lam: {}, upperBound: {}"
            .format(self.num_proc, self.num_proc_cpu, self.seed_val,
                    self.lambda_val, self.up_bound))


def main():
    if ((len(sys.argv) != 6)
            or (not sys.argv[1].isdigit())
            or (not sys.argv[2].isdigit())
            or (not isfloat(sys.argv[3]))
            or (not isfloat(sys.argv[4]))
            or (not sys.argv[2].isdigit())):
        print("ERROR!");
        return

    n = int(sys.argv[1])            # number of processes to simulate 
    ncpu = int(sys.argv[2])         # number of CPU bound processes
    seed = float(sys.argv[3])       # seed value for random number seq.
    lam = float(sys.argv[4])        # exp. distribution lambda value
    upper_bound = int(sys.argv[5])  # upper bound for valid random nums

    cpu = CPU(n, ncpu, seed, lam, upper_bound)
    cpu.debug_print()


if __name__ == "__main__":
    main()