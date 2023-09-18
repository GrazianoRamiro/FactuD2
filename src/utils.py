import datetime


def get_start_and_end_of_month(date=datetime.datetime.now()):
    # Get the first day of the current month
    first_date = datetime.datetime(date.year, date.month, 1)

    # Get the first day of the next month
    if date.month == 12:
        next_month = datetime.datetime(date.year + 1, 1, 1)
    else:
        next_month = datetime.datetime(date.year, date.month + 1, 1)

    # Subtract one day to get the last day of the current month
    last_date = next_month - datetime.timedelta(days=1)

    # Convert to desired format
    first_date_str = first_date.strftime("%d/%m/%Y")
    last_date_str = last_date.strftime("%d/%m/%Y")

    return (first_date_str, last_date_str)
