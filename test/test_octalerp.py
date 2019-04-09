from sphericalquadpy.octalerp.octalerp import Octalerp
from sphericalquadpy.octaslerp.octaslerp import Octaslerp
import pytest
import os


def test_Octalerp():
    Q = Octalerp(order=4)

    print(Q.xyz)


def test_Octaslerp():
    Q = Octaslerp(order=4)

    print(Q.xyz)


test_Octalerp()

test_Octaslerp()
