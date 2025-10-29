import reflex as rx


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text, href=href, class_name="hover:text-emerald-400 transition-colors"
    )


def social_icon(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-6 h-6"),
        href=href,
        class_name="text-gray-400 hover:text-white",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon("heart-pulse", class_name="h-8 w-8 text-emerald-500"),
                        rx.el.span(
                            "Carters Care Group", class_name="text-xl font-bold"
                        ),
                        href="#",
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "Providing high-quality and compassionate care for your loved ones. We are dedicated to improving the lives of seniors in our community.",
                        class_name="text-sm text-gray-400",
                    ),
                    rx.el.div(
                        social_icon("facebook", "#"),
                        social_icon("twitter", "#"),
                        social_icon("instagram", "#"),
                        social_icon("linkedin", "#"),
                        class_name="flex space-x-4 mt-4",
                    ),
                    class_name="flex-1 min-w-[200px]",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Quick Links",
                            class_name="text-lg font-semibold text-white mb-4",
                        ),
                        rx.el.ul(
                            footer_link("Home", "#"),
                            footer_link("About Us", "#about"),
                            footer_link("Services", "#services"),
                            footer_link("Our Team", "#team"),
                            footer_link("Blog", "#blog"),
                            footer_link("Contact Us", "#contact"),
                            class_name="space-y-2 text-sm",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Our Services",
                            class_name="text-lg font-semibold text-white mb-4",
                        ),
                        rx.el.ul(
                            footer_link("Personal Care", "#services"),
                            footer_link("Medical Support", "#services"),
                            footer_link("Companion Care", "#services"),
                            footer_link("Specialized Care", "#services"),
                            class_name="space-y-2 text-sm",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Contact Info",
                            class_name="text-lg font-semibold text-white mb-4",
                        ),
                        rx.el.div(
                            rx.el.p("123 Main Street, Anytown, AU"),
                            rx.el.p("contact@carterscaregroup.com.au"),
                            rx.el.p("(215) 456 - 1189"),
                            class_name="space-y-2 text-sm text-gray-400",
                        ),
                    ),
                    class_name="flex-grow grid grid-cols-2 md:grid-cols-3 gap-8",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-16",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    f"© {2024} Carters Care Group. All rights reserved.",
                    class_name="text-sm text-gray-500",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-4 text-center",
            ),
            class_name="border-t border-gray-800",
        ),
        class_name="bg-gray-900 text-gray-300",
    )