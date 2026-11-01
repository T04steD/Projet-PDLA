from functools import partial

from arithmp.parser import Parser


def test_add():
    parse = partial(Parser().parse, None)
    assert parse("1 + 1") == 2
    assert parse("0 + 3") == 3
