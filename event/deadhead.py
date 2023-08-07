from event import Event


class Deadhead(Event):
    """
    Represents a Deadhead Event consisting of a purpose, start and end, as well as an origin and destination.

    Attributes:
        - purpose: Event specified purpose.
        - start_time: Event start time.
        - end_time: Event start time.
        - origin: Event start location.
        - destination: Event end location.
    """

    VALID_PURPOSES = ["pull_in", "pull_out", "depot_pull_in", "depot_pull_out", "idle"]

    def __init__(self, purpose: str, start_time: str, end_time: str, origin: str, destination: str):
        # Inheriting from parent class
        super().__init__(start_time, end_time, origin, destination)

        # Defining purpose
        self.purpose = purpose

    @property
    def purpose(self):
        """Gets the purpose of the deadhead event."""
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        """Sets the purpose of the deadhead event."""
        self.validate_purpose(value)
        self._purpose = value

    def validate_purpose(self, purpose):
        """Ensure that the deadhead purpose is valid and in the list of acceptable purposes."""
        if not purpose:
            raise ValueError("Provided purpose is empty. Please provide a valid purpose.")
        if purpose not in self.VALID_PURPOSES:
            raise ValueError(f"Purpose should be one of {self.VALID_PURPOSES}")

    def __str__(self):
        return f'Deadhead for {self.purpose} from {self.origin} to {self.destination} starting at {self.start_time} and ending at {self.end_time}'
