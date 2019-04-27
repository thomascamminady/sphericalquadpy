from sphericalquadpy.dummy.dummy import Dummy
import pytest
from numpy import inf, pi


def test_dummy():
    Q = Dummy(order=1)

    assert Q.name() == "Dummy Quadrature"

    assert Q.getmaximalorder() == inf

    assert Q.getcorrespondingorder(1) == 1

    assert Q.computequadpoints(1) == 1

    assert Q.computequadweights(1) == 1
