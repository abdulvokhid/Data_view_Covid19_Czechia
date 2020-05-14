import requests
import json

# this tokens taken from tool named parsehub which automatically transfers data which we need
api_key = "t3QJjgbvqOC3"
project_token = "thovKo8zeufk"
run_token = "tpad2vUW5ht9"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{project_token}/last_ready_run/data', params={"api_key": api_key})
data = json.loads(response.text)


print(data)