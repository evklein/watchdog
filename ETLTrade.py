import requests

if __name__ == "__main__":
    res = requests.get("https://api.census.gov/data/timeseries/intltrade/exports/hs?get=DISTRICT,DIST_NAME,E_COMMODITY,E_COMMODITY_LDESC,ALL_VAL_MO,ALL_VAL_YR,VES_VAL_MO,VES_VAL_YR&YEAR=2024&MONTH=02&DISTRICT=70&key=1b5f57af004bd97bfe47a8ded2c1a9b432848bda")
    print(res.text)
