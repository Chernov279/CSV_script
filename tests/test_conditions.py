import pytest
from conditions import filter_rows, aggregate


@pytest.fixture
def sample_data():
    return [
        {'name': 'iphone', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'iphone 6', 'brand': 'apple', 'price': '199', 'rating': '4.6'},
    ]


def test_filter_numeric_equal(sample_data):
    result = filter_rows(sample_data, 'price', '=', '999')
    assert len(result) == 1
    assert result[0]['name'] == 'iphone'


def test_filter_numeric_greater(sample_data):
    result = filter_rows(sample_data, 'price', '>', '900')
    assert len(result) == 2
    assert result[0]['brand'] == 'apple'
    assert result[-1]['rating'] == '4.8'


def test_filter_numeric_less(sample_data):
    result = filter_rows(sample_data, 'rating', '<', '4.6')
    assert len(result) == 0


def test_filter_string_equal(sample_data):
    result = filter_rows(sample_data, 'brand', '=', 'apple')
    assert len(result) == 2
    assert result[0]['name'] == 'iphone'
    assert result[-1]['price'] == '199'


def test_filter_numeric_on_text_column_fails(sample_data):
    with pytest.raises(ValueError):
        filter_rows(sample_data, 'brand', '>', 'apple')


def test_aggregate_avg(sample_data):
    assert aggregate(sample_data, 'price', 'avg') == pytest.approx((999 + 1199 + 199) / 3, rel=1e-3)


def test_aggregate_min(sample_data):
    assert aggregate(sample_data, 'rating', 'min') == 4.6


def test_aggregate_max(sample_data):
    assert aggregate(sample_data, 'rating', 'max') == 4.9


def test_aggregate_on_non_numeric_column(sample_data):
    with pytest.raises(ValueError):
        aggregate(sample_data, 'brand', 'avg')


def test_aggregate_not_existing_column(sample_data):
    with pytest.raises(KeyError):
        aggregate(sample_data, 'country', 'avg')


def test_aggregate_empty_rows(sample_data):
    assert aggregate([], 'rating', 'avg') is None
