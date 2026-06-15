import reflex
from travel_expense_web_app.components.pages.form_services import FormState
from travel_expense_web_app.components.ui_library.form_table import (
    top_fields_row,
    travel_days_table,
)
from travel_expense_web_app.components.ui_library.buttons import (
    add_row_button,
    upload_button,
    reset_form_button,
    create_pdf_button,
)
from travel_expense_web_app.components.ui_library.receipt_list import receipt_list
from travel_expense_web_app.components.layout.main_layout import main_layout


UPLOAD_ID = "receipt_upload"


def _attachments_section() -> reflex.Component:
    return reflex.box(
        reflex.heading("Anlage(n)", size="4", class_name="mt-3"),
        reflex.text(
            "Falls du Nebenkosten getätigt hast, kannst du Belege hochladen. "
            "Beachte: es werden nur Belege in Dateiformaten wie ",
            reflex.el.code(".jpg"),
            ", ",
            reflex.el.code(".jpeg"),
            ", ",
            reflex.el.code(".pdf"),
            " und ",
            reflex.el.code(".png"),
            " akzeptiert. "
            "Berücksichtige die Reihenfolge deiner Uploads. "
            "Deine Uploads werden in deiner Reihenfolge ins PDF hinzugefügt. "
            "Du kannst bei Bedarf hochgeladene Dateien entfernen.",
            class_name="text-muted small",
        ),
        reflex.upload(
            reflex.text("Dateien auswählen oder hier ablegen"),
            id=UPLOAD_ID,
            accept={
                "image/jpeg": [".jpg", ".jpeg"],
                "image/png": [".png"],
                "application/pdf": [".pdf"],
            },
            multiple=True,
            border="1px dashed #aaa",
            padding="1rem",
            border_radius="6px",
            cursor="pointer",
        ),
        upload_button(
            on_click=FormState.handle_file_upload(reflex.upload_files(upload_id=UPLOAD_ID))
        ),
        receipt_list(),
        class_name="mt-4",
    )


def _form_card() -> reflex.Component:
    return reflex.box(
        reflex.box(
            reflex.heading("Reisekostenabrechnung erstellen", size="5", class_name="mb-0"),
            class_name="card-header bg-white border-bottom py-3",
        ),
        reflex.box(
            top_fields_row(),
            reflex.separator(class_name="my-4"),
            travel_days_table(),
            add_row_button(on_click=FormState.add_travel_day_row),
            _attachments_section(),
            reflex.separator(class_name="my-4"),
            reflex.flex(
                reset_form_button(on_click=FormState.reset_form),
                create_pdf_button(on_click=reflex.window_alert("PDF-Export wird vorbereitet.")),
                justify="end",
                gap="2",
                class_name="mt-4",
            ),
            class_name="card-body p-4",
        ),
        class_name="card shadow-sm",
    )


def form_page() -> reflex.Component:
    return main_layout(
        reflex.el.main(
            reflex.box(
                _form_card(),
                class_name="container-1700px w-100 ms-auto me-auto",
            ),
            class_name=(
                "flex-grow-1 d-flex justify-content-center "
                "align-items-start w-100 py-3"
            ),
            style={"background_color": "var(--dark-green-90)"},
        )
    )
