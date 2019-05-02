from sphericalquadpy.gausslegendre.gausslegendre import GaussLegendre
import pytest
from numpy import pi, inf


def test_icolerp():
    Q = GaussLegendre(order=2)

    assert Q.name() == "GaussLegendre Quadrature"

    assert Q.getmaximalorder() == inf

    xyz = Q.computequadpoints(10)
    w = Q.computequadweights(10)

    nq = Q.nqbyorder(10)

    assert len(w) == nq[1]


def test_weights():
    Q = GaussLegendre(order=10)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-10


def test_invalid():
    Q = GaussLegendre(order=3)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(234234234234)
