import sys
import typing


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