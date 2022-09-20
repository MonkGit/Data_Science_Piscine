from bs4 import BeautifulSoup
import sys
import requests
import time

def parse_html():
    time.sleep(5)
    web = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})
    if web.status_code != 200:
        raise Exception("page is not found")
    soup = BeautifulSoup(web.text, "html.parser")
    rows = soup.find_all('div', attrs={'data-test' : 'fin-row'})
    for i in rows:
        if i.find("div", attrs={'title' : sys.argv[2]}) is not None:
            cols = i.find_all('div', {'data-test' : 'fin-col'})
            return tuple([sys.argv[2], *[j.text for j in cols]])
    raise Exception("statement name is not found")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("invalid info")
    data = parse_html()
    if data is None:
        raise Exception("invalid info")
    print(data)
