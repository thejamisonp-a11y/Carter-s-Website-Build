import reflex as rx


def testimonial_card(quote: str, image: str, name: str, relation: str) -> rx.Component:
    return rx.el.div(
        rx.icon(
            "quote", class_name="w-10 h-10 text-emerald-600 opacity-20 mx-auto mb-4"
        ),
        rx.el.p(f'"{quote}"', class_name="text-gray-600 italic mb-6"),
        rx.el.div(
            rx.foreach(
                range(5),
                lambda i: rx.icon(
                    "star", class_name="w-5 h-5 text-yellow-400", fill="currentColor"
                ),
            ),
            class_name="flex items-center justify-center mb-4",
        ),
        rx.image(
            src=image,
            alt=name,
            class_name="w-16 h-16 mx-auto rounded-full object-cover mb-2 border-2 border-white shadow-sm",
        ),
        rx.el.h4(name, class_name="font-bold text-gray-800"),
        rx.el.p(relation, class_name="text-sm text-gray-500"),
        class_name="bg-white p-8 rounded-lg shadow-lg text-center transform hover:-translate-y-2 transition-transform duration-300",
    )


def testimonials() -> rx.Component:
    testimonial_data = [
        {
            "quote": "The care my mother received was exceptional. The team was so compassionate and professional. We couldn't have asked for better support during a difficult time.",
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=Sarah",
            "name": "Sarah L.",
            "relation": "Daughter of Client",
        },
        {
            "quote": "Carters Care Group provided wonderful companionship for my father. His caregiver was a perfect match, and it gave our family great peace of mind. Highly recommended!",
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=Michael",
            "name": "Michael B.",
            "relation": "Son of Client",
        },
        {
            "quote": "From the initial consultation to the daily care, every step was handled with professionalism and genuine kindness. Thank you for making my husband's final years comfortable.",
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=Janet",
            "name": "Janet P.",
            "relation": "Wife of Client",
        },
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "WHAT CLIENTS SAY",
                    class_name="text-emerald-600 font-semibold text-center",
                ),
                rx.el.h2(
                    "Real Stories from Real Families",
                    class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 text-center",
                ),
                rx.el.p(
                    "Our clients' experiences speak volumes about our commitment to compassionate and quality care.",
                    class_name="text-gray-600 mt-4 max-w-2xl mx-auto text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.foreach(
                    testimonial_data,
                    lambda item: testimonial_card(
                        item["quote"], item["image"], item["name"], item["relation"]
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        style={
            "backgroundImage": "radial-gradient(#e5e7eb 1px, transparent 1px)",
            "backgroundSize": "20px 20px",
        },
    )