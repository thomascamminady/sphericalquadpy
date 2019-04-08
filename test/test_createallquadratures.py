from sphericalquadpy.montecarlo.montecarlo import MonteCarlo
from sphericalquadpy.lebedev.lebedev import Lebedev
from sphericalquadpy.levelsymmetric.levelsymmetric import Levelsymmetric
from numpy import pi
import pytest

"""
def test_createallquadratures():
    Qs = [MonteCarlo, Lebedev, Levelsymmetric]

    # by nq
    for Q in Qs:
        q = Q(nq=10)
        assert abs(sum(q.weights) - 4 * pi) < 1e-12

        with pytest.raises(Exception):
            _ = q.computequadpoints(-123)
            _ = q.computequadpoints(-123)

    # by order
    q = MonteCarlo(order=10)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12

    q = Lebedev(order=3)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12

    q = Levelsymmetric(order=4)
    assert abs(sum(q.weights) - 4 * pi) < 1e-12


def test_lebedevexception():
    q = Lebedev(order=3)
    with pytest.raises(Exception):
        _ = q.computequadweights(order=-10)

    with pytest.raises(Exception):
        _ = q.computequadpoints(order=-10)


def test_levelsymexception():
    q = Levelsymmetric(order=4)
    with pytest.raises(Exception):
        _ = q.computequadpoints(order=-10)

    with pytest.raises(Exception):
        _ = q.computequadweights(order=-10)
"""
