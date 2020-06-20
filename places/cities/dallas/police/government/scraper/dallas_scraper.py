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
TODAY = date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)


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

        # results = client.get("qv6i-rri7", where="date1 BETWEEN '" + str(YESTERDAY) + "T00:00:00.000' AND '" +
        #                                         str(YESTERDAY) + "T23:59:59.000'", limit=500)

        # results = client.get("qv6i-rri7", where="date1 = '" + "2020-06-20" + "T00:00:00.000'", limit=500)
        results = client.get("qv6i-rri7", where="date1 > '" + "2020-06-20" + "'", limit=500)
        results_df = pd.DataFrame.from_records(results)
        print (results_df)

        # return dallas_tables




