import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.price_url = os.environ.get("SHEETY_PRICES_URL")
        self.desination_data = {}
        self.users_url = os.environ.get("SHEETY_USERS_URL")
        self.customer_data = {}
        self.headers = {
    "Authorization": os.environ.get("SHEETY_AUTH")
}
    def get_destination(self):
        response = requests.get(url=self.price_url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.desination_data = data["prices"]
        return self.desination_data
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{self.price_url}/{row_id}",
            json=new_data,
            headers=self.headers
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

    def get_customer_emails(self):
        response = requests.get(url=self.users_url, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data