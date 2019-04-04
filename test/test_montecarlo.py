import pytest
from numpy import pi
from numpy.random import seed
from sphericalquadpy.montecarlo.montecarlo import MonteCarlo

# remove randomness for different test runs
seed(12345)


def test_quadratureweights_sum_to_4pi():
    Q = MonteCarlo(nq=10)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12

    Q = MonteCarlo(nq=200)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12

    Q = MonteCarlo(nq=4000)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12


def test_integration_decreasewithorder_singlefunction_but_as_array():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(nq=1)
    v1 = Q1.integrate([f])

    Q4 = MonteCarlo(nq=80000)
    v4 = Q4.integrate([f])

    assert abs(v1[0]) > abs(v4[0])


def test_integration_decreasewithorder_singlefunction():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(nq=1)
    v1 = Q1.integrate(f)

    Q4 = MonteCarlo(nq=80000)
    v4 = Q4.integrate(f)

    assert abs(v1) > abs(v4)


def test_integration_decreasewithorder():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(nq=1000000)
    v1 = Q1.integrate([f])

    assert abs(v1[0]) < 1e-2


def test_integration_multiple_functions():
    def f(x, y, z):
        return x * y * z

    def g(x, y, z):
        return x * y * z * z * z

    Q1 = MonteCarlo(nq=1000000)
    v1 = Q1.integrate([f, g])

    assert abs(v1[0]) < 1e-2
    assert abs(v1[1]) < 1e-2


def test_relation_order_quadpoints():
    Q1 = MonteCarlo(nq=1000000)
    # mapping for Monte Carlo is one to one
    assert 100 == Q1.getcorrespondingorder(100)


def test_keywords_of_quadrature():
    _ = MonteCarlo(nq=10)
    _ = MonteCarlo(order=10)

    with pytest.raises(Exception):
        _ = MonteCarlo(nq=10, order=10)

    with pytest.raises(Exception):
        _ = MonteCarlo(blabla=10)

    with pytest.raises(Exception):
        _ = MonteCarlo(order=-10)
