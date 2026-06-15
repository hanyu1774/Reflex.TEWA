from typing import Final

class CalculateKilometerAllowance:
    def run(self, distance_in_kilometers: float) -> float:
        KILOMETER_RATE: Final[float] = 0.25
        return distance_in_kilometers * KILOMETER_RATE
