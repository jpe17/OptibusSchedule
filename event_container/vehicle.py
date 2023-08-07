from typing import List
from event import Event
from event_container import EventContainer
from utils import validate_non_empty
from datetime import timedelta


class Vehicle(EventContainer):
    """
    Represents a Vehicle consisting of multiple events.

    Attributes:
        - events (List[Event]): Events within the vehicle.
        - vehicle_type (str): Type of the vehicle.
    """
    def __init__(self, events: List[Event], vehicle_type: str = "standard"):

        # Inheriting from parent class
        super().__init__(events)  # Inheriting from parent class
        self.vehicle_type = vehicle_type  # Defining vehicle type

    @property
    def vehicle_type(self) -> str:
        """Returns the type of the vehicle."""
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value: str):
        """Sets the type of the vehicle."""
        validate_non_empty(value, "Vehicle type is empty. Please provide a vehicle type.")
        self._vehicle_type = value

    @property
    def spread_time(self) -> timedelta:
        """Calculates the spread time of the duty."""
        return self.end_time - self.start_time

    def __str__(self):
        return f"Vehicle of type {self.vehicle_type} with {len(self.events)} events from {self.start_time} to {self.end_time}"
