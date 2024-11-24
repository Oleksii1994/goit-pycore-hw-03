import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the standard format, leaving only digits and the '+' symbol at the start.
    If the number does not contain an international code, it automatically adds the code '+38'.

    phone_number: A string containing the phone number in various formats.
    A normalized phone number string.
    """
    # remove all characters except digits and '+'
    correct_number = re.sub(r'[^\d+]', '', phone_number)
    
    # check if the number starts with '+'
    if not correct_number.startswith('+'):
        # if the number starts with '380', add '+'
        if correct_number.startswith('380'):
            correct_number = '+' + correct_number
        else:
            # add the international code '+38'
            correct_number = '+38' + correct_number
    
    return correct_number

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

# iterate through each phone number in the list
for number in phone_numbers:
    normalized_number = normalize_phone(number)
    print("Normalized:", normalized_number)
    