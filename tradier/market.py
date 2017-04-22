from os import path

import tradier._helpers as helpers
import tradier.auth as auth

HERE = path.abspath(path.dirname(__file__))

QUOTES_URI = '/v1/markets/quotes'
def get_quote(
        symbol_list,
        auth_key,
        endpoint_root=helpers.ENDPOINT_ROOT,
        quotes_uri=QUOTES_URI
):
    """fetch price quote from tradier

    Notes:
        https://developer.tradier.com/documentation/markets/get-quotes

    Args:
        symbol_list (str): list of symbol to fetch
        auth_key (:obj:`auth.TradierAuth`): auth object
        endpoint_root (str, optional): tradier root address
        quotes_uri (str, optional): route to quotes endpoint
        logger (:obj:`logging.logger`, optional): logging handle

    Returns:
        (:obj:`dict`) tradier_quote response
        {symbol, description, exch, type, change, change_percentage
        volume, average_volume, last_volume, trade_date, open, high, low,
        close, prevclose, week_52_high, week_52_low, bid, bidsize, bidexch,
        bid_date, ask, asksize, askexch, ask_date, open_interest, underlying,
        strike, contract_size, expiration_date, expiration_type, option_type}

    """
    quote_addr = '{base_url}{quotes_uri}'.format(
        base_url=endpoint_root,
        quotes_uri=quotes_uri
    )
    params = {'symbols':symbol_list}

    data = helpers.generic_get_call(
        quote_addr,
        params,
        auth_key.generic_auth()
    )

    return data
