"""
Get water quality data from the city of Calgary database.
"""

import requests
import datetime as dt
from urllib.parse import urlencode

cutoff_dt = dt.datetime.now() - dt.timedelta(days=5)

base_url = "https://data.calgary.ca/resource/y8as-bmzj.json"

parameters = {
    "$where": f"sample_date > '{cutoff_dt:%Y-%m-%dT%H:%M:%S}'"
}

query_string = urlencode(parameters)

full_url = f"{base_url}?{query_string}"
result = requests.get(full_url, verify=False).json()