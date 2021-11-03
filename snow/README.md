# Service Now

The following is a sample script for creating a ServiceNow incident using a HTTP POST

You can create a quay POST using the output from the script

## Quickstart
```
python3 -m venv venv
. venv/bin/activate

pip install -r requirements.txt

export API_USER=< SNOW username >
export API_PASS=< SNOW password >

python create_incident.py
```

## Links
- [Developer Resources - Service Now](https://developer.servicenow.com/dev.do)
