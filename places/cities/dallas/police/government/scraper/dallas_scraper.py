#!/usr/bin/env python3
#
# Data Model to represent Centralized Police Data
#
# ------------------------------------------------


# Import modules
# --------------
import camelot.io
import pandas as pd
from sodapy import Socrata
import datetime
from datetime import date

# Constants
# ---------
BEGINNING_DATE = "2020-06-09"
ENDING_DATE = "2020-06-15"

class DallasScraper(object):


    """

    Dallas Scraper to fetch the data out of the PDF

    """

    __version__ = "0.1.0"

    def __init__(self):

        """

        Initialize the DallasScraper Setup.

        """

        self.file = self.fetch_crime_data()

    def fetch_crime_data(self):


        """

        Fetches the Dallas daily crime report data that comes as a PDF.

        Resources:
            Crime Data (Link): https://dallaspolice.net/resources/CrimeReports/NIBRS%20REPORT%20Compstat%20Daily.pdf


        Return:
            dallas_tables (Pandas Dataframe): Dataframe of the parsed PDF


        """

        # Read remote pdf into list of DataFrame

        # dallas_crime_feeds = feedparser.parse("https://www.dallasopendata.com/api/views/qv6i-rri7/rows.rss")

        client = Socrata("www.dallasopendata.com", 'o0H6i1rlXZOTSU5djUJCFKT8x')

        results = client.get("qv6i-rri7", where="date1 BETWEEN '" + str(BEGINNING_DATE) + "T00:00:00.000' AND '" +
                                                str(ENDING_DATE) + "T23:59:59.000'", limit=10000)

        results_df = pd.DataFrame.from_records(results)
        results_df.to_csv('dallas_police_government.csv')





