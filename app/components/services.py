import reflex as rx


def service_card(icon: str, image: str, title: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=image, alt=title, class_name="w-full h-48 object-cover rounded-t-lg"
        ),
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-emerald-600 mb-4"),
            rx.el.h3(title, class_name="text-xl font-bold text-gray-900 mb-2"),
            rx.el.p(text, class_name="text-gray-600 text-sm mb-4"),
            rx.el.a(
                "Learn more",
                href="#",
                class_name="font-semibold text-emerald-600 hover:text-emerald-700",
            ),
            class_name="p-6",
        ),
        class_name="bg-white rounded-lg shadow-md overflow-hidden transform hover:-translate-y-2 transition-transform duration-300",
    )


def services() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "WHAT WE OFFER",
                    class_name="text-emerald-600 font-semibold text-center",
                ),
                rx.el.h2(
                    "Our Comprehensive Care Services",
                    class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 text-center",
                ),
                rx.el.p(
                    "We provide a wide range of services to meet the unique needs of each senior, ensuring they receive the best possible care.",
                    class_name="text-gray-600 mt-4 max-w-2xl mx-auto text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                service_card(
                    "heart",
                    "/professional_care_healthcare.png",
                    "Personal Care",
                    "Assistance with daily activities including bathing, dressing, grooming, and mobility support.",
                ),
                service_card(
                    "stethoscope",
                    "/medical_professional_healthcare.png",
                    "Medical Support",
                    "Professional nursing care, medication management, and health monitoring by certified staff.",
                ),
                service_card(
                    "users",
                    "/heartwarming_elderly_person.png",
                    "Companion Care",
                    "Social interaction, conversation, activities, and emotional support to combat loneliness.",
                ),
                service_card(
                    "brain-circuit",
                    "/professional_care_healthcare.png",
                    "Specialized Care",
                    "Expert memory care, dementia support, and assistance for clients with specific medical needs.",
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="services",
        class_name="bg-white",
    )