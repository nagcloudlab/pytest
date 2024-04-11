from weather import get_weather

# Example 3: Mocking External APIs

def test_get_weather(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.json.return_value = {'weather': 'sunny'}
    
    weather = get_weather('London')
    
    assert weather == 'sunny'
    mock_get.assert_called_once_with("https://example.com/weather/London")
