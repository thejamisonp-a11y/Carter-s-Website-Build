import reflex as rx


def info_card(icon: str, title: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-8 w-8 text-emerald-600 mb-2"),
        rx.el.h3(title, class_name="font-semibold text-lg text-gray-800"),
        rx.el.p(text, class_name="text-sm text-gray-600"),
        class_name="bg-white p-6 rounded-lg shadow-sm text-center",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "SENIOR CARE SERVICES",
                            class_name="text-emerald-600 font-semibold mb-2",
                        ),
                        rx.el.h1(
                            "Compassionate care for your loved ones",
                            class_name="text-4xl md:text-5xl lg:text-6xl font-extrabold text-gray-900 leading-tight mb-6",
                        ),
                        rx.el.p(
                            "At Carters Care Group, we provide personalized and professional elder care services, ensuring your family members receive the respect, dignity, and high-quality support they deserve in the comfort of their own home.",
                            class_name="text-lg text-gray-600 mb-8",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Get a Quote",
                                href="#contact",
                                class_name="bg-emerald-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-emerald-700 transition-colors flex items-center justify-center shadow-md",
                            ),
                            rx.el.a(
                                rx.icon(
                                    "circle_play", class_name="h-6 w-6 text-emerald-600"
                                ),
                                "Watch our video",
                                href="#",
                                class_name="bg-transparent border-2 border-gray-300 text-gray-700 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 hover:border-gray-400 transition-colors flex items-center justify-center gap-3",
                            ),
                            class_name="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start",
                        ),
                        class_name="text-center lg:text-left",
                    ),
                    rx.el.div(
                        rx.image(
                            src="/professional_smiling_elderly.png",
                            alt="Caregiver and senior woman smiling",
                            class_name="relative w-full h-full object-cover rounded-lg shadow-2xl",
                        ),
                        class_name="relative h-96 lg:h-[450px] mt-12 lg:mt-0",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24",
            ),
            rx.el.div(
                rx.el.div(
                    info_card(
                        "clock",
                        "24/7 Support",
                        "Round-the-clock assistance for any need.",
                    ),
                    info_card(
                        "users",
                        "Expert Team",
                        "Certified and compassionate caregivers.",
                    ),
                    info_card(
                        "award",
                        "10+ Years",
                        "A decade of trusted experience in senior care.",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 pb-16 md:pb-24 -mt-16 relative z-10",
            ),
            class_name="bg-gray-50",
        ),
        id="home",
    )