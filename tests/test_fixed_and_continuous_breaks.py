import unittest
from data import duties, breaks_rules, vehicles, duty_type_rules
from schedule import Schedule


class TestFixedAndContinuousBreaks(unittest.TestCase):
    def test_fixed_and_continuous_breaks(self):
        schedule_full = Schedule(duties, vehicles, breaks_rules, duty_type_rules)

        result = schedule_full.assess_breaks_validity()
        expected_results = [True, True, False, False, False]

        print("\nTest: Duty Fixed and Continuous Breaks")
        self.assertEqual(expected_results, result)

    if __name__ == '__main__':
        unittest.main()



