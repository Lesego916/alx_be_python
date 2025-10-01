# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display and return the current date and time in formatted string."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return formatted_date

def calculate_future_date(days: int):
    """Calculate and return a future date after adding given days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return formatted_future

if __name__ == "__main__":
    display_current_datetime()
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(num_days)
    except ValueError:
        print("Invalid input. Please enter an integer.")
