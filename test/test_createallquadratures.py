from sphericalquadpy.montecarlo.montecarlo import MonteCarlo
from sphericalquadpy.lebedev.lebedev import Lebedev
from sphericalquadpy.levelsymmetric.levelsymmetric import Levelsymmetric
from numpy import pi


def test_createallquadratures():
    Qs = [MonteCarlo, Lebedev, Levelsymmetric]

    # by nq
    for Q in Qs:
        q = Q(nq=50)
        assert abs(sum(q.weights) - 4 * pi) < 1e-12


    # by order
    q = MonteCarlo(order=10)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12

    q = Lebedev(order=13)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12

    q = Levelsymmetric(order=8)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12
