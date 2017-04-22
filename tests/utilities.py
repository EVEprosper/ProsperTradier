"""utilities.py: helper functions for testing"""
from os import path
import configparser
import logging

HERE = path.abspath(path.dirname(__file__))
ROOT = path.abspath(path.dirname(HERE))

TEST_CONFIG_FILE = path.join(HERE, 'test.cfg')
CONFIG = parse_test_config(TEST_CONFIG_FILE)
def parse_test_config(config_filepath=TEST_CONFIG_FILE):
    """loads test.cfg for use in tests

    Args:
        config_filepath (str): path to config file

    Returns:
        (:obj:`configparser.ConfigParser)
    """
    config_parser = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation(),
        allow_no_value=True,
        delimiters=('='),
        inline_comment_prefixes=('#')
    )
    with open(config_filepath, 'r') as cfg_fh:
        config_parser.read_file(cfg_fh)

    return config_parser

def get_config(
        section_name,
        key_name,
        config=CONFIG
):
    """wrapper for configparser.get() to check env for vals
    Make travis secret-keeping easier

    Args:
        section_name (str): config section
        key_name (str): config key
        config (:obj:`configparser.ConfigParser, optional): config to search

    Returns:
        (str) value from config or env
    """
    try:
        value = config.get(section_name, key_name)
    except configparser.NoOptionError:
        pass
    except configparser.NoSectionError:
        raise

    if value:
        return value
    else:
        env_value = get_value_from_env(section_name, key_name)

    if env_value:
        return env_value
    else:
        raise Exception

ENVNAME_PAD = 'PROSPER'
def get_value_from_env(
        section_name,
        key_name,
        envname_pad=ENVNAME_PAD
):
    """check environment for key/value pair

    Args:
        section_name (str): config section
        key_name (str): config key
        envname_pad (str, optional): namespace pad

    Returns:
        (str): value from environment
    """
    var_name = '{pad}_{section}__{key}'.format(
        pad=envname_pad,
        section=section_name,
        key=key_name
    )
    value = getenv(var_name)

    return value
