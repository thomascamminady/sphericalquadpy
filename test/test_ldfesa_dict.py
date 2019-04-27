from sphericalquadpy.ldfesa.createxyzwdict import createdict, writedict
from sphericalquadpy.ldfesa.writtendict import ldfesadictionary
import os

from numpy import pi
from numpy.linalg import norm


def test_writedictionaryworks():
    os.chdir("../sphericalquadpy/ldfesa/")
    writedict()
    d1 = createdict()
    d2 = ldfesadictionary()

    orders = [1, 2, 3]

    for order in orders:
        a = norm(d1[order])
        b = norm(d2[order])
        assert abs(a - b) < 1e-12
    os.chdir("../../test")


def test_dictionary_correct():
    d = ldfesadictionary()
    orders = [1, 2, 3]
    for order in orders:
        assert order in d
        q = d[order]
        assert abs(sum(q[:, 3]) - 4 * pi) < 1e-12
