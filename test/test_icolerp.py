from sphericalquadpy.icolerp.icolerp import Icolerp
import pytest
from numpy import pi, inf


def test_lebedev():
    Q = Icolerp(nq=100)

    assert Q.name() == "Icolerp Quadrature"

    assert Q.getmaximalorder() == 40

    xyz = Q.computequadpoints(10)
    w = Q.computequadweights(10)

    nq = Q.nqbyorder(10)

    assert len(w) == nq[1]


def test_weights():
    Q = Icolerp(nq=100)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-10


def test_invalid():
    with pytest.raises(Exception):
        Q = Icolerp(order=3)


def test_invalid2():
    Q = Icolerp(order=4)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(-234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(-234234234234)
