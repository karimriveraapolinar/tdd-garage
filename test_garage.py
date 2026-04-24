from garage import calculate_fee, enter_garage
import pytest


def test_calculate_fee():
    assert calculate_fee(3,5) == 15


def test_calculate_fee_value_error():
    with pytest.raises(ValueError):
        calculate_fee(-3,5)

def test_calculate_fee_type_error():
    with pytest.raises(TypeError):
        calculate_fee(3,"hello")


def test_enter_garage():
    garage1 = {"capacity": 10, "cars": {}}
    enter_garage(garage1, 'Bugatti17', 13)
    assert 'Bugatti17' in garage1['cars'].keys()


def test_enter_garage_value_error():
    with pytest.raises(ValueError):
        garage1 = {"capacity": 0, "cars": {}}
        enter_garage(garage1, 'Bugatti17', 13)

def test_enter_garage_type_error():
    with pytest.raises(TypeError):
        garage1 = {"capacity": 10, "cars": {}}
        enter_garage(garage1, 'Bugatti17', "thirteen")