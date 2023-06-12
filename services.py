import requests
import os
BACKEND_BASE_URL = os.getenv('BACKEND_BASE_URL', 'http://localhost:4000')

def get_variable_names():
    # response = requests.get('http://localhost:4000/api/variables')
    response = requests.get(f'{BACKEND_BASE_URL}/api/variables')
    return response.json()

def get_variable_data(variable):
    #response = requests.get(f'http://localhost:4000/api/data/variable/{variable}/day')
    response = requests.get(f'{BACKEND_BASE_URL}/api/data/variable/{variable}/day')
    return response.json()

def get_history_data():
    response = requests.get(f'{BACKEND_BASE_URL}/api/data/history')
    #response = requests.get(f'http://localhost:4000/api/data/history')
    return response.json()