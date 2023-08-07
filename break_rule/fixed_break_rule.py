from break_rule import BreakRule
from utils import is_positive_integer
from event_container import Duty


class FixedBreakRule(BreakRule):
    """
    A class to represents a Fixed Break Rule.

    Attributes:
        - break_time_range: The time range for which the break is valid.
        - break_stops: The stops in which the break can occur.
        - min_break_count: Maximum time without a break.
    """
    def __init__(self, break_time_range: str, min_break_count: int, *args, **kwargs):
        super().__init__(break_time_range, *args, **kwargs)
        self.min_breaks = min_break_count

    @property
    def rule_type(self):
        """Getting the rule type"""
        return "Fixed"

    @property
    def min_breaks(self):
        """Getting the minimum number of breaks"""
        return self._min_breaks

    @min_breaks.setter
    def min_breaks(self, value):
        """Setting the minimum number of breaks"""
        is_positive_integer(value)
        self._min_breaks = value

    def is_valid(self, duty: Duty) -> bool:
        """Verifying if certain duty meets the fixed break rule criteria"""
        break_stops = self.break_stops or duty.get_all_stops()
        return duty.has_min_fixed_breaks(self.break_time_range_low, self.break_time_range_high, break_stops, self.min_breaks)

    def __str__(self):
        return f"Fixed Break Rule with Min Breaks: {self.min_breaks}"
