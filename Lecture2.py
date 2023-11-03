""" yf example3 .py
Downloads Qantas stock price data for a given year and saves it to a CSV file.
"""
import os
import toolkit_config as cfg
import yf_example2 as yf2

def gan_prc_to_csv(year):
    """ Downloads Qantas stock prices for a given year into a CSV file.

    Parameters:
    year : int
        The year for which you want to download stock prices.

    The CSy file will be saved under the data folder with a filename like 'qan_prc_YYYY.csv'.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    tic = 'QAN.AX'
    file_name = f'qan_prc_{year}.csv'
    output_path = os.path.join(cfg.DATADIR, file_name)

    yf2.yf_prc_to_csv(tic, output_path, start=start_date, end=end_date)

if _name_ == " main":
    year_to_download = 2023 # Change this to the desired year
    qan_prc_to_csv(year_to_download)