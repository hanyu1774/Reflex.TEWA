import uuid
from datetime import date, time
from typing import Final
import reflex


class ReceiptEntry(reflex.Base):
    receipt_id: str = ""
    original_name: str = ""
    size_in_bytes: int = 0


class TravelDayRow(reflex.Base):
    row_id: int = 0
    date_value: str = ""
    start_time: str = ""
    end_time: str = ""
    travel_reason: str = ""
    starting_location: str = ""
    goal_location: str = ""
    used_private_vehicle: bool = False
    distance_in_kilometers: float = 0.0
    received_breakfast: bool = False
    received_lunch: bool = False
    received_dinner: bool = False
    incidental_expenses: float = 0.0
    same_activity: bool = False


class FormState(reflex.State):
    travel_day_rows: list[TravelDayRow] = []
    next_row_id: int = 1
    selected_month: str = ""
    personnel_number: str = ""
    is_member_of_administration: bool = False
    receipt_entries: list[ReceiptEntry] = []

    def _current_month_string(self) -> str:
        today = date.today()
        return f"{today.year}-{today.month:02d}"

    def _min_month_string(self) -> str:
        today = date.today()
        three_months_ago = date(today.year, today.month, 1)
        month = three_months_ago.month - 3
        year = three_months_ago.year
        if month <= 0:
            month += 12
            year -= 1
        return f"{year}-{month:02d}"

    @reflex.var
    def min_month(self) -> str:
        return self._min_month_string()

    @reflex.var
    def max_month(self) -> str:
        return self._current_month_string()

    @reflex.var
    def selected_month_display(self) -> str:
        return self.selected_month if self.selected_month else self._current_month_string()

    @reflex.var
    def min_date_for_selected_month(self) -> str:
        month_str = self.selected_month if self.selected_month else self._current_month_string()
        return f"{month_str}-01"

    @reflex.var
    def max_date_for_selected_month(self) -> str:
        import calendar
        month_str = self.selected_month if self.selected_month else self._current_month_string()
        year, month = int(month_str[:4]), int(month_str[5:7])
        last_day = calendar.monthrange(year, month)[1]
        return f"{month_str}-{last_day:02d}"

    def on_load(self):
        today = date.today()
        self.selected_month = f"{today.year}-{today.month:02d}"
        first_day_string = f"{today.year}-{today.month:02d}-01"
        first_row = TravelDayRow(
            row_id=self.next_row_id,
            date_value=first_day_string,
        )
        self.travel_day_rows = [first_row]
        self.next_row_id = 2

    def set_selected_month(self, new_month: str):
        self.selected_month = new_month
        for row in self.travel_day_rows:
            row.date_value = f"{new_month}-01"

    def set_personnel_number(self, value: str):
        self.personnel_number = value

    def set_is_member_of_administration(self, value: bool):
        self.is_member_of_administration = value

    def add_travel_day_row(self):
        import calendar
        month_str = self.selected_month if self.selected_month else self._current_month_string()
        year, month = int(month_str[:4]), int(month_str[5:7])
        days_in_month = calendar.monthrange(year, month)[1]
        if len(self.travel_day_rows) >= days_in_month:
            return
        new_row = TravelDayRow(
            row_id=self.next_row_id,
            date_value=f"{month_str}-01",
        )
        self.travel_day_rows.append(new_row)
        self.next_row_id += 1

    def remove_travel_day_row(self, row_id: int):
        self.travel_day_rows = [r for r in self.travel_day_rows if r.row_id != row_id]

    def set_row_date(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                month_str = self.selected_month if self.selected_month else self._current_month_string()
                if value.startswith(month_str):
                    row.date_value = value
                break

    def set_row_start_time(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.start_time = value
                break

    def set_row_end_time(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.end_time = value
                break

    def set_row_travel_reason(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.travel_reason = value
                break

    def set_row_starting_location(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.starting_location = value
                break

    def set_row_goal_location(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.goal_location = value
                break

    def set_row_used_private_vehicle(self, row_id: int, value: bool):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.used_private_vehicle = value
                if not value:
                    row.distance_in_kilometers = 0.0
                break

    def set_row_distance(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                try:
                    row.distance_in_kilometers = float(value)
                except ValueError:
                    row.distance_in_kilometers = 0.0
                break

    def set_row_received_breakfast(self, row_id: int, value: bool):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.received_breakfast = value
                break

    def set_row_received_lunch(self, row_id: int, value: bool):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.received_lunch = value
                break

    def set_row_received_dinner(self, row_id: int, value: bool):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.received_dinner = value
                break

    def set_row_incidental_expenses(self, row_id: int, value: str):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                try:
                    row.incidental_expenses = float(value)
                except ValueError:
                    row.incidental_expenses = 0.0
                break

    def set_row_same_activity(self, row_id: int, value: bool):
        for row in self.travel_day_rows:
            if row.row_id == row_id:
                row.same_activity = value
                break

    async def handle_file_upload(self, files: list[reflex.UploadFile]):
        ALLOWED_EXTENSIONS: Final[set[str]] = {".jpg", ".jpeg", ".png", ".pdf"}
        for upload_file in files:
            file_name = upload_file.name
            extension = ""
            if "." in file_name:
                extension = f".{file_name.rsplit('.', 1)[-1].lower()}"
            if extension not in ALLOWED_EXTENSIONS:
                continue
            file_bytes = await upload_file.read()
            upload_path = reflex.get_upload_dir() / file_name
            with upload_path.open("wb") as destination:
                destination.write(file_bytes)
            entry = ReceiptEntry(
                receipt_id=str(uuid.uuid4()),
                original_name=file_name,
                size_in_bytes=len(file_bytes),
            )
            self.receipt_entries.append(entry)

    def remove_receipt(self, receipt_id: str):
        self.receipt_entries = [e for e in self.receipt_entries if e.receipt_id != receipt_id]

    def reset_form(self):
        today = date.today()
        self.selected_month = f"{today.year}-{today.month:02d}"
        self.personnel_number = ""
        self.is_member_of_administration = False
        self.receipt_entries = []
        first_row = TravelDayRow(
            row_id=1,
            date_value=f"{today.year}-{today.month:02d}-01",
        )
        self.travel_day_rows = [first_row]
        self.next_row_id = 2
