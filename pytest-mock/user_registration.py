class UserRegistration:
    def __init__(self, email_service):
        self.email_service = email_service

    def register(self, email_address):
        # Register the user and send a welcome email
        self.email_service.send_welcome_email(email_address)
