from pathlib import Path
from datetime import datetime

import pandas as pd


OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def save_news(news_list):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    file_path = OUTPUT_DIR / f"headline_{timestamp}.csv"

    df_headlines = pd.DataFrame(
        news_list,
        columns=["title", "subtitle", "link"]
    )

    df_headlines.to_csv(
        file_path,
        index=False,
        encoding="utf-8-sig"
    )

    return file_path