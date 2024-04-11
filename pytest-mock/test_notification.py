# file: test_notification.py

from notification import notify_user


# Example 1: Mocking Function

def test_notify_user(mocker):
    mock_send_email = mocker.patch('notification.send_email')
    user = type('User', (), {'email': 'user@example.com'})
    notify_user(user)
    mock_send_email.assert_called_once_with('user@example.com', "Your notification message.")
