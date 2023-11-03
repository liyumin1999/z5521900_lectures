"""yf example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf
import os

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """Downloads stock prices from Yahoo Finance and saves the information in a CsV file.

    Parameters:
    tic : str
        Ticker
    pth : str
        Location of the output CsV file
    start : str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-1-01'
    end : str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

if __name__ == "_main":
   tic = 'QAN.AX'
   pth = os.path.join('YOUR_DATA_DIRECTORY_PATH', 'qan_stk_prc.csy') # Replace 'YOUR DATA DIRECTORY PATH' with the actual path
   yf_prc_to_csv(tic, pth)