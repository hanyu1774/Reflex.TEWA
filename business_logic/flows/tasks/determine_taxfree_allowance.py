from typing import Final

class DetermineTaxfreeAllowance:
    def run(self, hours: float) -> float:
        FULL_DAY_ALLOWANCE: Final[float] = 28.00
        HALF_DAY_ALLOWANCE: Final[float] = 14.00
        FULL_DAY_MIN_HOURS: Final[float] = 23.0
        HALF_DAY_MIN_HOURS: Final[float] = 8.0

        if hours >= FULL_DAY_MIN_HOURS:
            return FULL_DAY_ALLOWANCE
        if hours >= HALF_DAY_MIN_HOURS:
            return HALF_DAY_ALLOWANCE
        return 0.0
