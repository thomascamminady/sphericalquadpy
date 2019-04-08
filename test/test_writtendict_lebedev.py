from sphericalquadpy.lebedev.writtendict import lebedevdictionary
from sphericalquadpy.lebedev.createxyzwdict import createdict, writedict
import os
from numpy import pi
from numpy.linalg import norm


def test_writedictionaryworks():
    os.chdir("../sphericalquadpy/lebedev/")
    writedict()
    d1 = createdict()
    d2 = lebedevdictionary()

    orders = [
        3,
        5,
        7,
        9,
        11,
        13,
        15,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        35,
        41,
        47,
        53,
        59,
        65,
        71,
        77,
        83,
        89,
        95,
        101,
        107,
        113,
        119,
        125,
        131,
    ]
    for order in orders:
        a = norm(d1[order])
        b = norm(d2[order])
        assert abs(a - b) < 1e-12
    os.chdir("../../test")


def test_dictionary_correct():
    d = lebedevdictionary()
    orders = [
        3,
        5,
        7,
        9,
        11,
        13,
        15,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        35,
        41,
        47,
        53,
        59,
        65,
        71,
        77,
        83,
        89,
        95,
        101,
        107,
        113,
        119,
        125,
        131,
    ]
    for order in orders:
        assert order in d
        q = d[order]
        assert abs(sum(q[:, 3]) - 4 * pi) < 1e-12
