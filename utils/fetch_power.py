# utils/fetch_power.py
import requests
import pandas as pd
import numpy as np

def fetch_power_point(lat, lon, start_date, end_date,
                      params="T2M,RH2M,ALLSKY_SFC_SW_DWN"):
    """
    Fetch hourly NASA POWER data for a single lat/lon.
    start_date, end_date: datetime.date objects
    """
    url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
    payload = {
        "start": start_date.strftime("%Y%m%d"),
        "end": end_date.strftime("%Y%m%d"),
        "latitude": lat,
        "longitude": lon,
        "parameters": params,
        "community": "RE",
        "format": "JSON"
    }
    r = requests.get(url, params=payload, timeout=60)
    r.raise_for_status()
    data = r.json()

    ts = data.get('properties', {}).get('parameter', {})
    if not ts:
        raise RuntimeError("No data returned from POWER API.")
    example_param = next(iter(ts))
    times = sorted(ts[example_param].keys())
    rows = []
    for t in times:
        rows.append({
            "timestamp_utc": pd.to_datetime(t, format="%Y%m%d%H", utc=True),
            **{param: ts[param].get(t, np.nan) for param in ts}
        })
    df = pd.DataFrame(rows).set_index('timestamp_utc').sort_index()
    # standard missing flag -> NaN
    df = df.replace(-999.0, np.nan).astype(float)
    return df
