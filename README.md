# 🌍 Air Quality Forecast — PM2.5 (Delhi)

This repository provides a simple pipeline to **forecast PM2.5 air pollution in Delhi** using:
- **NASA POWER** hourly weather reanalysis data (temperature, humidity, radiation)
- **CPCB station data** for PM2.5 levels  
- A baseline **machine learning model (Random Forest)** for predictions  
- Jupyter notebook for visualization (graphs & alerts)

---

## 🚀 Quick Start (Windows/Linux with Anaconda)

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/atmos_repo.git
cd atmos_repo
```
### 2. Install prerequisites
(a) Install [Anaconda](https://www.anaconda.com/download)(skip if already installed).
Make sure Anaconda is added to PATH.

(b) Create and activate environment
```bash
conda create -n atmos python=3.10 -y
conda activate atmos
```
(c) Install required packages
```bash
pip install -r requirements.txt
```
(d) Add kernel to Jupyter
```bash
python -m ipykernel install --user --name atmos --display-name "Python (atmos)"
```
### 3. Run the notebook
```bash
jupyter lab
```
- Open notebooks/pm25_forecast.ipynb
- Select kernel Python (atmos)
- Run cells sequentially

This will:
- Fetch NASA POWER hourly data
- Merge with CPCB PM2.5 CSVs
- Train a baseline ML model
- Plot PM2.5 forecasts & alerts

## Data Sources
- [NASA POWER API](https://power.larc.nasa.gov/)
- (Free, no authentication needed)
- [CPCB Air Quality Data (PM2.5)](https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing)
- Download station CSVs and place under data/.

## Requirements
Python 3.10+ with the following libraries (see requirements.txt):

numpy
pandas
scikit-learn
matplotlib
requests
jupyter / jupyterlab
Install with:
pip install numpy pandas scikit-learn matplotlib requests jupyterlab

## Notes
- Threshold alerts are included in the notebook (e.g. PM2.5 > 100 triggers a “Poor Air Quality” warning).
- Extendable: you can add deep learning models or connect to a web app for notifications.
- The repo is structured so future datasets/models can be added easily.
