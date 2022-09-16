import sys

def display_stck_price(brand_name):

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

    if brand_name in COMPANIES:
        print(STOCKS[COMPANIES[brand_name]])
    else:
        print('Unknown company')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        display_stck_price(sys.argv[1].capitalize())