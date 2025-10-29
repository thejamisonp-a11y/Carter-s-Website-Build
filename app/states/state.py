import reflex as rx


class State(rx.State):
    """The main state for the Carters Care Group app."""

    is_menu_open: bool = False
    blog_search: str = ""
    contact_name: str = ""
    contact_email: str = ""
    contact_phone: str = ""
    contact_subject: str = ""
    contact_message: str = ""

    @rx.event
    def toggle_menu(self):
        """Toggle the mobile menu."""
        self.is_menu_open = not self.is_menu_open

    @rx.event
    def submit_contact_form(self, form_data: dict) -> rx.event.EventSpec:
        """Handle contact form submission."""
        self.contact_name = form_data.get("name", "")
        self.contact_email = form_data.get("email", "")
        self.contact_phone = form_data.get("phone", "")
        self.contact_subject = form_data.get("subject", "")
        self.contact_message = form_data.get("message", "")
        if (
            not self.contact_name
            or not self.contact_email
            or (not self.contact_message)
        ):
            return rx.toast.error("Please fill in all required fields.")
        print(f"Contact form submitted: {form_data}")
        self.contact_name = ""
        self.contact_email = ""
        self.contact_phone = ""
        self.contact_subject = ""
        self.contact_message = ""
        return rx.toast.success(
            "Message sent successfully! We will get back to you soon."
        )