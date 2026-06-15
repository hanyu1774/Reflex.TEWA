from typing import Callable
import reflex

def text_field(
    value: str,
    on_change: Callable,
    placeholder: str = "",
    extra_class: str = "",
    title: str = "",
) -> reflex.Component:
    return reflex.el.input(
        type="text",
        value=value,
        on_change=on_change,
        placeholder=placeholder,
        title=title,
        class_name=f"form-control {extra_class}".strip(),
    )


def number_field(
    value: float,
    on_change: Callable,
    disabled: bool = False,
    title: str = "",
    extra_class: str = "",
) -> reflex.Component:
    return reflex.el.input(
        type="number",
        value=value,
        on_change=on_change,
        step="0.01",
        disabled=disabled,
        title=title,
        class_name=f"form-control width-110px {extra_class}".strip(),
    )


def date_field(
    value: str,
    on_change: Callable,
    min_date: str,
    max_date: str,
) -> reflex.Component:
    return reflex.el.input(
        type="date",
        value=value,
        on_change=on_change,
        min=min_date,
        max=max_date,
        class_name="form-control input-date",
    )


def time_field(
    value: str,
    on_change: Callable,
) -> reflex.Component:
    return reflex.el.input(
        type="time",
        value=value,
        on_change=on_change,
        class_name="form-control input-time",
    )


def month_field(
    value: str,
    on_change: Callable,
    min_month: str,
    max_month: str,
) -> reflex.Component:
    return reflex.el.input(
        type="month",
        id="month_picker",
        value=value,
        on_change=on_change,
        min=min_month,
        max=max_month,
        class_name="form-control",
    )


def checkbox_field(
    checked: bool,
    on_change: Callable,
    label: str,
    title: str = "",
) -> reflex.Component:
    return reflex.flex(
        reflex.el.input(
            type="checkbox",
            checked=checked,
            on_change=on_change,
            title=title,
            class_name="form-check-input",
        ),
        reflex.el.label(label, class_name="form-check-label ms-1"),
        class_name="form-check",
        align="center",
        gap="2",
    )
