import pandas as _pd
import numpy as _np
import yfinance as _yf
from yahoo_fin import stock_info as _si


_yfinance_priod_options = ('1d', '5d', '1mo', '3mo', '6mo',
                                  '1y', '2y', '5y', '10y', 'max', 'ytd')

_yfinance_details_options = ['info','actions','dividends','splits','financials',
                            'quarterly_financials','major_holders','institutional_holders',
                            'balance_sheet','quarterly_balance_sheet','cashflow',
                            'quarterly_cashflow','earnings','quarterly_earnings','sustainability',
                            'recommendations','calendar','options','all',
                            ]


def get_all_tickers():
    """ Return all tickers at NYSE"""
    _f1 = _pd.DataFrame(_si.tickers_sp500())
    _df2 = _pd.DataFrame(_si.tickers_nasdaq())
    _df3 = _pd.DataFrame(_si.tickers_dow())
    _df4 = _pd.DataFrame(_si.tickers_other())
    sym1 = set(symbol for symbol in _f1[0].values.tolist())
    sym2 = set(symbol for symbol in _df2[0].values.tolist())
    sym3 = set(symbol for symbol in _df3[0].values.tolist())
    sym4 = set(symbol for symbol in _df4[0].values.tolist())

    symbols = set.union(sym1, sym2, sym3, sym4)
    return sorted(symbols)

def get_sp500_portfolio():
    payload = _pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    first_table = payload[0]
    second_table = payload[1]

    df = first_table
    df = df.set_index('Symbol')
    df = df.sort_index()
    return df.copy()


def get_dow_portfolio():
    payload = _pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
    first_table = payload[0]
    second_table = payload[1]

    df = second_table
    df = df.set_index('Symbol')
    df = df.sort_index()
    return df.copy()

def get_brk_subsidiaries():
    payload = _pd.read_html('https://en.wikipedia.org/wiki/List_of_assets_owned_by_Berkshire_Hathaway')
    table = payload[1]
    df = table
    df = df.set_index('Company')
    df = df.sort_index()
    return df.copy()

def get_brk_portfolio():
    payload = _pd.read_html('https://en.wikipedia.org/wiki/List_of_assets_owned_by_Berkshire_Hathaway')
    table = payload[2]
    df = table
    df['Ticker'].replace('NYSE:', '', regex=True, inplace=True)
    df['Ticker'].replace('Nasdaq:', '', regex=True, inplace=True)
    df['Ticker'].replace('NYSE', '', regex=True, inplace=True)
    df['Ticker'].replace('Arca:', '', regex=True, inplace=True)
    df['Ticker'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
    df = df.set_index('Ticker')
    df = df.sort_index()
    return df.copy()



def get_yfinance_priod_options():
    return _yfinance_priod_options


def get_yfinance_details_options():
    return _yfinance_details_options

def get_yfinace_history_close(ticker, period="10y"):
    print('---- INFO ----',f"Geting close history of ticker {ticker}")
    if period not in get_yfinance_priod_options():
        raise ValueError(f"period must be one of {get_yfinance_priod_options()}")
    stock = _yf.Ticker(ticker).history(period=period)['Close']
    if not isinstance(stock,_pd.Series):
        raise ValueError(f"yfinance for ticker {ticker} close history not comleted")
    stock.rename_axis('Close')
    return _pd.Series(stock)

def get_yfinace_history(ticker, period="10y"):
    print('---- INFO ----',f"Geting history of ticker {ticker}")
    if period not in get_yfinance_priod_options():
        raise ValueError(f"period must be one of {get_yfinance_priod_options()}")
    stock = _yf.Ticker(ticker).history(period=period)
    if not isinstance(stock,_pd.DataFrame):
        raise ValueError(f"yfinance for ticker {ticker} history not comleted")
    close = stock['Close']
    retcom = close.returns_com()
    stock['Return_Com'] = retcom
    return stock



def get_yfinance_stock_details(ticker,details='info'):
    print('---- INFO ----', f"Geting {details} details of ticker {ticker}")
    if details not in get_yfinance_details_options():
        raise ValueError(f"period must be one of {get_yfinance_details_options()}")
    cmd = f"_yf.Ticker('{ticker}').{details}"
    stock = eval(cmd)
    if stock is None:
        stock = _pd.DataFrame()
        return stock
    if details == 'info':
        if not isinstance(stock, dict):
            raise ValueError(f"yfinance for ticker {ticker} details {details} not completed")
        stock = _pd.DataFrame.from_dict(stock,orient="index")
        stock.columns = ['info']
    if details == 'options':
        if not isinstance(stock, tuple):
            raise ValueError(f"yfinance for ticker {ticker} details {details} not completed")
        stock = _pd.DataFrame(stock)
        stock.columns = ['options']
    return stock


def get_yfinance_stock_details_all(ticker):
    all_detail = dict()
    all_detail['history'] = get_yfinace_history(ticker)
    for d in get_yfinance_details_options():
        if d == 'all':
            continue
        all_detail[d] = get_yfinance_stock_details(ticker, details=d)
    return all_detail


class FinacialRatios():
    """  מכפילים פיננסיים """

    def PE(self):
      """
      https://www.investopedia.com/terms/p/price-earningsratio.asp
The price-to-earnings ratio (P/E ratio) is the ratio for valuing a company that measures its current
share price relative to its earnings per share (EPS).
The price-to-earnings ratio is also sometimes known as the price multiple or the earnings multiple.
P/E ratios are used by investors and analysts to determine the relative value of a company's shares in an
apples-to-apples comparison.
It can also be used to compare a company against its own historical record or to compare aggregate markets
against one another or over time.
P/E may be estimated on a trailing (backward-looking) or forward (projected) basis.
        """

    pass
