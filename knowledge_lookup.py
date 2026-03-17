import requests

def check_drug_interactions(drug):

    url = f"https://api.fda.gov/drug/label.json?search={drug}"

    response = requests.get(url)

    return response.json()