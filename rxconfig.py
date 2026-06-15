import reflex  

config = reflex.Config(
    app_name="travel_expense_web_app",
    plugins=[
        reflex.plugins.SitemapPlugin(),
        reflex.plugins.TailwindV4Plugin(),
    ]
)
