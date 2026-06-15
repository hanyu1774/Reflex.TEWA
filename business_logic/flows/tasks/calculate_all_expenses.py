class CalculateAllExpenses:
    def run(self, expense_list: list[float]) -> float:
        result: float = 0.0
        for value in expense_list:
            result += value
        return result
