import reflex as rx

config = rx.Config(
    app_name="travel_expense_web_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
