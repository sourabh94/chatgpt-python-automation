import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write linux script to check os version.",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open('linux-script.sh', "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
