import sys
import typing


def isfloat(num: typing.Any) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


class Time:
    # TO DO: COMPARTMENTALIZE THIS CLASS!!
    time_create: float
    length: float
    name: str

    def __init__(self, tc: float, l: float; n: str) -> None:
        self.time_create = tc
        length = l
        name = n


def main():
    if (len(sys.argv) != 6)
            or (not sys.argv[1].isdigit())
            or (not sys.argv[2].isdigit())
            or (not isfloat(sys.argv[3]))
            or (not isfloat(sys.argv[4]))
            or (not sys.argv[2].isdigit()):
        # some sort of error handling here
        return -1

    n = int(sys.argv[1])           # number of processes to simulate 
    ncpu = int(sys.argv[2])        # number of CPU bound processes
    seed = float(sys.argv[3])      # seed value for random number seq.
    lam = float(sys.argv[4])       # exp. distribution lambda value
    upperBound = int(sys.argv[5])  # upper bound for valid random nums

    print("n: {}, ncpu: {}, seed: {}, lam: {}, upperBound: {}"
            .format(n, ncpu, seed, lam, upperBound))


if __name__ == "__main__":
    main()