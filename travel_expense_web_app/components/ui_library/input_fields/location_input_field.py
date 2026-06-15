from typing import Callable
import reflex
from components.ui_library.input_fields.base_input_field import text_field


def goal_location_input_field(
    value: str,
    on_change: Callable,
) -> reflex.Component:
    return text_field(
        value=value,
        on_change=on_change,
        extra_class="input-locations",
    )
