from sphericalquadpy.octalerp.octalerp import Octalerp
import pytest
from numpy import pi, inf


def test_lebedev():
    Q = Octalerp(nq=100)

    assert Q.name() == "Octalerp Quadrature"

    assert Q.getmaximalorder() == 80

    xyz = Q.computequadpoints(10)
    w = Q.computequadweights(10)

    nq = Q.nqbyorder(10)

    assert len(w) == nq[1]


def test_weights():
    Q = Octalerp(nq=100)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-10


def test_invalid():
    with pytest.raises(Exception):
        Q = Octalerp(order=3)


def test_invalid2():
    Q = Octalerp(order=4)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(-234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(-234234234234)
