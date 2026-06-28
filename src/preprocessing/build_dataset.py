import os
import json
import pandas as pd

from src.preprocessing.helpers import statistics_to_dict

DATA_FOLDER = "data/raw/statistics"

rows = []

for filename in os.listdir(DATA_FOLDER):

    filepath = os.path.join(DATA_FOLDER, filename)

    with open(filepath, "r") as f:
        match = json.load(f)

    response = match.get("response", [])

# Skip invalid or incomplete responses
    if len(response) != 2:
        print(f"Skipping {filename} - Invalid response")
        continue

    home = response[0]
    away = response[1]
    home_stats = statistics_to_dict(home["statistics"])
    away_stats = statistics_to_dict(away["statistics"])

    row = {
        "home_team": home["team"]["name"],
        "away_team": away["team"]["name"],

        "home_xg": home_stats.get("expected_goals"),
        "away_xg": away_stats.get("expected_goals"),

        "home_shots": home_stats.get("Total Shots"),
        "away_shots": away_stats.get("Total Shots"),

        "home_possession": home_stats.get("Ball Possession"),
        "away_possession": away_stats.get("Ball Possession"),

        "home_corners": home_stats.get("Corner Kicks"),
        "away_corners": away_stats.get("Corner Kicks"),
    }

    rows.append(row)

df = pd.DataFrame(rows)

os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/match_dataset.csv", index=False)

print(df.head())