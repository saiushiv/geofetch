import pytest
from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig

@pytest.fixture
def api_handler():
    """Fixture to create an APIHandler instance with real API config."""
    return GeoAPIHandler(GeoAPIConfig())

def test_zip_endpoint_integration(api_handler):
    """Test real integration with the 'zip' endpoint."""
    response = api_handler.get_data("zip", "10001")
    assert response["name"] == "New York"
    assert response["lat"] == 40.7484
    assert response["lon"] == -73.9967

def test_direct_endpoint_integration(api_handler):
    """Test real integration with the 'direct' endpoint."""
    response = api_handler.get_data("direct", "Madison")
    assert response["name"] == "Madison"
    assert response["lat"] == 43.074761
    assert response["lon"] == -89.3837613