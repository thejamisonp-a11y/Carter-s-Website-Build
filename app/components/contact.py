import reflex as rx
from app.states.state import State


def contact_info_item(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-5 w-5 mr-3"),
        rx.el.span(text),
        class_name="flex items-center",
    )


def contact() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "GET IN TOUCH",
                    class_name="text-emerald-600 font-semibold text-center",
                ),
                rx.el.h2(
                    "We're Here to Help",
                    class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 text-center",
                ),
                rx.el.p(
                    "Have questions about our services, pricing, or anything else? Our team is ready to answer all your questions.",
                    class_name="text-gray-600 mt-4 max-w-2xl mx-auto text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Contact Information", class_name="text-2xl font-bold mb-4"
                    ),
                    rx.el.p(
                        "We're here to help and answer any question you might have. We look forward to hearing from you.",
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        contact_info_item("map-pin", "123 Main Street, Anytown, AU"),
                        contact_info_item("mail", "contact@carterscaregroup.com.au"),
                        contact_info_item("phone", "(215) 456 - 1189"),
                        class_name="space-y-4",
                    ),
                    class_name="bg-emerald-600 text-white p-8 rounded-lg shadow-lg",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Send us a message",
                        class_name="text-2xl font-bold text-gray-900 mb-6",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Name",
                                html_for="name",
                                class_name="block text-gray-700 font-medium mb-2",
                            ),
                            rx.el.input(
                                id="name",
                                name="name",
                                placeholder="Your Name",
                                class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email",
                                html_for="email",
                                class_name="block text-gray-700 font-medium mb-2",
                            ),
                            rx.el.input(
                                id="email",
                                name="email",
                                type="email",
                                placeholder="your.email@example.com",
                                class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Phone",
                                html_for="phone",
                                class_name="block text-gray-700 font-medium mb-2",
                            ),
                            rx.el.input(
                                id="phone",
                                name="phone",
                                type="tel",
                                placeholder="(123) 456-7890",
                                class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Subject",
                                html_for="subject",
                                class_name="block text-gray-700 font-medium mb-2",
                            ),
                            rx.el.input(
                                id="subject",
                                name="subject",
                                placeholder="Question about services",
                                class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Message",
                                html_for="message",
                                class_name="block text-gray-700 font-medium mb-2",
                            ),
                            rx.el.textarea(
                                id="message",
                                name="message",
                                placeholder="Your message here...",
                                rows=4,
                                class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                            ),
                        ),
                        rx.el.button(
                            "Send Message",
                            type="submit",
                            class_name="w-full bg-emerald-600 text-white py-3 rounded-lg font-semibold hover:bg-emerald-700 transition-colors shadow-md",
                        ),
                        on_submit=State.submit_contact_form,
                        reset_on_submit=True,
                        class_name="space-y-4",
                    ),
                    class_name="bg-white p-8 rounded-lg shadow-lg",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="contact",
        class_name="bg-white",
    )