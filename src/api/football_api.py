import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FootballAPI:

    def __init__(self):
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {
            "x-apisports-key": os.getenv("API_FOOTBALL_KEY")
        }
        self.api_key = os.getenv("API_FOOTBALL_KEY")
        print(f"API Key Loaded: {self.api_key}")

    def get_fixtures(self, league, season):
        endpoint = f"{self.base_url}/fixtures"

        params = {
            "league": league,
            "season": season
        }

        response = requests.get(
            endpoint,
            headers=self.headers,
            params=params
        )
        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text)
        response.raise_for_status()

        return response.json()
    
    def get_fixture_statistics(self, fixture_id):
        endpoint = f"{self.base_url}/fixtures/statistics"

        params = {
            "fixture": fixture_id
        }

        response = requests.get(
            endpoint,
            headers=self.headers,
            params=params
        )

        response.raise_for_status()

        return response.json()

     