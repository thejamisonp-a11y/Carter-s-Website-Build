import reflex as rx
from app.components.header import header
from app.components.hero import hero
from app.components.services import services
from app.components.about import about_us
from app.components.team import team
from app.components.testimonials import testimonials
from app.components.blog import blog
from app.components.contact import contact
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(
            hero(), services(), about_us(), team(), testimonials(), blog(), contact()
        ),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)