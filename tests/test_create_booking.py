import allure
import pytest


@allure.feature('Test Create Booking')
@allure.story('Test connection')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    assert 'bookingid' in response
    booking = response['booking']
    assert booking['firstname'] == generate_random_booking_data['firstname']
    assert booking['lastname'] == generate_random_booking_data['lastname']
    assert booking['totalprice'] == generate_random_booking_data['totalprice']
    assert booking['depositpaid'] == generate_random_booking_data['depositpaid']
    assert booking['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert booking['bookingdates']["checkout"] == generate_random_booking_data['bookingdates']['checkout']
    assert booking['additionalneeds'] == generate_random_booking_data['additionalneeds']



