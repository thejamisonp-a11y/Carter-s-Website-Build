import reflex as rx


def feature_highlight(text: str) -> rx.Component:
    return rx.el.li(
        rx.icon("square_check", class_name="h-6 w-6 text-emerald-600"),
        rx.el.span(text, class_name="text-gray-700"),
        class_name="flex items-center gap-3",
    )


def about_us() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="/professional_smiling_elderly.png",
                        alt="Team discussing plans",
                        class_name="rounded-lg shadow-lg object-cover w-full h-full",
                    ),
                    class_name="flex-1 p-4",
                ),
                rx.el.div(
                    rx.el.p(
                        "ABOUT US", class_name="text-emerald-600 font-semibold mb-2"
                    ),
                    rx.el.h2(
                        "Dedicated to Exceptional Senior Care",
                        class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mb-6",
                    ),
                    rx.el.p(
                        "For over a decade, Carters Care Group has been a trusted name in elder care services. We believe every senior deserves to live with dignity, comfort, and independence in their own home.",
                        class_name="text-gray-600 mb-6 leading-relaxed",
                    ),
                    rx.el.ul(
                        feature_highlight("Certified and experienced caregivers"),
                        feature_highlight(
                            "Personalized care plans tailored to individual needs"
                        ),
                        feature_highlight("24/7 availability and emergency support"),
                        class_name="space-y-4 mb-8",
                    ),
                    rx.el.a(
                        "Contact Us",
                        href="#contact",
                        class_name="bg-emerald-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-emerald-700 transition-colors shadow-md",
                    ),
                    class_name="flex-1 p-4",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-12 items-center",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="about",
        class_name="bg-gray-50",
    )