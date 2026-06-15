from datetime import datetime, time
from typing import Final
 
class CalculateSpendHours:
    def run(self, end_time: time, start_time: time) -> float:
        FULL_DAY_HOURS: Final[float] = 24.0
        end_as_datetime = datetime(1, 1, 1, end_time.hour, end_time.minute, end_time.second)
        start_as_datetime = datetime(1, 1, 1, start_time.hour, start_time.minute, start_time.second)
        difference_in_seconds = (end_as_datetime - start_as_datetime).total_seconds()
        if difference_in_seconds < 0:
            difference_in_seconds += FULL_DAY_HOURS * 3600
        return difference_in_seconds / 3600
