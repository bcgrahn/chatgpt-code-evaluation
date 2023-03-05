

def calculate_total_cost(price, tax_rate):
    """Calculate the total cost of an item given its price and tax rate.

    Args:
        price (float): The price of the item.
        tax_rate (float): The tax rate as a decimal (e.g. 0.08 for 8%).

    Returns:
        float: The total cost of the item.
    """
    total_cost = price * (1 + tax_rate)
    return total_cost