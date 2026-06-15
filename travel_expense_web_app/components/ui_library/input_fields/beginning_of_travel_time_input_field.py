from typing import Callable
import reflex
from components.ui_library.input_fields.base_input_field import time_field

def beginning_of_time_input_field(value: str, on_change: Callable) -> reflex.Component:
    return time_field(value=value, on_change=on_change)
