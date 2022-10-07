import requests
import json

def get_vin_record(vin):
    resp = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/decodevinextended/" + vin + "?format=json")
    data = json.loads(resp.text)

    retval = ""
    for r in data["Results"]:
        if r['VariableId'] == 26:
            retval = r['Value']
    return retval

def random_api():
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = json.loads(resp.text)

    return data["userId"]