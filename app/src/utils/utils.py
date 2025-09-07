import re

import pandas as pd
from nltk.corpus import stopwords


def get_df(query: str) -> pd.DataFrame:
    try:
        df: pd.DataFrame = pd.read_csv(
            filepath_or_buffer=f"./relevants/{query}_relevant.csv"
        )
    except Exception:
        df = pd.DataFrame()

    if "Unnamed: 0" not in df.columns:
        df["Unnamed: 0"] = []
    if "ID" not in df.columns:
        df["ID"] = []

    return df


def query_processing(query: str) -> str:
    new_query: str = re.sub(pattern=r"\W", repl=" ", string=query)
    new_query = new_query.strip().lower()
    new_query = " ".join(
        [
            word
            for word in new_query.split()
            if word not in stopwords.words(fileids="english")
        ]
    )
    return query
