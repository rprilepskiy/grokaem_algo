import pytest
from chapter_2.binary_search import binary_search

@pytest.mark.parametrize("item, expected", [
    (3, 3),
    (2, None),
    (5, 5),
    (7, 7),
    (9, 9),
    (0, None),
    (10, None),
    (-1, None)
])
def test_binary_search(sorted_list, item, expected):
    # Test a case where the item is present in the list
    assert binary_search(sorted_list, item) == expected

@pytest.mark.parametrize("item", [1, 50, 100])
def test_binary_search_100(list_100, item):
    assert binary_search(list_100, item) == item


@pytest.mark.parametrize("item", [1, 500000, 1000000])
def test_binary_seach_1000000(list_1000000, item):
    assert binary_search(list_1000000, item) == item