import sys

sys.path.append('../')
import sphericalquadpy
from numpy import zeros, exp, mean, var
from sphericalquadpy.tools.rotations import randomrotate
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from test.functioncollection_cartesian import gettestcase
import matplotlib
import pandas as pd
import seaborn as sns


def visconvergence(result, legends, func, refintegral, name):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    ax.set_xscale('log')

    for i, _ in enumerate(legends):
        meanerr = mean(result[i, :, 1:], axis=1)
        varerr = var(result[i, :, 1:], axis=1)

        # ax.errorbar((result[i, :, 0]), meanerr,
        #            yerr=varerr, capthick=2)
        ax.plot(result[i, :, 0], meanerr, linewidth=3)
        ax.fill_between(result[i, :, 0], meanerr,
                        meanerr + 3 * varerr,
                        alpha=0.2, linewidth=15, linestyle='dashdot',
                        antialiased=True)
    tmp = ax.get_ylim()
    print(tmp)
    plt.ylim(max(1e-6,min(tmp)),max(tmp))
    ax.legend(legends)
    ax.set_xlabel("Number of quadrature points")
    if refintegral == 0:
        ax.set_ylabel("Mean absolute error with variance ")
    else:
        ax.set_ylabel("Mean relative error with variance ")

    ax.set_title(
        r"Integration of ${}$ over the unit sphere".format(
            name) + "\n for 100 randomly rotated samples")
    ax.grid(True, linewidth=0.5)
    plt.savefig("figures/convergence{}.png".format(name).replace(" ", ""))
    plt.show()


def visfunctiononsphere(func, refintegral, name):
    Phi = np.linspace(0, np.pi, 100)
    Theta = np.linspace(0, 2 * np.pi, 100)
    fcolors = zeros((100, 100))
    for i in range(100):
        for j in range(100):
            phi = Phi[j]
            theta = Theta[i]
            x = np.sin(phi) * np.cos(theta)
            y = np.sin(phi) * np.sin(theta)
            z = np.cos(phi)

            fcolors[i, j] = func(x, y, z).real

    fmax, fmin = fcolors.max(), fcolors.min()
    fcolors = (fcolors - fmin) / (fmax - fmin)

    phi, theta = np.meshgrid(Phi, Theta)

    # The Cartesian coordinates of the unit sphere
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    # Set the aspect ratio to 1 so our sphere looks spherical
    fig = plt.figure(figsize=(10, 10), dpi=80, )
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    facecolors=plt.cm.Spectral_r(fcolors))
    fig.tight_layout()
    # Turn off the axis planes
    # ax.set_title(r"$f(x,y,z) = {}$".format(name))
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()

    ax.set_axis_off()

    plt.savefig("figures/function{}.png".format(name).replace(" ", ""),
                bbox_inches='tight')
    plt.show()


def getquadraturelist():
    mc = sphericalquadpy.montecarlo.montecarlo.MonteCarlo
    leb = sphericalquadpy.lebedev.lebedev.Lebedev
    ls = sphericalquadpy.levelsymmetric.levelsymmetric.Levelsymmetric
    ldfesa = sphericalquadpy.ldfesa.ldfesa.LDFESA
    gaussleg = sphericalquadpy.gausslegendre.gausslegendre.GaussLegendre
    octalerp = sphericalquadpy.octalerp.octalerp.Octalerp
    octaslerp = sphericalquadpy.octaslerp.octaslerp.Octaslerp
    icolerp = sphericalquadpy.icolerp.icolerp.Icolerp
    icoslerp = sphericalquadpy.icoslerp.icoslerp.Icoslerp

    quads = [mc, leb, gaussleg, ldfesa, octalerp, octaslerp, icolerp,
             icoslerp]
    return quads


def computeintegralonsphere(func, refintegral, name):
    quads = getquadraturelist()

    nqs = [2 ** k for k in range(2, 12)]
    nrotations = 1000
    results = zeros((len(quads), len(nqs), 1 + nrotations))
    legends = []
    for i, quad in enumerate(quads):
        for j, nq in enumerate(nqs):
            q = quad(nq=nq)
            if j == 0:
                legends.append(q.name())
            for k in range(nrotations):
                q.xyz = randomrotate(q.xyz)
                if refintegral == 0:
                    val = abs(q.integrate(func) - refintegral)
                else:
                    val = abs(q.integrate(func) - refintegral) / abs(
                        refintegral)
                realnq = len(q.weights)
                results[i, j, 0] = realnq
                results[i, j, 1 + k] = val

    visconvergence(results, legends, func, refintegral, name)


def computeweightratio():
    quads = getquadraturelist()
    nqs = [2 ** k for k in range(2, 12)]

    df = pd.DataFrame(columns=['name', 'nq', 'min', 'max', 'mean', 'var'])
    for quad in quads:
        print(quad)
        for i, nq in enumerate(nqs):
            q = quad(nq=nq)
            w = q.weights
            df.loc[-1] = [q.name(), len(w), min(w), max(w), mean(w), var(w)]
            df.index = df.index + 1  # shifting index
    df = df.drop_duplicates()
    df = df.sort_index()
    print(df)
    df.to_csv("quadrature_summary.csv")


def fulldf():
    quads = getquadraturelist()
    nqs = [2 ** k for k in range(2, 12)]

    df = pd.DataFrame(
        columns=['name', 'nq', 'id', 'weight', 'ratiotomin', 'ratiotomean',
                 'nqtimesw'])
    for quad in quads:
        print(quad)
        lastnq = 0
        for i, nq in enumerate(nqs):
            q = quad(nq=nq)
            ws = q.weights
            if len(ws) == lastnq:
                continue
            lastnq = len(ws)
            minweight = min(ws)
            meanweight = mean(ws)
            for j, w in enumerate(ws):
                df.loc[-1] = [q.name(), len(ws), j, w, w / minweight,
                              w / meanweight, w * len(ws)]

                df.index = df.index + 1  # shifting index
    df = df.sort_index()
    print(df)
    df.to_csv("quadrature_summary_full.csv")


font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}

matplotlib.rc('font', **font)
f
# computeweightratio()
# fulldf()
collection = [1, 2, 4, 5, 7, 8]
for i in collection:
    func, refintegral, name = gettestcase(i)
    computeintegralonsphere(func, refintegral, name)
    visfunctiononsphere(func, refintegral, name)
