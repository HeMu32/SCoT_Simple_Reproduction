def loss_amount(actual_cost, sale_amount):
    difference = actual_cost - sale_amount
    if difference > 0:
        return difference
    else:
        return None