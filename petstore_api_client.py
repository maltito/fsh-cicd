import requests
from config import API_KEY, BASE_URL

class PetstoreClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"api_key": API_KEY}

    def create_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.post(url, json=pet_data, headers=self.headers)
        return response


    def get_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url, headers=self.headers)
        return response
    
    
    def update_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.put(url, json=pet_data, headers=self.headers)
        return response
    

    def delete_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.delete(url, headers=self.headers)
        return response