import reflex
# put the namespace for the state here!
 
def header() -> reflex.Component:
    return reflex.el.header(
        reflex.flex(
            reflex.text(
                #FormState.EmployeeFullName,
                color="white",
                font_size="0.95rem",
            ),
            justify="end",
            align="center",
            width="100%",
            padding_x="1rem",
            padding_y="0.5rem",
        ),
        position="sticky",
        top="0",
        z_index="100",
        background_color="#0e613a",
        box_shadow="0 2px 4px rgba(0,0,0,0.25)",
        width="100%",
    )
