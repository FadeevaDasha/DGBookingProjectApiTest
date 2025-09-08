from http.client import responses
from urllib.error import HTTPError

from pydantic import ValidationError
from core.models.booking import BookingResponse

import allure
import pytest
import requests


@allure.feature('Test Create Booking')
@allure.story('Test create valid booking')
def test_create_booking_generate_random_data(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']["checkout"] == generate_random_booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == generate_random_booking_data['additionalneeds']


@allure.feature('Test Create Booking')
@allure.story('Positive: create booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']["checkout"] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test Create Booking')
@allure.story('Positive: create booking with with a double name')
def test_create_booking_with_double_name(api_client):
    booking_data = {
        "firstname": "Ivan-Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']["checkout"] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test Create Booking')
@allure.story('Positive: create booking with a long lastname')
def test_create_booking_with_long_lastname(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Garcia-Lopez-Martinez-Rodriguez",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']["checkout"] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test Create Booking')
@allure.story('Positive: create booking without additionalneeds')
def test_create_booking_without_additionalneeds(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": None
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']["checkout"] == booking_data['bookingdates']['checkout']


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty data')
def test_create_booking_with_empty_data(api_client):
    booking_data = {
        "firstname": None,
        "lastname": None,
        "totalprice": None,
        "depositpaid": None,
        "bookingdates": {
            "checkin": None,
            "checkout": None
        },
        "additionalneeds": None
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty firstname')
def test_create_booking_with_empty_firstname(api_client):
    booking_data = {
        "firstname": None,
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty lastname')
def test_create_booking_with_empty_lastname(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": None,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty totalprice')
def test_create_booking_with_empty_totalprice(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": None,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty bookingdates')
def test_create_booking_with_empty_bookingdates(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": None,
            "checkout": None
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty checkin')
def test_create_booking_with_empty_checkin(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": None,
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with empty checkout')
def test_create_booking_with_empty_checkout(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-10",
            "checkout": None
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with checkin more checkout')
def test_create_booking_with_checkin_more_checkout(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-10",
            "checkout": "2025-02-02"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with checkout instead of checkin')
def test_create_booking_with_checkout_instead_checkin(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkout": "2025-02-02",
            "checkin": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with invalid bookingdates')
def test_create_booking_with_invalid_bookingdates(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkout": "2025-24-02",
            "checkin": "2025-02-ab"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with a negative totalprice')
def test_create_booking_with_negative_totalprice(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": -150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with totalprice, text instead of numbers')
def test_create_booking_with_totalprice_text_instead_numbers(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 12976576476464368039483589340985,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"


@allure.feature('Test Create Booking')
@allure.story('Negative: create booking with zero in totalprice')
def test_create_booking_with_zero_in_totalprice(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 0,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    try:
        api_client.create_booking(booking_data)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 500, f"Expected 500 but got {e.response.status_code}"