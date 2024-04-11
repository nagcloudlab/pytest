from user_registration import UserRegistration
from email_service import EmailService

# Example 2: Mocking Class Instances

def test_register_user(mocker):
    mock_email_service = mocker.create_autospec(EmailService)
    user_registration = UserRegistration(mock_email_service)
    email_address = 'test@example.com'
    
    user_registration.register(email_address)
    
    mock_email_service.send_welcome_email.assert_called_once_with(email_address)
