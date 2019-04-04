from numpy import zeros, savetxt, reshape, ones, concatenate
from .functioncollection_cartesian import f1, f2, f3
from sphericalquadpy.montecarlo.montecarlo import MonteCarlo


def test_convergence():
    n = [10 ** k for k in range(6)]
    functions = [f1, f2, f3]
    errors = zeros((len(n), len(functions)))

    for pos, f in enumerate(functions):

        def func(x, y, z):
            return f(x, y, z)[0]

        truevalue = f(ones(3), zeros(3), zeros(3))[1]
        for i, nq in enumerate(n):
            Q = MonteCarlo(nq=nq)
            computedvalue = Q.integrate([func])
            error = abs(truevalue - computedvalue)
            print(error)
            errors[i, pos] = error
        relerrors = errors / truevalue
        savetxt("errors.txt", concatenate((reshape(n, (len(n), 1)), errors), axis=1))
        savetxt(
            "relerrors.txt", concatenate((reshape(n, (len(n), 1)), relerrors), axis=1)
        )

    # TODO: create plots


def test_convergence_under_random_rotations():
    pass