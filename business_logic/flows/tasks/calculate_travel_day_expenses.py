class CalculateTravelDayExpenses:
    def run(
            self, 
            taxable_allowance: float, 
            taxfree_allowance: float, 
            kilometer_allowance: float, 
            incidental_costs: float
    ) -> float:
        return (taxable_allowance+taxfree_allowance+kilometer_allowance+incidental_costs)
