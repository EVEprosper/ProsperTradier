"""auth.py: tradier auth handler"""
from os import path

import requests

import tradier._helpers as helpers

HERE = path.abspath(path.dirname(__file__))

GENERAL_AUTH_TOKEN = None

class TradierAuth(object):
    """wrapper for authentication in Tradier"""
    def __init__(self, access_token):
        self.access_token = access_token
        self.client_id = None
        self.scope = None
        self.expires_in = None
        self.issued_at = None
        self.status = None

    def generic_auth(self):
        """for endpoints that only need app authorization"""
        auth_header = {
            'Authorization': 'Bearer {0}'.format(self.access_token)
        }
        return auth_header

AUTH_AUTHORIZE_URI = '/v1/oauth/authorize'
def get_auth_code():
    """fetch authorization code from oAuth

    Notes:
        https://developer.tradier.com/documentation/oauth/authorization-code

    Returns:
        TBD
    """
    pass

AUTH_ACCESSTOKEN_URI = '/v1/oauth/accesstoken'
def get_access_token():
    """fetch access token from oAuth

    Notes:
        https://developer.tradier.com/documentation/oauth/access-token

    Returns:
        (:obj:`dict`) tradier_accesstoken response
        {access_token, expires_in, issued_at, scope, status}
    """
    pass
