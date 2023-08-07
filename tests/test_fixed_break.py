import unittest
from data import duties, vehicles, duty_type_rules, fixed_break
from schedule import Schedule


class TestContinuousBreak(unittest.TestCase):
    def test_fixed_break(self):
        schedule_full = Schedule(duties, vehicles, fixed_break, duty_type_rules)

        result = schedule_full.assess_breaks_validity()
        expected_results = [True, True, True, False, True]

        print("\nTest: Duty Fixed Breaks")
        self.assertEqual(expected_results, result)

    if __name__ == '__main__':
        unittest.main()


