from event import Deadhead, Travel, ServiceTrip
from event_container import Duty

duties = [
    Duty(
        [
            Travel('walk', '08:05', '08:20', 'A', 'B'),
            ServiceTrip('1A', '08:20', '10:00', 'B', 'C'),
            ServiceTrip('1B', '10:05', '12:00', 'C', 'B'),
            ServiceTrip('1C', '12:30', '14:00', 'B', 'A'),
            Deadhead('pull_in', '14:00', '14:00', 'A', 'A'),
        ]
    ),
    Duty(
        [
            Travel('walk', '08:00', '08:05', 'A', 'B'),
            ServiceTrip('1B', '08:10', '10:00', 'B', 'C'),
            ServiceTrip('1C', '10:10', '12:00', 'C', 'D'),
            ServiceTrip('1D', '12:30', '14:00', 'D', 'C'),
            ServiceTrip('1A', '14:10', '16:00', 'C', 'A'),
        ]
    ),
    Duty(
        [
            ServiceTrip('1A', '18:00', '20:00', 'A', 'C'),
            ServiceTrip('1C', '20:30', '22:00', 'C', 'A'),
            ServiceTrip('1A', '24:00', '25:30', 'A', 'C'),
            Travel('relief_car', '25:30', '25:31', 'C', 'A')
        ]
    ),
    Duty(
        [
            ServiceTrip('1A', '12:00', '14:00', 'A', 'C'),
            Travel('walk', '14:00', '14:05', 'C', 'A')
        ]
    ),
    Duty(
        [
            Deadhead('depot_pull_out', '14:00', '14:30', 'A', 'B'),
            ServiceTrip('1B', '14:30', '15:30', 'B', 'C'),
            ServiceTrip('1C', '16:00', '18:00', 'C', 'B'),
            ServiceTrip('1B', '18:00', '22:00', 'B', 'A'),
        ]
    )
]
