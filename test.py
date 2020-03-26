from secedgar.filings import Filing, FilingType
# This will download the past 15 10-Q filings made by Apple.
import pandas as pd

path = '/Users/schen/sec-scraper/data/cik_ticker.csv'
df = pd.read_csv(path, sep='|')

def run(df):
    cik = list(df['CIK'])
    names = list(df['Name'])
    for c, n in zip(cik, names):
        if len(str(c)) < 10:
            missing = 10 - len(str(c))
            temp = ("0" * missing) + str(c)
            print("SCRAPING {} ...".format(temp))
        my_filings = Filing(cik=temp, filing_type=FilingType.FILING_10K) # 10-Q filings for Apple (NYSE: AAPL)
        try:
            my_filings.save('./filings/') # Saves last 15 10Q reports from AAPL to ~/path/to/dir
        except ValueError:
            print("No {}".format(n))

run(df)