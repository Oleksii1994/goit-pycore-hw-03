from datetime import datetime, timedelta, date
from typing import List, Dict

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Determines which colleagues have birthdays in the next 7 days, including today.
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday.

    :param users: A list of dictionaries, each containing the keys 'name' (str) and 'birthday' (str in 'YYYY.MM.DD' format).
    :return: A list of dictionaries with 'name' and 'congratulation_date' (str in 'YYYY.MM.DD' format).
    """
    today: date = datetime.today().date()  # Типізація змінної
    end_date: date = today + timedelta(days=7)
    upcoming_birthdays: List[Dict[str, str]] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # adapt the birthday date to the current year
        birthday_this_year = birthday.replace(year=today.year)

        # if the birthday has already passed this year, check the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # check if the birthday is within the next 7 days
        if today <= birthday_this_year <= end_date:
            # if the birthday falls on a weekend, move it to the next Monday
            if birthday_this_year.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.07.07"},
    {"name": "Jane Smith", "birthday": "1990.07.25"},
    {"name": "Jane Smile", "birthday": "1990.07.20"},
    {"name": "Alice Johnson", "birthday": "1985.07.09"},
    {"name": "Bob Brown", "birthday": "1985.01.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("This week's list of greetings:")
for birthday in upcoming_birthdays:
    print(birthday)