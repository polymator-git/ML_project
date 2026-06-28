import json
from pathlib import Path

from src.api.football_api import FootballAPI

api = FootballAPI()
print("Downloading fixtures...")
data = api.get_fixtures(
    league=39,
    season=2024
)
Path("data/raw").mkdir(parents=True, exist_ok=True)
with open("data/raw/premier_league_2024.json", "w") as f:
    json.dump(data, f, indent=4)

print("Download Complete!")