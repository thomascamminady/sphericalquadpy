from sphericalquadpy.ldfesa.ldfesa import LDFESA
from numpy import pi
import pytest


def test_ldfesa():
    Q = LDFESA(order=1)

    assert Q.name() == "LDFESA Quadrature"

    assert Q.getmaximalorder() == 3

    xyz = Q.computequadpoints(3)
    w = Q.computequadweights(3)

    nq = Q.nqbyorder(3)

    assert len(w) == nq[1]


def test_weights():
    Q = LDFESA(nq=100)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-10


def test_invalid():
    with pytest.raises(Exception):
        Q = LDFESA(order=4)


def test_invalid2():
    Q = LDFESA(order=3)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(-234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(-234234234234)
