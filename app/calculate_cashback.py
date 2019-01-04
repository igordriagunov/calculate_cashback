def calculate_cashback(amount, category):
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

    standart_category = 1
    upper_category = 2
    special_category = 3

    limit = 3_000

    if category == standart_category:
        result = amount * standart_cashback
        return result_or_limit(result, limit)

    if category == upper_category:
        result = amount * upper_cashback
        return result_or_limit(result, limit)

    if category == special_category:
        result = amount * special_cashback
        return result_or_limit(result, limit)

    else:
        return 0


def result_or_limit(result, limit):
    if result >= limit:
        return limit
    return result
