import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_data(from_currency, to_currency):
    try:
        response = requests.get(os.getenv('API_URL'), params={
                                'from': from_currency, 'to': to_currency, 'api_key': os.getenv('API_KEY')})
        return response.json()
    except requests.exceptions.RequestException as e:
        return None
