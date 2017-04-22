"""test_version.py: setup pytest defaults/extensions"""
from os import path

import pytest

import tradier._helpers as helpers

HERE = path.abspath(path.dirname(__file__))
ROOT = path.abspath(path.dirname(HERE))

ECHO_ENDPOINT = 'https://postman-echo.com/get'
def test_GET_happypath():
    """validate GET helper is working"""
    test_params = {
        'key1':'val1',
        'key2':'val2'
    }
    test_auth = {
        'Authorization': 'I AM THE ADMINISTRATOR!'
    }
    test_headers = {
        'User-Agent': 'Prosper Tradier TEST'
    }

    data = helpers.generic_get_call(
        address=ECHO_ENDPOINT,
        params=test_params,
        auth_header=test_auth,
        headers=test_headers
    )

    assert data['args'] == test_params
    for key in test_headers:
        assert data['headers'][key.lower()] == test_headers[key]

    assert data['headers']['authorization'] == test_auth['Authorization']

    for key in helpers.GENERIC_HEADER:
        if key == 'User-Agent':
            #Validate User-Agent can be overwritten
            assert data['headers'][key.lower()] != helpers.GENERIC_HEADER[key]
        else:
            assert data['headers'][key.lower()] == helpers.GENERIC_HEADER[key]
