from garage import calculate_fee

def test_calculate_fee():
    assert calculate_fee(3,5) == 15