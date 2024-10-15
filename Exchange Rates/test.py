import creds
from datetime import datetime, timedelta
import requests
import pandas as pd

def getDates():
    # Get current date
    # today = datetime(2024, 3, 1)
    today = datetime.today()

    # Calculate the first day of the current month
    first_day_of_this_month = today.replace(day=1)

    # Calculate the last and first day of the previous month
    last_day_of_last_month = first_day_of_this_month - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)

    # Store formatted dates in variables
    firstDay = first_day_of_last_month.strftime("%d-%m-%Y")
    lastDay = last_day_of_last_month.strftime("%d-%m-%Y")
    firstDayName = first_day_of_last_month.strftime("%Y-%m-%d")
    """
    print("First day of last month:", today)
    print("First day of last month:", today.strftime("%d-%m-%Y"))
    print("First day of last month:", firstDay)
    print("Last day of last month:", lastDay)
    """
    return firstDay, lastDay, firstDayName

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

def extraction2excel(dataset, extraction_name):
    if dataset:
        df = pd.DataFrame(dataset)
        # print(df)
        
        df['buying_rate'].ffill(inplace=True)

        # Save to Excel
        df.to_excel(extraction_name+'_EUR-TRY.xlsx', index=False)



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
            previous_date_str = date_a_day_before.strftime("%d-%m-%Y")
            print(previous_date_str)
            return get_euro_try_rate_daily(previous_date_str)
            print('test_pozitif')
        else:
            print('test_negatif')
            return rate_check
    else:
        # print(f"Failed: {response.status_code}")
        return None
    
def get_euro_try_rates_test(first_day_formatted, last_day_formatted):
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
        print(rate_check)
        if rate_check==None:
            initial_date = datetime.strptime(data[0]['Tarih'], "%d-%m-%Y")
            date_obj = initial_date - timedelta(days=1)
            previous_date_str = date_obj.strftime("%d-%m-%Y")
            print(previous_date_str)
            data[0]['TP_DK_EUR_A_YTL']=get_euro_try_rate_daily(previous_date_str)
            print('test_pozitif')
        else:
            print('test_negatif')
        dataset = [{'date': item['Tarih'], 'buying_rate': item['TP_DK_EUR_A_YTL']} for item in data]
        print(dataset)
        return dataset

    else:
        print(f"Failed: {response.status_code}")
        return None

first_day, last_day, first_day_name=getDates()

dataset = get_euro_try_rates_test("01-01-2023", "09-10-2024")

if dataset:
    df = pd.DataFrame(dataset)
    print(df)
            
    df['buying_rate'].ffill(inplace=True)

        # Save to Excel
    df.to_excel('TEST'+'_EUR-TRY.xlsx', index=False)
