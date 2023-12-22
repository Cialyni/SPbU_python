import warnings

import pytest
from io import StringIO
from src.Tests.final_rewirte.safe_call import safe_call


@pytest.mark.parametrize(
    "func, expected",
    (
        (lambda x="aboba": int(x), None),
        (lambda: int(1 / 0), None),
        (lambda x="prnt(int(1))": eval(x), None),
        (lambda x="int(13)": eval(x), 13),
        (lambda x=5: x / 10, 0.5),
    ),
)
def test_return_with_safe_call(func, expected):
    func = safe_call(func)
    assert func() == expected


def test_checking_warning_cast():
    with pytest.warns(Warning):
        safe_call(lambda: int(1 / 0))()
    with pytest.warns(Warning):
        safe_call(lambda x="aboba": int(x))()
    with pytest.warns(Warning):
        safe_call(lambda x="prnt(int(1))": eval(x))()


def test_warning_format():
    with warnings.catch_warnings(record=True) as w:
        safe_call(lambda x="aboba": int(x))()
        assert (
            "Error type" in str(*w)
            and "Error text" in str(*w)
            and "Error place" in str(*w)
            and "UserWarning" in str(*w)
        ) == True
