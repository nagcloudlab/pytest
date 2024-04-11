from unittest.mock import PropertyMock
from user_profile import UserProfile

# Example 5: Mocking Properties with PropertyMock

def test_user_profile(mocker):
    mock_is_active = PropertyMock(return_value=False)
    mocker.patch('user_profile.UserProfile.is_active', new_callable=PropertyMock, return_value=False)
    
    user_profile = UserProfile()
    assert not user_profile.is_active
