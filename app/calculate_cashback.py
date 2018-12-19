def calculate_cashback(purchase_amount, purchase_category):
    """
    >>> calculate_cashback(0, 0)
    0
    >>> calculate_cashback(1_000, 0)
    0
    >>> calculate_cashback(0, 1)
    0.0
    >>> calculate_cashback(5_000, 1)
    50.0
    >>> calculate_cashback(300_001, 1)
    3000
    >>> calculate_cashback(5_000, 2)
    250.0
    >>> calculate_cashback(60_005, 2)
    3000
    >>> calculate_cashback(10_004, 3)
    3000
    """
    standart_cashback = 0.01
    upper_cashback = 0.05
    special_cashback = 0.3

    standart_buying_category = 1
    upper_buying_category = 2
    special_buying_category = 3

    limit = 3_000

    if purchase_category == standart_buying_category:
        result = purchase_amount * standart_cashback
        if result >= limit:
            return limit
        return result

    if purchase_category == upper_buying_category:
        result = purchase_amount * upper_cashback
        if result >= limit:
            return limit
        return result

    if purchase_category == special_buying_category:
        result = purchase_amount * special_cashback
        if result >= limit:
            return limit
        return result

    else:
        return 0


print(calculate_cashback(50000, 1))
