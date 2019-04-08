from sphericalquadpy.lebedev.lebedev import Lebedev
import pytest


def test_lebedev():
    Q = Lebedev(order=3)

    assert Q.name() == "Lebedev Quadrature"

    assert Q.getmaximalorder() == 131

    with pytest.raises(Exception):
        _ = Lebedev(order=-10)

    Q = Lebedev(nq=100000000)  # maximal order


def test_emptyquadrature():
    Q = Lebedev(nq=-1)


def test_maxquadrature():
    Q = Lebedev(order=131)


def test_invalid():
    Q = Lebedev(order=3)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(234234234234)
