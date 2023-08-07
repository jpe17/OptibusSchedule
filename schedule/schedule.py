from typing import List
from event_container import Vehicle, Duty
from duty_type import DutyType
from break_rule import BreakRule


class Schedule:
    """
    Represents a Schedule with Duties, Vehicles, Break Rules and Duty Type Rules.

    Attributes:
        - events (List[Event]): Events within the container.
    """
    def __init__(self, duties: List[Duty], vehicles: List[Vehicle], break_rules: List[BreakRule],
                 duty_type_rules: List[DutyType]):
        self.duties = duties
        self.vehicles = vehicles
        self.break_rules = break_rules if isinstance(break_rules, list) else [break_rules]
        self.duty_type_rules = duty_type_rules

    def assign_duty_types(self):
        """Iterate over all duties and for each, assign its type based on matching duty_type_rules."""
        for duty in self.duties:
            duty.duty_type = next((duty_type_rule.name for duty_type_rule in self.duty_type_rules if duty_type_rule.matches(duty)), None)

    def assess_breaks_validity(self) -> List[bool]:
        """Iterate over all duties and for each, assess whether they meet both the fixed and continuous breaks."""
        return [all(break_rule.is_valid(duty) for break_rule in self.break_rules) for duty in self.duties]

