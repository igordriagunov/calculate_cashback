import pytest

from app.calculate_cashback import calculate_cashback


@pytest.mark.parametrize('purchase_amount, purchase_category, expected', [
    (0, 0, 0),
    (100_000, 0, 0),
    (0, 1, 0),
    (5_000, 1, 50),
    (300_001, 1, 3_000),
    (5_000, 2, 250),
    (60_005, 2, 3_000),
    (1_000, 3, 300),
    (10_005, 3, 3_000),
])
def test_calculate_cashback(purchase_amount, purchase_category, expected):
    actual = calculate_cashback(purchase_amount, purchase_category)
    assert expected == actual
