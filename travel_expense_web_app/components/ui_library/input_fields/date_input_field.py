from typing import Callable
import reflex
from components.ui_library.input_fields.base_input_field import date_field

def date_input_field(
    value: str,
    on_change: Callable,
    min_date: str,
    max_date: str,
) -> reflex.Component:
    return date_field(
        value=value,
        on_change=on_change,
        min_date=min_date,
        max_date=max_date,
    )
