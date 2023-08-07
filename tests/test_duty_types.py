import unittest
from data import duties, vehicles, breaks_rules, duty_type_rules
from schedule import Schedule


class TestDutyTypes(unittest.TestCase):
    def test_duty_types(self):
        schedule = Schedule(duties, vehicles, breaks_rules, duty_type_rules)
        schedule.assign_duty_types()  # Call this function to set the duty types for the duties

        expected_results = ['Morning', 'Morning', 'Evening', 'Short', 'Afternoon']

        print("\nTest: Duty Types from Schedule")

        for i, duty in enumerate(schedule.duties):
            print(duty.duty_type)
            self.assertEqual(duty.duty_type, expected_results[i])


if __name__ == '__main__':
    unittest.main()
