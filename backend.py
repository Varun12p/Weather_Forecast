import requests

API_KEY ="a33a9d30deccb330c9daf36cb23e0cb4"

def get_data(place,days=None,option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__=="__main__":
    print(get_data(place="Tokyo"))