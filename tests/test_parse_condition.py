import pytest
from parse_condition import parse_condition


@pytest.mark.parametrize("where_str,expected", [
    ("price>100", ('price', '>', '100')),
    ("brand=apple", ('brand', '=', 'apple')),
    ("rating<5", ('rating', '<', '5')),
])
def test_parse_condition_valid(where_str, expected):
    assert parse_condition(where_str) == expected


@pytest.mark.parametrize("invalid_string", [
    "price is 100",
    "brand==apple",
    "rating<=5",
    "=apple",
    "brand>"
])
def test_parse_condition_invalid(invalid_string):
    with pytest.raises(ValueError):
        parse_condition(invalid_string)
