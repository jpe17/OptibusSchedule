from duty_type import DutyType

duty_type_rules = [DutyType("Morning", start_time_range="08:00-10:00"),
                   DutyType("Afternoon", start_time_range="12:00-15:00",
                            driving_time_range="04:00-12:00"),
                   DutyType("Evening", start_time_range="16:00-22:00"),
                   DutyType("Short", driving_time_range="01:00-03:00", spread_time_range="01:00-04:00")]
