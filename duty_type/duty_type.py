from utils import validate_non_empty, validate_time_str, time_str_to_timedelta, time_range_str_to_time_str, \
    time_str_to_datetime
from event_container import Duty


class DutyType:
    """
    Represents a Duty Type.

    Attributes:
        - name: Name of the Duty Type.
        - start_time_range: Time range in which duties of that type can start.
        - end_time_range:  Time range in which duties of that type can end.
        - driving_time_range: Driving time range which duties of that type must have.
        - spread_time_range: Spread time range which duties of that type must have.
    """

    def __init__(self, name: str, start_time_range: str = None, end_time_range: str = None,
                 driving_time_range: str = None, spread_time_range: str = None):

        self.name = name

        if start_time_range is not None:
            self.start_time_low, self.start_time_high = time_range_str_to_time_str(start_time_range)
        if end_time_range is not None:
            self.end_time_low, self.end_time_high = time_range_str_to_time_str(end_time_range)
        if driving_time_range is not None:
            self.driving_time_low, self.driving_time_high = time_range_str_to_time_str(driving_time_range)
        if spread_time_range is not None:
            self.spread_time_low, self.spread_time_high = time_range_str_to_time_str(spread_time_range)

    @property
    def name(self):
        """Gets the name of the duty type."""
        return self._name

    @name.setter
    def name(self, value):
        """Gets the name of the duty type."""
        validate_non_empty(value, "Duty type name should not be empty.")
        self._name = value

    @property
    def start_time_low(self):
        """Gets the start time low boundary of the duty type."""
        return self._start_time_low

    @start_time_low.setter
    def start_time_low(self, value):
        """Sets the start time low boundary of the duty type."""
        validate_time_str(value)
        self._start_time_low = time_str_to_datetime(value)

    @property
    def start_time_high(self):
        """Gets the start time high boundary of the duty type."""
        return self._start_time_high

    @start_time_high.setter
    def start_time_high(self, value):
        """Sets the start time high boundary of the duty type."""
        validate_time_str(value)
        self._start_time_high = time_str_to_datetime(value)

    @property
    def end_time_low(self):
        """Gets the end time low boundary of the duty type."""
        return self._end_time_low

    @end_time_low.setter
    def end_time_low(self, value):
        """Sets the end time low boundary of the duty type."""
        validate_time_str(value)
        self._end_time_low = time_str_to_datetime(value)

    @property
    def end_time_high(self):
        """Gets the end time high boundary of the duty type."""
        return self._end_time_high

    @end_time_high.setter
    def end_time_high(self, value):
        """Sets the end time high boundary of the duty type."""
        validate_time_str(value)
        self._end_time_high = time_str_to_datetime(value)

    @property
    def driving_time_low(self):
        """Gets the driving time low boundary of the duty type."""
        return self._driving_time_low

    @driving_time_low.setter
    def driving_time_low(self, value):
        """Sets the driving time low boundary of the duty type."""
        validate_time_str(value)
        self._driving_time_low = time_str_to_timedelta(value)

    @property
    def driving_time_high(self):
        """Gets the driving time high boundary of the duty type."""
        return self._driving_time_high

    @driving_time_high.setter
    def driving_time_high(self, value):
        """Sets the driving time high boundary of the duty type."""
        validate_time_str(value)
        self._driving_time_high = time_str_to_timedelta(value)

    @property
    def spread_time_low(self):
        """Gets the spread time low boundary of the duty type."""
        return self._spread_time_low

    @spread_time_low.setter
    def spread_time_low(self, value):
        """Sets the spread time low boundary of the duty type."""
        validate_time_str(value)
        self._spread_time_low = time_str_to_timedelta(value)

    @property
    def spread_time_high(self):
        """Gets the spread time high boundary of the duty type."""
        return self._spread_time_high

    @spread_time_high.setter
    def spread_time_high(self, value):
        """Sets the spread time high boundary of the duty type."""
        validate_time_str(value)
        self._spread_time_high = time_str_to_timedelta(value)

    def matches(self, duty: Duty) -> bool:
        """Checks if a duty falls into the description of this duty type."""
        duty_attributes = ['start_time', 'end_time', 'driving_time', 'spread_time']
        return all(
            (getattr(self, attr + '_low', None) is None or getattr(self, attr + '_low') <= getattr(duty, attr)) and
            (getattr(self, attr + '_high', None) is None or getattr(duty, attr) <= getattr(self, attr + '_high'))
            for attr in duty_attributes
        )
