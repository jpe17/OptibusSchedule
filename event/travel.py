from event import Event


class Travel(Event):
    """
    Represents a Deadhead Event consisting of a purpose, start and end, as well as an origin and destination.

    Attributes:
        - travel_type: Event specified travel type.
        - start_time: Event start time.
        - end_time: Event start time.
        - origin: Event start location.
        - destination: Event end location.
    """
    
    VALID_TRAVEL_TYPES = ["walk", "relief_car", "public_transport", "other"]

    def __init__(self, travel_type: str, start_time: str, end_time: str, origin: str, destination: str):        
        # Inheriting from parent class
        super().__init__(start_time, end_time, origin, destination)

        # Define travel
        self.travel_type = travel_type

    @property
    def travel_type(self):
        """Gets the travel type of the travel event."""
        return self._travel_type

    @travel_type.setter
    def travel_type(self, value):
        """Sets the travel type of the travel event."""
        self.validate_travel_type(value)
        self._travel_type = value

    def validate_travel_type(self, travel_type):
        """Ensure that the travel type is valid and in the list of acceptable purposes."""
        if not travel_type:
            raise ValueError("Provided travel type is empty. Please provide a valid travel type.")
        if travel_type not in self.VALID_TRAVEL_TYPES:
            raise ValueError(f"Travel type should be one of {self.VALID_TRAVEL_TYPES}")

    def __str__(self):
        return f'Travel type {self.travel_type} from {self.origin} to {self.destination} starting at {self.start_time} \
        and ending at {self.end_time}'
