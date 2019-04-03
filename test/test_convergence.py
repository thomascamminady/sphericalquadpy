from numpy import zeros, savetxt, stack
from .functioncollection_cartesian import f1, f2, f3
from sphericalquadpy.montecarlo.montecarlo import MonteCarlo


def test_convergence():
    n = [10 ** k for k in range(6)]
    errors = zeros(len(n))

    def func(x, y, z):
        return f1(x, y, z)[0]

    truevalue = f1(0, 0, 0)[1]
    for i, order in enumerate(n):
        Q = MonteCarlo(order)
        computedvalue = Q.integrate([func])
        error = abs(truevalue - computedvalue)
        print(error)
        errors[i] = error
    relerrors = errors / truevalue
    savetxt("output/errors.txt", stack([n, errors], axis=1))
    savetxt("output/relerrors.txt", stack([n, relerrors], axis=1))

    # TODO: create plots


def test_convergence_under_random_rotations():
    pass
