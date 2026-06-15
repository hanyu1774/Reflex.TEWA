from typing import Final
 
 
class DetermineTaxableAllowance:
    def run(self, hours: float) -> float:

        ALLOWANCE_SHORT_TRIP: Final[float] = 6.00
        ALLOWANCE_LONG_TRIP: Final[float] = 30.00
        SHORT_TRIP_MIN_HOURS: Final[float] = 6.0
        SHORT_TRIP_MAX_HOURS: Final[float] = 8.0

        if SHORT_TRIP_MIN_HOURS <= hours <= SHORT_TRIP_MAX_HOURS:
            return ALLOWANCE_SHORT_TRIP
        if hours > SHORT_TRIP_MAX_HOURS:
            return ALLOWANCE_LONG_TRIP
        return 0.0
 
