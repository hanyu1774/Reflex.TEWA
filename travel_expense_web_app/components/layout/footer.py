import reflex

def footer() -> reflex.Component:
    return reflex.el.footer(
        reflex.flex(
            reflex.text("<your name here>", class_name="small text_muted"),
            #reflex.image(),
            justify="between",
            align="center",
            width="100%",
            padding_x="1rem",
            padding_y="0.5rem",
        ),
        class_name="container-fluid mt-auto border-top bg-light",
        width="100%",
    )
