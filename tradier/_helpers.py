"""helpers.py collection of global utilities"""
from os import path
from enum import Enum
import logging

import requests

HERE = path.abspath(path.dirname(__file__))

class EndpointMode(Enum):
    """switch class for endpoint access modes"""
    REQUEST = 'https://api.tradier.com/v1/'
    STREAMING = 'https://stream.tradier.com/v1/'
    BETA = 'https://api.tradier.com/beta/'
    SANDBOX = 'https://sandbox.tradier.com/v1/'

ENDPOINT_ROOT = EndpointMode.REQUEST.value

LOGGER = logging.getLogger('ProsperTradier')
LOGGER.addHandler(logging.NullHandler())

GENERIC_HEADER = {
    'Accept':'application/json',
    'User-Agent':'ProsperTradier application'   #TODO
}
def generic_get_call(
        address,
        params,
        auth_header,
        headers=None
):
    """generic GET HTTP request

    Args:
        address (str): complete url
        params (:obj:`dict`): REST arguments
        auth_key (:obj:`dict`): auth key/value pair
        headers (:obj:`dict`, optional): call headers

    Returns:
        (:obj:`dict`) response from GET HTTP endpoint
    """
    sent_headers = dict(GENERIC_HEADER) #save copy
    sent_headers.update(headers)
    sent_headers.update(auth_header)

    LOGGER.debug('URL:{0}'.format(address))
    LOGGER.debug('params:{0}'.format(params))
    LOGGER.debug('headers:{0}'.format(headers))

    req = requests.get(
        address,
        params=params,
        headers=sent_headers
    )
    req.raise_for_status()
    data = req.json()

    return data
