from dataclasses import field
from business_logic.models.form_entities import file_attachment
from models.form_entities.company import Company
from models.form_entities.employee import Employee
from models.form_entities.file_attachment import FileAttachment
from models.form_entities.time_event import TimeEvent
from models.form_entities.travel_day import TravelDay

class TravelExpenseData:
    employee: Employee = Employee()
    company: Company = Company()
    time_event: TimeEvent = TimeEvent()
    file_attachments: list[FileAttachment] = []
    travel_activities: list[TravelDay] = []
    travel_expenses_per_day: list[float] = []
    all_expenses: float = 0.0
