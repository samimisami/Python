from datetime import datetime, timedelta

def getDates():
    # Get current date
    # today = datetime(2024, 3, 1)
    today = datetime.today()

    # Calculate the first day of the current month
    first_day_of_this_month = today.replace(day=1)

    # Calculate the last and first day of the previous month
    last_day_of_last_month = first_day_of_this_month - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)

    # Store formatted dates in variables
    firstDay = first_day_of_last_month.strftime("%d-%m-%Y")
    lastDay = last_day_of_last_month.strftime("%d-%m-%Y")
    firstDayName = first_day_of_last_month.strftime("%Y-%m-%d")
    """
    print("First day of last month:", today)
    print("First day of last month:", today.strftime("%d-%m-%Y"))
    print("First day of last month:", firstDay)
    print("Last day of last month:", lastDay)
    """
    return firstDay, lastDay, firstDayName