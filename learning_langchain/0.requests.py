import requests
import os
import json

url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']
}
data = {
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
  ]
}

response = requests.post(url=url, headers=headers, json=data)
print(json.dumps(response.json(), indent=2))
