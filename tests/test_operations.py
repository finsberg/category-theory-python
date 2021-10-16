import pytest
from category_theory import operations as op
from hypothesis import given
from hypothesis import strategies as st


@pytest.mark.parametrize(
    "f, g, h",
    [
        (lambda x: x + 2, lambda x: x - 4, lambda x: x - 2),
        (
            lambda x: (x + 1) ** 2,
            lambda x: 2 * (x + 1),
            lambda x: 2 * ((x + 1) ** 2 + 1),
        ),
    ],
)
@given(st.integers())
def test_compose(f, g, h, value):
    gf = op.compose(g, f)
    assert gf(value) == h(value)


@pytest.mark.parametrize(
    "x, expected",
    [
        (None, True),
        (float("nan"), True),
        (float("inf"), True),
        (1, False),
        (0, False),
        ("", False),
        (False, False),
        (True, False),
    ],
)
def test_is_nothing(x, expected):
    assert op.is_nothing(x) is expected
