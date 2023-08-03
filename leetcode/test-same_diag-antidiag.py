from typing import Tuple
def is_same_diag(coord1: Tuple[int], coord2: Tuple[int]) -> bool:
            # c1 same diag c2 <==> (z:= c1-c2 => z_1 = z_2)
            z = (coord1[0] - coord2[0], coord1[1] - coord2[1])
            return z[0] == z[1]
def is_same_anti_diag(coord1: Tuple[int], coord2: Tuple[int]) -> bool:
    # c1 same anti_diag c2 <==> (z:= c1-c2 => z_1 = -z_2)
    z = (coord1[0] - coord2[0], coord1[1] - coord2[1])
    return z[0] == -z[1]

def test_same_diag():
    coord1 = (2, 4)
    signs = [1, -1]
    for s in signs:
        for i in range(0, 5):
            coord2 = (2 + s*i, 4 + s*i)
            assert is_same_diag(coord1, coord2)


def test_same_anti_diag():
    coord1 = (2, 4)
    signs = [1, -1]
    for s in signs:
        for i in range(0, 5):
            coord2 = (2 - s*i, 4 + s*i)
            assert is_same_anti_diag(coord1, coord2)
