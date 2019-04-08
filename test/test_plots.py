import sys

sys.path.append('../')
import sphericalquadpy
import matplotlib.pyplot as plt
from numpy import zeros, exp, mean, var
from sphericalquadpy.tools.rotations import randomrotate


def getquadraturelist():
    mc = sphericalquadpy.montecarlo.montecarlo.MonteCarlo
    leb = sphericalquadpy.lebedev.lebedev.Lebedev
    ls = sphericalquadpy.levelsymmetric.levelsymmetric.Levelsymmetric
    quads = [mc, leb, ls]
    return quads


def gettestcase(i=1):
    if i == 0:
        def f(x, y, z):
            return exp(-z * z)

        refintegral = 9.38486877222642
        name = "exp(-z^2)"
        return f, refintegral, name

    if i == 1:
        def f(x, y, z):
            return exp(-z * z * 10)

        refintegral = 3.521692537170621
        name = "exp(-10z^2)"
        return f, refintegral, name


def create_plot(result, legends):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    ax.set_xscale('log')

    for i, _ in enumerate(legends):
        meanerr = mean(result[i, :, 1:], axis=1)
        varerr = var(result[i, :, 1:], axis=1)

        ax.errorbar((result[i, :, 0]), meanerr,
                    yerr=varerr, capthick=2)
    ax.legend(legends)
    ax.set_xlabel("Number of quadrature points")
    ax.set_ylabel("Mean relative error with variance ")
    _, _, name = gettestcase()
    ax.set_title(
        "Integration of {} over the unit sphere\nfor 100 randomly rotated samples".format(
            name))
    ax.grid(True, linewidth=0.5)
    plt.savefig("convergence1.png")
    plt.show()


def test_plots():
    quads = getquadraturelist()
    f, refintegral, _ = gettestcase()

    nqs = [2 * (k + 1) for k in range(130)]
    nrotations = 100
    results = zeros((len(quads), len(nqs), 1 + nrotations))
    legends = []
    for i, quad in enumerate(quads):
        for j, nq in enumerate(nqs):
            q = quad(nq=nq)
            if j == 0:
                legends.append(q.name())
            for k in range(nrotations):
                q.xyz = randomrotate(q.xyz)
                val = abs(q.integrate(f) - refintegral) / abs(refintegral)
                realnq = len(q.weights)
                results[i, j, 0] = realnq
                results[i, j, 1 + k] = val

    create_plot(results, legends)


test_plots()
