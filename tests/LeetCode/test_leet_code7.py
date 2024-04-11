import pytest
from src.LeetCode.leet_code7 import smallest_repunit_div_by_k  # type: ignore


@pytest.mark.parametrize("k, excepted", ((1, 1), (2, -1), (3, 3), (19927, 19926), (42413, 984), (49993, 49992)))
def test_smallest_repunit_div_by_k(k, excepted):
    assert smallest_repunit_div_by_k(k) == excepted
