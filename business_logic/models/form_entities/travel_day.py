from dataclasses import field
from datetime import datetime, time
from models.expense_entitlements.travel_allowance import TravelAllowance
from models.expense_entitlements.travel_day_expenses import TravelDayExpenses

class TravelDay:
    date: datetime = field(default_factory=lambda: datetime.min)
    beginning_of_travel_Time: time = field(default_factory=lambda: time(0, 0))
    end_of_travel_time: time = field(default_factory=lambda: time(0, 0))
    duration_of_travel_time: float = 0.0
    travel_reason: str = ""
    used_private_vehicle: bool = False
    starting_location: str = ""
    goal_location: str = ""
    distance_in_kilometers: float = 0.0
    kilometer_allowance: float = 0.0
    travel_allowance= TravelAllowance()
    travel_day_expenses = TravelDayExpenses()
    expenses_of_travel_day: float = 0.0
