import reflex as rx
from app.states.state import State


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-600 hover:text-emerald-600 font-medium transition-colors",
    )


def mobile_nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="block py-2 px-4 text-sm text-gray-700 hover:bg-emerald-50",
        on_click=State.toggle_menu,
    )


def header() -> rx.Component:
    nav_items = [
        {"name": "Home", "href": "#"},
        {"name": "About", "href": "#about"},
        {"name": "Services", "href": "#services"},
        {"name": "Our Team", "href": "#team"},
        {"name": "Blog", "href": "#blog"},
        {"name": "Contact", "href": "#contact"},
    ]
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("phone", class_name="h-4 w-4 text-gray-500"),
                        rx.el.span(
                            "(215) 456 - 1189", class_name="text-sm text-gray-600"
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.div(
                        rx.icon("mail", class_name="h-4 w-4 text-gray-500"),
                        rx.el.span(
                            "contact@carterscaregroup.com.au",
                            class_name="text-sm text-gray-600",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="flex items-center gap-6",
                ),
                class_name="flex justify-between items-center w-full",
            ),
            class_name="bg-gray-100 border-b border-gray-200 hidden md:block",
            style={"padding": "0.5rem 1rem"},
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon("heart-pulse", class_name="h-8 w-8 text-emerald-600"),
                        rx.el.span(
                            "Carters Care Group",
                            class_name="text-2xl font-bold text-gray-800",
                        ),
                        href="#",
                        class_name="flex items-center gap-2",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.nav(
                    rx.foreach(
                        nav_items, lambda item: nav_link(item["name"], item["href"])
                    ),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(tag="menu", class_name="h-6 w-6"),
                        on_click=State.toggle_menu,
                        class_name="md:hidden",
                    )
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-20",
            )
        ),
        rx.cond(
            State.is_menu_open,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "heart-pulse", class_name="h-8 w-8 text-emerald-600"
                            ),
                            rx.el.span(
                                "Carters Care Group",
                                class_name="text-2xl font-bold text-gray-800",
                            ),
                            href="#",
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.button(
                            rx.icon(tag="x", class_name="h-6 w-6"),
                            on_click=State.toggle_menu,
                        ),
                        class_name="flex justify-between items-center p-4 border-b",
                    ),
                    rx.el.nav(
                        rx.foreach(
                            nav_items,
                            lambda item: mobile_nav_link(item["name"], item["href"]),
                        ),
                        class_name="py-2",
                    ),
                ),
                class_name="md:hidden fixed inset-0 z-50 bg-white",
            ),
        ),
        class_name="bg-white/80 backdrop-blur-md sticky top-0 z-40 border-b border-gray-200",
    )