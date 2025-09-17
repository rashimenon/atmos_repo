# Air Quality Forecast — PM2.5 (Delhi)

This repository contains a Jupyter notebook and small utilities to fetch NASA POWER hourly weather data, combine it with station PM2.5 (CPCB) data, train a baseline model and visualize forecasts.

## Quick start (Linux/Windows with Anaconda)

1. Clone:
git clone https://github.com/YOUR_USERNAME/air_quality_forecast.git


2. Create environment (recommended):

conda create -n atmos python=3.10 -y
conda activate atmos
pip install -r requirements.txt
python -m ipykernel install --user --name atmos --display-name "Python (atmos)"


3. Open notebook:

jupyter lab

Open `notebooks/pm25_forecast.ipynb` and select kernel **Python (atmos)**. Run cells sequentially.

## Files
- `notebooks/pm25_forecast.ipynb` — main notebook (fetch, merge, feature engineering, baseline RF, graph).
- `utils/fetch_power.py` — NASA POWER helper function.
- `data/` — raw CSVs (place CPCB CSVs here).
- `models/` — saved models and scalers.

## Notes
- CPCB data: download station CSVs from CPCB / data.gov.in and place under `data/`.
- This repo uses NASA POWER (no auth) and public CPCB station files.
