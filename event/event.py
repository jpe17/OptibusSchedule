from utils import validate_non_empty, validate_time_str, time_str_to_datetime


class Event:
    """
    Represents an Event consisting of a start and end, as well as an origin and destination.

    Attributes:
        - start_time: Event start time.
        - end_time: Event start time.
        - origin: Event start location.
        - destination: Event end location.
    """

    def __init__(self, start_time: str, end_time: str, origin: str, destination: str):
        self.start_time = start_time
        self.end_time = end_time
        self.origin = origin
        self.destination = destination
        self.validate_start_end_time()

    @property
    def start_time(self):
        """Gets the start time of the event."""
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """Sets the start time of the event."""
        validate_time_str(value)
        self._start_time = time_str_to_datetime(value)

    @property
    def end_time(self):
        """Gets the end time of the event."""
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        """Sets the end time of the event."""
        validate_time_str(value)
        self._end_time = time_str_to_datetime(value)

    @property
    def origin(self):
        """Gets the start location of the event."""
        return self._origin

    @origin.setter
    def origin(self, value):
        """Sets the start location of the event."""
        validate_non_empty(value, "Origin should not be empty")
        self._origin = value

    @property
    def destination(self):
        """Gets the end location of the event."""
        return self._destination

    @destination.setter
    def destination(self, value):
        """Gets the end location of the event."""
        validate_non_empty(value, "Destination should not be empty")
        self._destination = value

    def validate_start_end_time(self):
        """Ensure start and end time are consistent."""
        if self.start_time > self.end_time:
            raise ValueError("Invalid time range. End time should not be before start time")

    def __str__(self):
        return f'Event from {self.origin} to {self.destination} starting at {self.start_time} and ending at {self.end_time}'
