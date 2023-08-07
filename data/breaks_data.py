from break_rule import ContinuousBreakRule, FixedBreakRule

continuous_break = ContinuousBreakRule(break_time_range='00:30-02:00', break_stops=['B', 'D'], max_time_without_break="04:00")
fixed_break = FixedBreakRule(break_time_range='00:30-02:00', min_break_count=1)

breaks_rules = [continuous_break, fixed_break]