

def calculate_total_cost(price_list):
    """
    Calculate the total cost of items in a given price list.

    Args:
        price_list (list): A list of prices for items.

    Returns:
        float: The total cost of the items.
    """
    total_cost = 0
    for price in price_list:
        total_cost += price
    return total_cost