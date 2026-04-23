from garage import calculate_fee
import pytest


def test_calculate_fee():
    assert calculate_fee(3,5) == 15


def test_calculate_fee_value_error():
    with pytest.raises(ValueError):
        calculate_fee(-3,5)