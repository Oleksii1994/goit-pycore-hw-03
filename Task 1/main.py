from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between the given date and today's date.
    
    Args:
        date (str): The date in 'YYYY-MM-DD' format.
        
    Returns:
        int: The number of days from the given date to today. If the given date 
             is in the future, the result will be negative.
    """
    
    try:
         # convert the date string into a date object
        transformed_date = datetime.strptime(date, "%Y-%m-%d").date()
        # get today's date
        today = datetime.today().date()
        # calculate the difference between today and the entered date
        difference = (today - transformed_date).days
        return difference
    except ValueError:
        # handle the error of incorrect date format
        print(f"Date {date} has invalid format. Try fotmat: YYYY-MM-DD")
            
result = get_days_from_today("2024-05-07")
# if result is valid, print the number of days
if result is not None:
    print(result)

  

    

