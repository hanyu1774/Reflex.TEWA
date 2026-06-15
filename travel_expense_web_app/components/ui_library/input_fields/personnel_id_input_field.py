from typing import Callable
import reflex
from travel_expense_web_app.components.ui_library.input_fields.base_input_field import text_field


def personnel_id_input_field(
    value: str,
    on_change: Callable,
) -> reflex.Component:
    return text_field(
        value=value,
        on_change=on_change,
        placeholder="Personalnummer",
    )
