import pytest

from fetch_data import fetch_data

@pytest.mark.asyncio
async def test_fetch_data(mocker):
    async_mock = mocker.AsyncMock(return_value="mocked data")
    mocker.patch('fetch_data.fetch_data', new=async_mock)
    
    result = await fetch_data()
    assert result == "mocked data"
