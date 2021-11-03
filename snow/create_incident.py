import json,os
import requests
from requests.auth import HTTPBasicAuth

# using local http proxy to log requests and responses
proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "https://127.0.0.1:8888",
}

API_USER = os.environ.get('API_USER', 'admin')
API_PASS = os.environ.get('API_PASS', 'admin')

auth = HTTPBasicAuth(API_USER, API_PASS)
uri = "https://dev114955.service-now.com/incident.do?JSONv2"

# define your message
msg = "An Alert from API POST"

# define http headers for request
headers = {
    "Accept": "application/json;charset=utf-8",
    "Content-Type": "application/json"
}

# define payload for request, note we are passing the sysparm_action variable in the body of the request
# https://docs.servicenow.com/bundle/rome-application-development/page/integrate/inbound-other-web-services/concept/c_JSONv2WebService.html
payload = {
    'sysparm_action': 'insert',
    'category': 'software',
    'impact': '1',
    'urgency': '1',
    'short_description': 'new incident from Quay API POST',
    'cmdb_ci': 'Email',
    'caller_id': 'Abel Tuter',
    'description': msg
}

print("Post Content: \n" + json.dumps(payload, indent=4))

# r = requests.post(url=uri, data=json.dumps(payload), auth=auth, proxies=proxies, verify=False, headers=headers)
r = requests.post(url=uri, data=json.dumps(payload), auth=auth, headers=headers)

content = r.json()
assert (r.status_code == 200)

print("Response Status: \n" + str(r.status_code))
print("Response Content: \n" + json.dumps(content, indent=4))
