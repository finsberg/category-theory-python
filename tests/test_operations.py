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
