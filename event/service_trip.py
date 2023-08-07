from event import Event
from utils import validate_non_empty


class ServiceTrip(Event):
    """
    Represents a Service Trip Event consisting of a purpose, start and end, as well as an origin and destination.

    Attributes:
        - route: Event specified route.
        - start_time: Event start time.
        - end_time: Event start time.
        - origin: Event start location.
        - destination: Event end location.
    """

    def __init__(self, route: str, start_time: str, end_time: str, origin: str, destination: str):
        # Inheriting from parent class
        super().__init__(start_time, end_time, origin, destination)

        # Define route
        self.route = route

    @property
    def route(self):
        """Gets the route of the service trip event."""
        return self._route

    @route.setter
    def route(self, value):
        """Sets the route of the service trip event."""
        validate_non_empty(value, "Provided route is empty. Please provide a route.")
        self._route = value

    def __str__(self):
        return f'ServiceTrip on route {self.route} from {self.origin} to {self.destination} starting at {self.start_time} and ending at {self.end_time}'
