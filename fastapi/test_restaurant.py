import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from restaurant import recommend_restaurant, TravelMode, CateringType

# Mock a successful response from geoapify geocode API
mock_geocode_response_success = {
    "results": [
        {
            "name": "Test Location",
            "formatted": "Test Address",
            "lat": 12.34,
            "lon": 56.78
        }
    ]
}

# Mock a successful response from geoapify isoline API
mock_isoline_response_success = {
    "features": [
        {
            "properties": {
                "id": "test_geometry_id"
            }
        }
    ]
}

# Mock a successful response from geoapify places API
mock_places_response_success = {
    "features": [
        {
            "properties": {
                "name": "Test Restaurant",
                "formatted": "Test Restaurant Address",
                "lon": 56.789,
                "lat": 12.345
            }
        }
    ]
}

# Mock a successful response from geoapify routing API
mock_routing_response_success = {
    "features": [
        {
            "properties": {},
            "geometry": {}
        }
    ]
}

@pytest.fixture
def mock_requests_get():
    with patch("restaurant.requests.get") as mock_get:
        yield mock_get

def configure_mock_requests_get(mock_requests_get):
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success),  # Geocode
        MagicMock(status_code=200, json=lambda: mock_isoline_response_success),  # Isoline
        MagicMock(status_code=200, json=lambda: mock_places_response_success),   # Places
        MagicMock(status_code=200, json=lambda: mock_routing_response_success)   # Routing
    ]

    # Call the function
    result = recommend_restaurant(
        location="Test Location",
        mode=TravelMode.drive,
        time_range=15,
        categories=[CateringType.restaurant]
    )

    # Assertions
    assert result["features"][0]["start"]["name"] == "Test Location"
    assert result["features"][0]["destination"]["name"] == "Test Restaurant"
    
    # Check that "drive" was used in API calls
    # Isoline API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]
    # Routing API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[3][0][0]


def test_recommend_restaurant_drive_no_restaurant_found(mock_requests_get):
    # Configure mock responses for no restaurant found
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success), # Geocode
        MagicMock(status_code=200, json=lambda: mock_isoline_response_success), # Isoline
        MagicMock(status_code=200, json=lambda: {"features": []})  # Places (no restaurants)
    ]

    # Call the function
    result = recommend_restaurant(
        location="Test Location",
        mode=TravelMode.drive,
        time_range=15,
        categories=[CateringType.restaurant]
    )

    # Assertions
    assert result["start"]["name"] == "Test Location"
    assert result["destination"] == "No restaurant found."

    # Check that "drive" was used in API calls
    # Isoline API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]


def test_recommend_restaurant_drive_geocode_fails(mock_requests_get):
    # Configure mock response for geocode failure
    mock_requests_get.return_value = MagicMock(status_code=500)

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Test Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Failed to retrieve data from geoapify." in str(excinfo.value.detail)


def test_recommend_restaurant_drive_isoline_fails(mock_requests_get):
    # Configure mock responses for isoline failure
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success), # Geocode
        MagicMock(status_code=500)  # Isoline
    ]

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Test Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Failed to retrieve data from geoapify." in str(excinfo.value.detail)

    # Check that "drive" was used in the Isoline API call before it failed
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]


def test_recommend_restaurant_drive_places_fails(mock_requests_get):
    # Configure mock responses for places failure
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success), # Geocode
        MagicMock(status_code=200, json=lambda: mock_isoline_response_success), # Isoline
        MagicMock(status_code=500)  # Places
    ]

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Test Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Failed to retrieve data from geoapify." in str(excinfo.value.detail)

    # Check that "drive" was used in the Isoline API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]


def test_recommend_restaurant_drive_routing_fails(mock_requests_get):
    # Configure mock responses for routing failure
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success),  # Geocode
        MagicMock(status_code=200, json=lambda: mock_isoline_response_success),  # Isoline
        MagicMock(status_code=200, json=lambda: mock_places_response_success),   # Places
        MagicMock(status_code=500)  # Routing
    ]

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Test Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Failed to retrieve data from geoapify." in str(excinfo.value.detail)
    
    # Check that "drive" was used in API calls
    # Isoline API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]
    # Routing API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[3][0][0]

def test_recommend_restaurant_location_not_found(mock_requests_get):
    # Configure mock response for location not found
    mock_requests_get.return_value = MagicMock(status_code=200, json=lambda: {"results": []})

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Unknown Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Location not found." in str(excinfo.value.detail)

def test_recommend_restaurant_isochrone_map_not_generated(mock_requests_get):
    # Configure mock responses for isochrone map not generated
    mock_requests_get.side_effect = [
        MagicMock(status_code=200, json=lambda: mock_geocode_response_success), # Geocode
        MagicMock(status_code=200, json=lambda: {"features": []})  # Isoline (no features)
    ]

    # Call the function and expect an HTTPException
    with pytest.raises(HTTPException) as excinfo:
        recommend_restaurant(
            location="Test Location",
            mode=TravelMode.drive,
            time_range=15,
            categories=[CateringType.restaurant]
        )
    assert excinfo.value.status_code == 422
    assert "Can not generate isochrone map." in str(excinfo.value.detail)
    
    # Check that "drive" was used in the Isoline API call
    assert f"mode={TravelMode.drive.value}" in mock_requests_get.call_args_list[1][0][0]
