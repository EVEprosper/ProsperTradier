"""helpers.py collection of global utilities"""
from os import path
from enum import Enum
import logging

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
