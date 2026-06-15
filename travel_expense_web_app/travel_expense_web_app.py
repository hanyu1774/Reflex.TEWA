"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex  

from rxconfig import config


class State(reflex.State):
    """The app state."""


def index() -> reflex.Component:
    # Welcome Page (Index)
    return reflex.container(
        reflex.color_mode.button(position="top-right"),
        reflex.vstack(
            reflex.heading("Welcome to Reflex!", size="9"),
            reflex.text(
                "Get started by editing ",
                reflex.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            reflex.link(
                reflex.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = reflex.App()
app.add_page(index)
