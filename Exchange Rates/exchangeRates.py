import creds
import requests

def get_euro_try_rates(first_day_formatted, last_day_formatted):
    # EVDS API endpoint
    #      https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.EUR.A.YTL&type=json&startDate=01-01-2024&endDate=01-02-2024
    url = "https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.EUR.A.YTL&type=json&startDate="+first_day_formatted+"&endDate="+last_day_formatted
    
    # Adding headers with API key
    headers = {
        'key': creds.api_key  # Adjust according to your API specification
    }
    # Sending the request to the API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # print(f"Success: {response.status_code}")
        data = response.json()['items']
        return [{'date': item['Tarih'], 'buying_rate': item['TP_DK_EUR_A_YTL']} for item in data]
    else:
        # print(f"Failed: {response.status_code}")
        return None
