import json
import os

from src.api.football_api import FootballAPI

api = FootballAPI()

# Create folder if it doesn't exist
os.makedirs("data/raw/statistics", exist_ok=True)

# Load fixtures
with open("data/raw/premier_league_2024.json", "r") as f:
    fixtures = json.load(f)

# Loop through every fixture
for fixture in fixtures["response"]:

    fixture_id = fixture["fixture"]["id"]

    print(f"Downloading statistics for {fixture_id}...")

    try:
        data = api.get_fixture_statistics(fixture_id)

        with open(f"data/raw/statistics/{fixture_id}.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

    except Exception as e:
        print(f"Failed for {fixture_id}: {e}")

print("Finished downloading statistics!")