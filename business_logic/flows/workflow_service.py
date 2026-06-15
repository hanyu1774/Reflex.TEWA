from flows.tasks.apply_deductions import ApplyDeductions
from flows.tasks.calculate_all_expenses import CalculateAllExpenses
from flows.tasks.calculate_travel_day_expenses import CalculateTravelDayExpenses
from flows.tasks.calculate_kilometer_allowance import CalculateKilometerAllowance
from flows.tasks.calculate_spend_hours import CalculateSpendHours
from flows.tasks.determine_taxable_allowance import DetermineTaxableAllowance
from flows.tasks.determine_taxfree_allowance import DetermineTaxfreeAllowance

class WorkflowService:
    ApplyDeductions = ApplyDeductions().run
    CalculateAllExpenses = CalculateAllExpenses().run
    CalculateTravelDayExpenses = CalculateTravelDayExpenses().run
    CalculateKilometerAllowance = CalculateKilometerAllowance().run
    CalculateSpendHours = CalculateSpendHours().run
    DetermineTaxableAllowance = DetermineTaxableAllowance().run
    DetermineTaxfreeAllowance = DetermineTaxfreeAllowance().run
