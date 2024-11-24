import random
from typing import List

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates a set of unique random numbers within a specified range.
    min: Minimum possible number in the set (at least 1).
    max: Maximum possible number in the set (up to 1000).
    quantity: Number of unique numbers to select (between min and max).
    A sorted list of unique random numbers.
    Returns an empty list if the parameters are not valid.
    """
    # validate parameters
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # generate unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Sort the numbers
    numbers.sort()
    
    return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)