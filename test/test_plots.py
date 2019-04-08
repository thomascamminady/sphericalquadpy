import sys

sys.path.append('../')
import sphericalquadpy
import matplotlib.pyplot as plt
from numpy import zeros, exp, mean, var
from sphericalquadpy.tools.rotations import randomrotate
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.special import sph_harm


def getquadraturelist():
    mc = sphericalquadpy.montecarlo.montecarlo.MonteCarlo
    leb = sphericalquadpy.lebedev.lebedev.Lebedev
    ls = sphericalquadpy.levelsymmetric.levelsymmetric.Levelsymmetric
    quads = [mc, leb, ls]
    return quads


def gettestcase(i=1):
    if i == 0:
        def f(x, y, z):
            return exp(z * 10)

        refintegral = 13839.63717474464
        name = "exp(10z)"
        return f, refintegral, name

    if i == 1:
        def f(x, y, z):
            return exp(-z * z * 10)

        refintegral = 3.521692537170621
        name = "exp(-10z^2)"
        return f, refintegral, name


def create_plot(result, legends, testcaseid):
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
    _, _, name = gettestcase(testcaseid)
    ax.set_title(
        "Integration of {} over the unit sphere\nfor 100 randomly rotated samples".format(
            name))
    ax.grid(True, linewidth=0.5)
    plt.savefig("convergence{}.png".format(testcaseid))
    plt.show()


def test_plots(testcaseid):
    quads = getquadraturelist()
    f, refintegral, _ = gettestcase(testcaseid)

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

    create_plot(results, legends, testcaseid)


def vissphericalharmonics(testcaseid):
    Theta = np.linspace(0, np.pi, 100)
    Phi = np.linspace(0, 2 * np.pi, 100)
    func, _, _ = gettestcase(testcaseid)
    fcolors = zeros((100, 100))
    for i in range(100):
        for j in range(100):
            phi = Phi[j]
            theta = Theta[i]
            x = np.sin(phi) * np.cos(theta)
            y = np.sin(phi) * np.sin(theta)
            z = np.cos(phi)

            fcolors[i, j] = func(x, y, z)

    fmax, fmin = fcolors.max(), fcolors.min()
    fcolors = (fcolors - fmin) / (fmax - fmin)

    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    # The Cartesian coordinates of the unit sphere
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    # Set the aspect ratio to 1 so our sphere looks spherical
    fig = plt.figure(figsize=plt.figaspect(1.))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    facecolors=cm.seismic(fcolors))
    # Turn off the axis planes
    ax.set_axis_off()
    plt.savefig("function{}.png".format(testcaseid))
    plt.show()


i = 0
test_plots(i)
vissphericalharmonics(i)
