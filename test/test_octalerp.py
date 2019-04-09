from sphericalquadpy.octalerp.octalerp import Octalerp
import pytest


def test_Octalerp():
    Q = Octalerp(order=2)

    print(Q.xyz)


test_Octalerp()
