from sphericalquadpy.levelsymmetric.levelsymmetric import Levelsymmetric
import pytest


def test_levelsymmetric():
    Q = Levelsymmetric(order=4)

    assert Q.name() == "Levelsymmetric Quadrature"

    assert Q.getmaximalorder() == 20

    with pytest.raises(Exception):
        _ = Levelsymmetric(order=-10)

    Q = Levelsymmetric(nq=30)


def test_invalid():
    Q = Levelsymmetric(order=4)
    with pytest.raises(Exception):
        _ = Q.computequadpoints(234234234234)
    with pytest.raises(Exception):
        _ = Q.computequadweights(234234234234)
