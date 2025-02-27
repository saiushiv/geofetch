import pytest
from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig
from src.utils.validate_util import validate_input

"""
Integration tests for the GeoFetch package.
These tests validate the integration of various components of the GeoFetch package,
including the API handler and input validation utilities. The tests make real API
calls to ensure that the components work together as expected.
"""

@pytest.fixture
def api_handler():
    """Fixture to create an APIHandler instance with real API config."""
    return GeoAPIHandler(GeoAPIConfig())

@pytest.fixture
def validated_input():
    """Fixture to validate input using the validate_input util function."""
    def _validate(input_str):
        return validate_input(input_str)
    return _validate

def test_zip_endpoint_integration(api_handler, validated_input):
    """Test real integration with the 'zip' endpoint."""
    input_str = validated_input("10001")
    response = api_handler.get_data("zip", input_str)
    assert response["name"] == "New York"
    assert response["lat"] == 40.7484
    assert response["lon"] == -73.9967

def test_direct_endpoint_integration(api_handler, validated_input):
    """Test real integration with the 'direct' endpoint."""
    input_str = validated_input("Madison, WI")
    response = api_handler.get_data("direct", input_str)
    # Response is a list of dictionaries. so the first one is checked
    assert response[0]["name"] == "Madison"
    assert response[0]["lat"] == 43.074761
    assert response[0]["lon"] == -89.3837613

def test_invalid_zip_input(validated_input):
    """Test to validate input with invalid zip code. US zip needs to be of 5 digits"""
    with pytest.raises(ValueError) as e:
       validated_input("100")
    assert "Invalid Location" in str(e.value)

def test_invalid_location_input(validated_input):
    """Test to validate input with invalid location. Location needs to be in 'city,state' format."""
    with pytest.raises(ValueError) as e:
       validated_input("Madison")
    assert "Invalid Location" in str(e.value)

def test_zip_empty_response(api_handler, validated_input):
    """Test real integration with the 'zip' endpoint with invalid zip code."""
    input_str = validated_input("11000")
    response = api_handler.get_data("zip", input_str)
    assert response["error"] == "Request failed with status 404"

def test_direct_empty_response(api_handler, validated_input):
    """Test real integration with the 'direct' endpoint with invalid city name."""
    input_str = validated_input("10000, WI")
    response = api_handler.get_data("direct", input_str)
    assert response["error"] == "Invalid input. Empty response received"

def test_zip_alphanumeric_input(api_handler, validated_input):
    """Test to validate input with invalid alphanumeric zip code."""
    input_str = validated_input("100AB")
    response = api_handler.get_data("zip", input_str)
    assert response["error"] == "Request failed with status 404"

def test_direct_alphanumeric_input(api_handler, validated_input):
    """Test real integration with the 'direct' endpoint with invalid alphanumeric city name."""
    input_str = validated_input("Madison100, WI")
    response = api_handler.get_data("direct", input_str)
    assert response["error"] == "Invalid input. Empty response received"

def test_direct_empty_input1(api_handler, validated_input):
    """Test real integration with the 'direct' endpoint with invalid empty input."""
    input_str = validated_input(""     ",")
    response = api_handler.get_data("direct", input_str)
    assert response["error"] == "Request failed with status 404"

def test_direct_empty_input2(api_handler, validated_input):
    """Test real integration with the 'direct' endpoint with invalid empty input."""
    input_str = validated_input('"     ",')
    response = api_handler.get_data("direct", input_str)
    assert response["error"] == "Invalid input. Empty response received"

