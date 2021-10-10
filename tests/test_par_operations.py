from category_theory import par_operations as parop


def test_chunkify():
    iterable = (1, 2, 3, 4, 5)
    chunks = parop.chunkify(3, iterable, fillvalue=None)
    assert tuple(chunks) == ((1, 2, 3), (4, 5, None))
