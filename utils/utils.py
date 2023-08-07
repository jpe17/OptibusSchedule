from datetime import datetime, timedelta
import re


def is_positive_integer(number):
    """Check if a number is a positive integer."""
    if not (isinstance(number, int) and number > 0):
        raise ValueError(f"{number} is not a positive integer.")
    return True


def validate_non_empty(value, error_message):
    """Ensure that the value is not empty.
    If the value is empty, raises ValueError with the given error message."""
    if not value:
        raise ValueError(error_message)


def validate_time_str(time_str):
    """Ensure that the time strings are valid.
    If the time string is not in 'HH:MM' format or hours/minutes are not in valid range,
    raises ValueError."""
    if not re.match(r'^\d{1,2}:\d{2}$', time_str):
        raise ValueError(f"Invalid format for time. Expected format is 'HH:MM'")

    hours, minutes = map(int, time_str.split(":"))
    if not (0 <= hours < 36) or not (0 <= minutes < 60):
        raise ValueError("Invalid time values. Hours should be between 0 and 35, and minutes between 0 and 59.")


def time_str_to_timedelta(time_str):
    """Convert time string to time delta"""
    hours, minutes = map(int, time_str.split(':'))
    return timedelta(hours=hours, minutes=minutes)


def time_str_to_datetime(time_str):
    """Convert time string in HH:MM format to datetime object using today's date as the base."""
    hours, minutes = map(int, time_str.split(":"))
    days = hours // 24
    hours %= 24

    # Using today's date as the base and adding days and hours to it.
    base_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    return base_date + timedelta(days=days, hours=hours, minutes=minutes)


def time_range_str_to_time_str(time_range_str):
    """Convert time range string to high range and low range time delta"""
    start_time_str, end_time_str = time_range_str.split('-')
    return start_time_str, end_time_str
