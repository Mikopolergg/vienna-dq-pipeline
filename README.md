# Vienna tree register: data quality pipeline

A student project where I check the quality of the tree register of the City of Vienna (Baumkataster) and build a small pipeline around it. I'm doing it to learn DuckDB, Pandera, Streamlit and pytest, and to practice finding and describing problems in real data.

**Status:** work in progress. Setup is done, loading and profiling the data is next.

## Data

- Source: Baumkataster Wien, published by Stadt Wien on data.gv.at
- Attribution: Datenquelle: Stadt Wien - https://data.wien.gv.at
- Licence: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.en)
- File: `BAUMKATOGD.csv`, about 53 MB, 19 columns, one row per tree
- The raw file is not in this repository because of its size. To run the project, download it from data.gv.at and save it as `data/raw/baumkataster.csv`.

## Setup (Windows, PowerShell)

    git clone https://github.com/Mikopolergg/vienna-dq-pipeline.git
    cd vienna-dq-pipeline
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

I use Python 3.10.

## Plan

- [x] Setup and choosing the dataset
- [ ] Load the data into DuckDB
- [ ] Profile the data and find problems
- [ ] Write data quality checks (SQL and Pandera)
- [ ] Build a Streamlit dashboard for the results
- [ ] Add tests and automatic checks on GitHub
- [ ] Write up what I found

## Tools

Python, pandas, DuckDB, Pandera, Streamlit, pytest