from chapter_2.binary_search import binary_search

def test_binary_search():
    # Test a case where the item is present in the list
    assert binary_search([1, 3, 5, 7, 9], 3) == 3

    # Test a case where the item is not present in the list
    assert binary_search([1, 3, 5, 7, 9], 2) is None

    # Test a case where the list is empty
    assert binary_search([], 1) is None

    # Test a case where the list has only one element
    assert binary_search([5], 5) == 5