import matplotlib.pyplot as plt
from timeit import timeit
import random
from collections.abc import Callable, Iterator, Iterable
import functools
from stupidsort import stupidsort


def input_arrays(n: int=1_000, N: int=1_000, repl: bool=True) -> Iterator[list[int]]:
    l=[]

    for i in range(0,n-1):
        if repl:
            l = random.choices(range(N), k=size)
        else:
        # Tirage sans remise : sample impose size ≤ N
            l = random.sample(range(N), k=size)
    yield l
    pass


def plot_array(array: list[float], title: str, log: bool = False) -> None:
    plt.title(title)
    plt.semilogy(array) if log else plt.plot(array)
    plt.show()


def timeit_batch(fun: Callable, inputs: Iterable, setup: str='pass', cumul: int = 10) -> list[float]:
    return [timeit( f'{fun.__name__}({arg})',
                    setup=setup,
                    globals=globals(),
                    number=cumul) for arg in inputs]


def sum_reduce(t):
    def function(x, y):
        return x + y

    return functools.reduce(function, t, 0)


if __name__ == '__main__':
    # "scénario jouet" de parangonnage, à adapter au fur et à mesure du TP
    input_arrs = [list(range(100)) for _ in range(20)]
    result: list[float] = timeit_batch(sum, input_arrs, cumul=4)
    print(result)
    plot_array(array=result, title="sum", log=False)
    # Benchmark sum_reduce
    result2: list[float] = timeit_batch(sum_reduce, input_arrs, cumul=4)
    print(result2)
    plot_array(array=result2, title="sumred", log=False)
    print(stupidsort([2,5,2,444,111,0,2,7,88,3]))
