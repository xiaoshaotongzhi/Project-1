import math
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
        self.n = int(25214903917 * self.n + 11) & int(2 ** 48 - 1)
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
    def __init__(self, p: str, s: str, cpu_b: bool) -> None:
        self.pid = p
        self.state = s
        self.arrival = None 
        self.cpu_bound = cpu_b
        self.burst_num = None
        # self.bursts = []


class CPU:
    def __init__(self, n: int, ncpu: int, s: int, l: float, ub: int, r: Rand48) -> None:
        self.num_proc = n
        self.num_proc_cpu = ncpu
        self.seed_val = s
        self.lambda_val = l
        self.up_bound = ub
        self.r = Rand48(s)
        self.util_time = 0


    def debug_print(self) -> None:
        print("n: {}, ncpu: {}, seed: {}, lam: {}, upperBound: {}"
            .format(self.num_proc, self.num_proc_cpu, self.seed_val,
                    self.lambda_val, self.up_bound))

    def next_exp(self) -> float:
        x = -math.log(self.r.drand())/self.lambda_val
        while x > self.up_bound:
            x = -math.log(self.r.drand())/self.lambda_val
        return x

    def run_all(self) -> None:
        print("<<< PROJECT PART I -- process set (n={}) with {} CPU-bound process >>>".format(self.num_proc, self.num_proc_cpu))
        for i in range(self.num_proc):
            p = Process(chr(i+65), "idk", (i >= self.num_proc - self.num_proc_cpu))
            self.run_process(p)

    def run_process(self, p: Process) -> None:
        p.arrival = math.floor(self.next_exp())
        p.burst_num = math.ceil(100*self.r.drand())
        if p.cpu_bound:
            print("CPU-bound process {}: arrival time {}ms; {} CPU bursts:".format(p.pid, p.arrival,p.burst_num))
        else:
            print("I/O-bound process {}: arrival time {}ms; {} CPU bursts:".format(p.pid, p.arrival,p.burst_num))

        for i in range(p.burst_num):
            cpu_burst = math.ceil(self.next_exp())
            io_burst = 10* math.ceil(self.next_exp())
            if p.cpu_bound:
                cpu_burst = math.ceil(4*self.next_exp())
                io_burst = math.ceil(10*self.next_exp()/4)
            if i == p.burst_num-1:
                print("--> CPU burst {}ms".format(cpu_burst))
            else:
                print("--> CPU burst {}ms --> I/O burst {}ms".format(cpu_burst, io_burst))


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
    seed = int(sys.argv[3])       # seed value for random number seq.
    lam = float(sys.argv[4])        # exp. distribution lambda value
    upper_bound = int(sys.argv[5])  # upper bound for valid random nums

    if ncpu > n:
        print("ERROR!")
        return

    r = Rand48(seed)
    r.srand(seed)
    cpu = CPU(n, ncpu, seed, lam, upper_bound,r)
    cpu.run_all()


if __name__ == "__main__":
    main()