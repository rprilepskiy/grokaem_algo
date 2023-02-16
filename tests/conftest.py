import pytest
import numpy as np


@pytest.fixture()
def sorted_list():
    return [1, 3, 5, 7, 9]


@pytest.fixture
def list_100():
    return np.arange(1, 101, 1)


@pytest.fixture
def list_1000000():
    return np.arange(1, 1000001, 1)
