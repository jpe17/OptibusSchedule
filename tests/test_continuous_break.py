import unittest
from data import duties, continuous_break, vehicles, duty_type_rules
from schedule import Schedule


class TestContinuousBreak(unittest.TestCase):
    def test_continuous_break(self):
        schedule_full = Schedule(duties, vehicles, continuous_break, duty_type_rules)

        result = schedule_full.assess_breaks_validity()
        expected_results = [True, True, False, True, False]

        print("\nTest: Duty Continuous Breaks")
        self.assertEqual(expected_results, result)

    if __name__ == '__main__':
        unittest.main()

