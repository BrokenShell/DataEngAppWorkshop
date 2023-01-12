import os
import uuid

import pandas as pd
import streamlit


def main():
    streamlit.set_page_config(page_title="Data Eng", layout="wide")
    upload_file = streamlit.file_uploader("Upload a file", type=["csv"])
    if upload_file:
        filepath = f"temp/{uuid.uuid4()}.csv"
        df = data_eng(pd.read_csv(upload_file))
        df.to_csv(filepath, index=False)
        with open(filepath, "r") as file:
            streamlit.download_button(
                data=file,
                label="Download File",
                file_name=upload_file.name,
            )
        os.remove(filepath)


def data_eng(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["_id", "Time Stamp"])
    df.columns = [col.lower() for col in df.columns]
    return df


if __name__ == '__main__':
    main()
