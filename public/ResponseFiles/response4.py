

def get_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Args:
        numbers (list): List of numbers to sum.

    Returns:
        int: The sum of the numbers.
    """
    sum_val = 0
    for num in numbers:
        sum_val += num
    return sum_val