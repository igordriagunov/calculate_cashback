def calculate_cashback(purchase_amount, purchase_category):

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
