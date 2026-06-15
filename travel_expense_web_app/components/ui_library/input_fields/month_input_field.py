from typing import Callable
import reflex
from components.ui_library.input_fields.base_input_field import month_field

def month_input_field(
    value: str,
    on_change: Callable,
    min_month: str,
    max_month: str,
) -> reflex.Component:
    return month_field(
        value=value,
        on_change=on_change,
        min_month=min_month,
        max_month=max_month,
    )
