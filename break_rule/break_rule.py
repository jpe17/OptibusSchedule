from abc import ABC
from typing import List
from utils import time_range_str_to_time_str, time_str_to_timedelta, validate_time_str, validate_non_empty
from event_container import Duty


class BreakRule(ABC):
    """
    An abstract class to represents a Break Rule.

    Attributes:
        - break_time_range: The time range for which the break is valid.
        - break_stops: The stops in which the break can occur.
    """
    def __init__(self, break_time_range: str, break_stops: List[str] = None):
        validate_non_empty(break_time_range, "Break time range cannot be empty")
        self.break_time_range = break_time_range
        self.break_time_range_low, self.break_time_range_high = time_range_str_to_time_str(break_time_range)
        self.break_stops = break_stops or []

    @property
    def break_time_range_low(self):
        """Gets the break time range low boundary."""
        return self._break_time_range_low

    @break_time_range_low.setter
    def break_time_range_low(self, value):
        """Sets the break time range low boundary."""
        validate_time_str(value)
        self._break_time_range_low = time_str_to_timedelta(value)

    @property
    def break_time_range_high(self):
        """Gets the break time range high boundary."""
        return self._break_time_range_high

    @break_time_range_high.setter
    def break_time_range_high(self, value):
        """Sets the break time range high boundary."""
        validate_time_str(value)
        self._break_time_range_high = time_str_to_timedelta(value)

    def is_valid(self, duty: Duty) -> bool:
        pass
