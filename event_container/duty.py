from datetime import timedelta
from typing import List
from event import Event, ServiceTrip, Deadhead
from event_container import EventContainer


class Duty(EventContainer):
    """
    Represents a Duty consisting of multiple events.

    Attributes:
        - events (List[Event]): Events within the duty.
        - duty_type (str): Type of the duty.
    """

    def __init__(self, events: List[Event], duty_type: str = None):
        # Inheriting from parent class
        super().__init__(events)
        self.duty_type = duty_type

    @property
    def duty_type(self) -> str:
        """Returns the type of the duty."""
        return self._duty_type

    @duty_type.setter
    def duty_type(self, value: str):
        """Sets the type of the duty."""
        self._duty_type = value

    @property
    def driving_time(self) -> timedelta:
        """Calculates the total driving time of the duty."""
        return sum(
            (event.end_time - event.start_time for event in self.events if isinstance(event, (ServiceTrip, Deadhead))),
            timedelta())

    @property
    def spread_time(self) -> timedelta:
        """Calculates the spread time of the duty."""
        return self.end_time - self.start_time

    def get_all_stops(self) -> List[str]:
        """Retrieves all unique stops within the duty."""
        return list({stop for event in self.events for stop in (event.origin, event.destination)})

    # Break-related methods
    def needs_continuous_break(self, max_time: timedelta) -> bool:
        """Checks if a continuous break is needed within the duty."""
        return self.spread_time > max_time

    @staticmethod
    def _is_event_break(current_event, next_event, break_time_range_low: timedelta,
                        break_time_range_high: timedelta,
                        break_stops: List[str]) -> bool:
        """Determines if the gap between two events is a valid break."""
        available_break_time = next_event.start_time - current_event.end_time
        is_break = break_time_range_low <= available_break_time <= break_time_range_high and (
                current_event.destination in break_stops)
        return is_break

    @staticmethod
    def _time_since_last_break(next_event, last_break_end: timedelta) -> timedelta:
        """Computes the time since the last break."""
        return next_event.end_time - last_break_end

    def has_continuous_break_within_max_time(self, break_time_range_low: timedelta,
                                             break_time_range_high: timedelta,
                                             break_stops: List[str],
                                             max_time: timedelta) -> bool:
        """Checks if there's a continuous valid break within a maximum time."""
        # Start last_break_end at starting time of duty
        last_break_end = self.start_time

        # Iterate through events
        for current_event, next_event in zip(self.events, self.events[1:]):
            if self._is_event_break(current_event, next_event, break_time_range_low,
                                    break_time_range_high, break_stops):
                last_break_end = next_event.start_time
            else:
                if self._time_since_last_break(next_event, last_break_end) > max_time:
                    return False
        return True

    def has_min_fixed_breaks(self, break_time_range_low: timedelta, break_time_range_high: timedelta,
                             break_stops: List[str], min_breaks: int) -> bool:
        """Checks if there are a minimum number of valid fixed breaks."""
        valid_break_count = sum(1 for current_event, next_event in zip(self.events, self.events[1:])
                                if self._is_event_break(current_event, next_event, break_time_range_low,
                                                        break_time_range_high, break_stops))
        return valid_break_count >= min_breaks
