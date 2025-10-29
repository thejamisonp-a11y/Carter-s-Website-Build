import reflex as rx
from app.states.state import State


def blog_card(
    image: str, category: str, title: str, excerpt: str, date: str
) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=image, alt=title, class_name="w-full h-48 object-cover rounded-t-lg"
        ),
        rx.el.div(
            rx.el.div(
                category,
                class_name="absolute top-4 left-4 bg-emerald-600 text-white text-xs font-bold uppercase px-2 py-1 rounded-md",
            ),
            rx.el.h3(title, class_name="text-xl font-bold text-gray-900 mb-2"),
            rx.el.p(excerpt, class_name="text-gray-600 text-sm mb-4"),
            rx.el.div(
                rx.el.p(date, class_name="text-xs text-gray-500"),
                rx.el.a(
                    "Read more",
                    href="#",
                    class_name="font-semibold text-emerald-600 hover:text-emerald-700",
                ),
                class_name="flex justify-between items-center",
            ),
            class_name="p-6 relative",
        ),
        class_name="bg-white rounded-lg shadow-md overflow-hidden transform hover:-translate-y-2 transition-transform duration-300",
    )


def blog() -> rx.Component:
    blog_posts = [
        {
            "image": "/professional_checklist_blog.png",
            "category": "Care Tips",
            "title": "10 Tips for Choosing the Right Senior Care Provider",
            "excerpt": "Making the decision to seek professional care for a loved one is never easy. Here are essential factors to consider...",
            "date": "March 15, 2024",
        },
        {
            "image": "/professional_blog_header.png",
            "category": "Health & Wellness",
            "title": "Understanding Dementia Care: A Family Guide",
            "excerpt": "Dementia care requires specialized knowledge and patience. Learn about the best practices and approaches...",
            "date": "March 8, 2024",
        },
        {
            "image": "/heartwarming_elderly_person.png",
            "category": "Services",
            "title": "The Benefits of Companion Care for Seniors",
            "excerpt": "Social interaction plays a crucial role in senior wellbeing. Discover how companion care makes a difference...",
            "date": "February 28, 2024",
        },
    ]
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "FROM OUR BLOG",
                    class_name="text-emerald-600 font-semibold text-center",
                ),
                rx.el.h2(
                    "Latest News & Resources",
                    class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 text-center",
                ),
                rx.el.p(
                    "Stay informed with our latest articles, tips, and insights on senior care and well-being.",
                    class_name="text-gray-600 mt-4 max-w-2xl mx-auto text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("search", class_name="h-5 w-5 text-gray-400"),
                    rx.el.input(
                        placeholder="Search articles...",
                        on_change=State.set_blog_search,
                        class_name="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-emerald-500 focus:border-emerald-500",
                    ),
                    class_name="relative w-full max-w-md mx-auto mb-12",
                )
            ),
            rx.el.div(
                rx.foreach(
                    blog_posts,
                    lambda post: blog_card(
                        post["image"],
                        post["category"],
                        post["title"],
                        post["excerpt"],
                        post["date"],
                    ),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="blog",
        class_name="bg-gray-50",
    )