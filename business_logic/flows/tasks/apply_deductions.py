from typing import Final

class ApplyDeductions:
    def run(
        self, 
        received_breakfast: bool,
        received_lunch: bool,
        received_dinner: bool,
        taxfree_allowance: float,
    ) -> float:
        BREAKFAST_DEDUCTION: Final[float] = 5.60
        LUNCH_DEDUCTION: Final[float] = 11.20
        DINNER_DEDUCTION: Final[float] = 11.20

        if received_breakfast:
            taxfree_allowance -= BREAKFAST_DEDUCTION
        if received_lunch:
            taxfree_allowance -= LUNCH_DEDUCTION
        if received_dinner:
            taxfree_allowance -= DINNER_DEDUCTION
        if taxfree_allowance <= 0:
            taxfree_allowance = 0.0
        return taxfree_allowance
