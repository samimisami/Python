import creds
import requests
from datetime import datetime, timedelta

def get_euro_try_rate_daily(day):
    #      https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.EUR.A.YTL&type=json&startDate=01-01-2024&endDate=01-02-2024
    url = "https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.EUR.A.YTL&type=json&startDate="+day+"&endDate="+day

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
        rate_check = data[0]['TP_DK_EUR_A_YTL']
        if rate_check==None:
            initial_date = datetime.strptime(day, "%d-%m-%Y")
            date_a_day_before = initial_date - timedelta(days=1)
            date_a_day_before_str = date_a_day_before.strftime("%d-%m-%Y")
            return get_euro_try_rate_daily(date_a_day_before_str)
        else:
            return rate_check
    else:
        # print(f"Failed: {response.status_code}")
        return None

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
        rate_check = data[0]['TP_DK_EUR_A_YTL']
        if rate_check==None:
            date_initial = datetime.strptime(data[0]['Tarih'], "%d-%m-%Y")
            date_day_before = date_initial - timedelta(days=1)
            date_day_before_str = date_day_before.strftime("%d-%m-%Y")
            data[0]['TP_DK_EUR_A_YTL']=get_euro_try_rate_daily(date_day_before_str)
        else:
            pass # do nothing
        dataset = [{'date': item['Tarih'], 'buying_rate': item['TP_DK_EUR_A_YTL']} for item in data]
        return dataset
    else:
        print(f"Failed: {response.status_code}")
        return None
