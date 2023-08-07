from utils import validate_non_empty, time_str_to_timedelta, validate_time_str
from break_rule import BreakRule
from event_container import Duty


class ContinuousBreakRule(BreakRule):
    """
    A class to represents a Continuous Break Rule.

    Attributes:
        - break_time_range: The time range for which the break is valid.
        - break_stops: The stops in which the break can occur.
        - max_time: Maximum time without a break.
    """
    def __init__(self, break_time_range: str, max_time_without_break: str, break_stops: str = None):
        super().__init__(break_time_range, break_stops)
        self.max_time = max_time_without_break

    @property
    def rule_type(self):
        """Getting the rule type"""
        return "Continuous"

    @property
    def max_time(self):
        """Getting the maximum time without a break"""
        return self._max_time

    @max_time.setter
    def max_time(self, value):
        """Setting the maximum time without a break"""
        validate_non_empty(value, "Maximum time without break should not be empty.")
        validate_time_str(value)
        self._max_time = time_str_to_timedelta(value)

    def is_valid(self, duty: Duty) -> bool:
        """Verifying if certain duty meets the continuous break rule criteria"""
        break_stops = self.break_stops or duty.get_all_stops()
        return not (duty.needs_continuous_break(self.max_time) and
                    not duty.has_continuous_break_within_max_time(
                        self.break_time_range_low, self.break_time_range_high, break_stops, self.max_time))

    def __str__(self):
        return f"Continuous Break Rule with Max Time: {self.max_time}"
