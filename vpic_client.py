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