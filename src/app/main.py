import os
from typing import Any

import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from app.system.system import InformationRetrievalSystem
from app.utils.utils import get_df

if not os.path.exists(path="./relevants"):
    os.makedirs(name="./relevants")

df: pd.DataFrame = pd.read_csv(filepath_or_buffer="./classes.csv")

major_description_model = InformationRetrievalSystem(
    df=df, col="Major_Course_Description"
)

st.title(body="Information Retrieval System")
query: str = st.text_input(
    label="insert your query:", placeholder="example: computer science"
)

quantity: int = st.slider(
    label="number of results:", min_value=1, max_value=100, value=10
)

major_description_model_search: pd.DataFrame = major_description_model.search(
    query=query, topn=100
)

if major_description_model_search.shape[0] > 0:
    df = get_df(query=query)
    c: DeltaGenerator = st.container()
    c.write("results:")
    for i in range(major_description_model_search.shape[0]):
        expander: DeltaGenerator = st.expander(
            label=f"{major_description_model_search.iloc[i]['Course Title']}"
        )
        expander.write(
            "major: {}".format(major_description_model_search.iloc[i]["Major"])
        )
        expander.write(
            "description: {}".format(
                major_description_model_search.iloc[i]["Course Description_Clean"]
            )
        )
        value: bool = major_description_model_search.iloc[i]["ID"] in df["ID"].values
        agree: bool = expander.checkbox(label="is it relevant?", key=i, value=value)
        if agree:
            if major_description_model_search.iloc[i]["ID"] in df["ID"].values:
                expander.write("already marked as relevant")
            else:
                expander.write("thanks!")
                new_row: dict[str, int | Any] = {
                    "Unnamed: 0": len(df),
                    "ID": major_description_model_search.iloc[i]["ID"],
                }
                df = pd.concat(
                    objs=[df, pd.DataFrame(data=[new_row])], ignore_index=True
                )
                df.to_csv(path_or_buf=f"./relevants/{query}_relevants.csv", index=False)
