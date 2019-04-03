from numpy import pi
from numpy.random import seed
from sphericalquadpy.montecarlo.montecarlo import MonteCarlo


# remove randomness for different test runs
seed(12345)


def test_quadratureweights_sum_to_4pi():
    Q = MonteCarlo(10)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12

    Q = MonteCarlo(200)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12

    Q = MonteCarlo(4000)
    assert abs(sum(Q.weights) - 4 * pi) < 1e-12


def test_integration_decreasewithorder_singlefunction_but_as_array():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(1)
    v1 = Q1.integrate([f])

    Q2 = MonteCarlo(20)
    v2 = Q2.integrate([f])

    Q3 = MonteCarlo(400)
    v3 = Q3.integrate([f])

    Q4 = MonteCarlo(80000)
    v4 = Q4.integrate([f])

    assert abs(v1[0]) > abs(v2[0]) > abs(v3[0]) > abs(v4[0])
    assert abs(v4[0]) < 1e-2


def test_integration_decreasewithorder_singlefunction():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(1)
    v1 = Q1.integrate(f)

    Q2 = MonteCarlo(20)
    v2 = Q2.integrate(f)

    Q3 = MonteCarlo(400)
    v3 = Q3.integrate(f)

    Q4 = MonteCarlo(80000)
    v4 = Q4.integrate(f)

    assert abs(v1) > abs(v2) > abs(v3) > abs(v4)
    assert abs(v4) < 1e-2


def test_integration_decreasewithorder():
    def f(x, y, z):
        return x * y * z

    Q1 = MonteCarlo(1000000)
    v1 = Q1.integrate([f])

    assert abs(v1[0]) < 1e-2


def test_integration_multiple_functions():
    def f(x, y, z):
        return x * y * z

    def g(x, y, z):
        return x * y * z * z * z

    Q1 = MonteCarlo(1000000)
    v1 = Q1.integrate([f, g])

    assert abs(v1[0]) < 1e-2
    assert abs(v1[1]) < 1e-2


def test_relation_order_quadpoints():
    Q1 = MonteCarlo(1000000)
    # mapping for Monte Carlo is one to one
    assert 100 == Q1.getcorrespondingorder(100)
