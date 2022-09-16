import sys

def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key

def ticker_symbols(ticker_symbol):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if ticker_symbol not in STOCKS:
        print('Unknown ticker')
    else:
        brand_name = get_key(COMPANIES, ticker_symbol)
        print(brand_name + ' ' + str(STOCKS[COMPANIES[brand_name]]))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_symbols(sys.argv[1].upper())
