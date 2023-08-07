from typing import List
from event import Event


class EventContainer:
    """
    Represents an Event Container consisting of multiple events.

    Attributes:
        - events (List[Event]): Events within the container.
    """
    def __init__(self, events: List[Event]):
        self.events = events

    @property
    def events(self):
        """Gets the events."""
        return self._events

    @events.setter
    def events(self, value):
        self.validate_events_continuity(self.sort_events(value))
        self._events = self.sort_events(value)

    @staticmethod
    def sort_events(events: List[Event]) -> List[Event]:
        """Sorting events based on start_time to ensure events are in the correct order."""
        return sorted(events, key=lambda x: x.start_time)

    @staticmethod
    def validate_events_continuity(events: List[Event]) -> None:
        """Checks that the end of one event is not later than the start of the next event
        and the destination of the current event is the same as the origin of the next event."""

        for current_event, next_event in zip(events, events[1:]):
            if current_event.end_time < current_event.start_time:
                raise ValueError(f"End time of event {current_event} is before its start time!")

            if current_event.end_time > next_event.start_time:
                raise ValueError(f"Event {current_event} and {current_event} are overlapping!")

            if current_event.destination != next_event.origin:
                raise ValueError(f"Destination of event {current_event} doesn't match the origin of event {next_event}!")

    @property
    def start_time(self):
        """Gets the start time of the event container."""
        return self._events[0].start_time if self._events else None

    @property
    def end_time(self):
        """Gets the end time of the event container."""
        return self._events[-1].end_time if self._events else None

    @property
    def origin(self):
        """Gets the origin of the event container."""
        return self._events[0].origin if self._events else None

    @property
    def destination(self):
        """Gets the destination of the event container."""
        return self._events[-1].destination if self._events else None

    def __str__(self):
        return f"EventContainer with {len(self.events)} events from {self.start_time} to {self.end_time}"
