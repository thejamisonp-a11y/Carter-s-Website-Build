import reflex as rx


def social_icon(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5"),
        href=href,
        class_name="text-gray-400 hover:text-emerald-600",
    )


def team_member_card(image: str, name: str, role: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=image,
                alt=name,
                class_name="w-40 h-40 mx-auto rounded-full object-cover shadow-lg border-4 border-white",
            ),
            class_name="relative inline-block",
        ),
        rx.el.h3(name, class_name="text-xl font-bold text-gray-800 mt-6"),
        rx.el.p(role, class_name="text-emerald-600 font-medium mb-3"),
        rx.el.div(
            social_icon("twitter", "#"),
            social_icon("linkedin", "#"),
            class_name="flex justify-center space-x-3 mt-2",
        ),
        class_name="text-center",
    )


def team() -> rx.Component:
    team_members = [
        {
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=Eleanor",
            "name": "Eleanor Carter",
            "role": "Founder & CEO",
        },
        {
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=David",
            "name": "David Chen",
            "role": "Head of Care Operations",
        },
        {
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=Maria",
            "name": "Maria Rodriguez",
            "role": "Client Relations Manager",
        },
        {
            "image": "https://api.dicebear.com/9.x/notionists/svg?seed=James",
            "name": "James Wilson",
            "role": "Lead Care Coordinator",
        },
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "OUR EXPERTS",
                    class_name="text-emerald-600 font-semibold text-center",
                ),
                rx.el.h2(
                    "Meet Our Compassionate Team",
                    class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 text-center",
                ),
                rx.el.p(
                    "Our dedicated and experienced professionals are the heart of Carters Care Group, committed to providing exceptional support.",
                    class_name="text-gray-600 mt-4 max-w-2xl mx-auto text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.foreach(
                    team_members,
                    lambda member: team_member_card(
                        member["image"], member["name"], member["role"]
                    ),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="team",
        class_name="bg-gray-50",
    )