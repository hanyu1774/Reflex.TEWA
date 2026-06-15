import reflex
from travel_expense_web_app.components.pages.form_services import FormState, TravelDayRow
from travel_expense_web_app.components.ui_library import input_fields, buttons


def _table_header_row() -> reflex.Component:
    return reflex.el.tr(
        reflex.el.th(""),
        reflex.el.th("Datum", class_name="date-cell"),
        reflex.el.th("Beginn", class_name="time-cell"),
        reflex.el.th("Ende", class_name="time-cell"),
        reflex.el.th("Reisegrund", class_name="travel-reason-cell"),
        reflex.el.th("Startort", class_name="location-cell"),
        reflex.el.th("Zielort", class_name="location-cell"),
        reflex.el.th(""),
        reflex.el.th("Kilometer", class_name="kilometers-cell"),
        reflex.el.th("Mahlzeiten", class_name="meals-cell"),
        reflex.el.th("Nebenkosten", class_name="incidental-costs-cell"),
        reflex.el.th("Selbe Aktivitäten"),
    )


def travel_day_row(row: TravelDayRow) -> reflex.Component:
    return reflex.el.tr(
        reflex.el.td(
            reflex.cond(
                row.row_id != 1,
                buttons.delete_row_button(
                    on_click=lambda: FormState.remove_travel_day_row(row.row_id)
                ),
                reflex.fragment(),
            ),
            class_name="delete-button-cell ps-0 text-center padding-0_5rem",
        ),
        reflex.el.td(
            input_fields.date_input(
                value=row.date_value,
                on_change=lambda v: FormState.set_row_date(row.row_id, v),
                min_date=FormState.min_date_for_selected_month,
                max_date=FormState.max_date_for_selected_month,
            ),
            class_name="padding-0_5rem",
        ),
        reflex.el.td(
            input_fields.time_input(
                value=row.start_time,
                on_change=lambda v: FormState.set_row_start_time(row.row_id, v),
            ),
            class_name="padding-0_5rem time-cell",
        ),
        reflex.el.td(
            input_fields.time_input(
                value=row.end_time,
                on_change=lambda v: FormState.set_row_end_time(row.row_id, v),
            ),
            class_name="padding-0_5rem time-cell",
        ),
        reflex.el.td(
            input_fields.travel_reason_input(
                value=row.travel_reason,
                on_change=lambda v: FormState.set_row_travel_reason(row.row_id, v),
            ),
            class_name="padding-0_5rem travel-reason-cell",
        ),
        reflex.el.td(
            input_fields.location_input(
                value=row.starting_location,
                on_change=lambda v: FormState.set_row_starting_location(row.row_id, v),
            ),
            class_name="padding-0_5rem location-cell",
        ),
        reflex.el.td(
            input_fields.location_input(
                value=row.goal_location,
                on_change=lambda v: FormState.set_row_goal_location(row.row_id, v),
            ),
            class_name="padding-0_5rem location-cell",
        ),
        reflex.el.td(
            input_fields.used_private_vehicle_checkbox(
                checked=row.used_private_vehicle,
                on_change=lambda v: FormState.set_row_used_private_vehicle(row.row_id, v),
            ),
            class_name="padding-0_5rem",
        ),
        reflex.el.td(
            input_fields.distance_input(
                value=row.distance_in_kilometers,
                on_change=lambda v: FormState.set_row_distance(row.row_id, v),
                disabled=~row.used_private_vehicle,
            ),
            class_name="padding-0_5rem kilometer-cell",
        ),
        reflex.el.td(
            reflex.flex(
                input_fields.breakfast_checkbox(
                    checked=row.received_breakfast,
                    on_change=lambda v: FormState.set_row_received_breakfast(row.row_id, v),
                ),
                input_fields.lunch_checkbox(
                    checked=row.received_lunch,
                    on_change=lambda v: FormState.set_row_received_lunch(row.row_id, v),
                ),
                input_fields.dinner_checkbox(
                    checked=row.received_dinner,
                    on_change=lambda v: FormState.set_row_received_dinner(row.row_id, v),
                ),
                class_name="meals-content p-1",
                direction="row",
                gap="3",
                wrap="wrap",
            ),
            class_name="meals-cell padding-0_5rem",
        ),
        reflex.el.td(
            input_fields.incidental_expenses_input(
                value=row.incidental_expenses,
                on_change=lambda v: FormState.set_row_incidental_expenses(row.row_id, v),
            ),
            class_name="padding-0_5rem incidental-costs-cell",
        ),
        reflex.el.td(
            input_fields.labeled_checkbox(
                checked=row.same_activity,
                on_change=lambda v: FormState.set_row_same_activity(row.row_id, v),
                label="",
            ),
            class_name="padding-0_5rem",
        ),
        class_name="padding-0_5rem",
    )


def top_fields_row() -> reflex.Component:
    return reflex.flex(
        reflex.flex(
            reflex.el.label("Monat", class_name="form-label"),
            input_fields.month_input(
                value=FormState.selected_month_display,
                on_change=FormState.set_selected_month,
                min_month=FormState.min_month,
                max_month=FormState.max_month,
            ),
            direction="column",
            gap="1",
        ),
        reflex.flex(
            reflex.el.label("Personalnummer", class_name="form-label"),
            input_fields.personnel_id_input(
                value=FormState.personnel_number,
                on_change=FormState.set_personnel_number,
            ),
            direction="column",
            gap="1",
        ),
        reflex.flex(
            input_fields.is_member_of_administration_checkbox(
                checked=FormState.is_member_of_administration,
                on_change=FormState.set_is_member_of_administration,
            ),
            align="end",
        ),
        direction="row",
        gap="4",
        wrap="wrap",
        align="end",
        class_name="mb-3",
    )


def travel_days_table() -> reflex.Component:
    return reflex.box(
        reflex.el.table(
            reflex.el.thead(_table_header_row()),
            reflex.el.tbody(
                reflex.foreach(FormState.travel_day_rows, travel_day_row)
            ),
            class_name="table align-middle mb-3",
        ),
        class_name="table-responsive",
        overflow_x="auto",
    )
