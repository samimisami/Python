import requests
import certifi
from bs4 import BeautifulSoup
import pandas as pd

# URL of the exchange rate page
url = "https://www.scrapethissite.com/pages/forms/"

# Send a GET request to the URL
#response = requests.get(url, verify=certifi.where())
response = requests.get(url, verify=False)
response.raise_for_status()  # Raise an error if the request failed

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the exchange rate data
table = soup.find("table", {"class": "table"})

# Extract the header row to identify the columns
headers = []
for th in table.find("tr").find_all("th"):
    headers.append(th.text.strip())

# Extract the data rows
rows = []
for tr in table.find_all("tr"):
    cells = tr.find_all("td")
    if cells:  # Ensure the row is not empty
        row = [cell.text.strip() for cell in cells]
        rows.append(row)

# Print the extracted data
print(f"{' | '.join(headers)}")
print('-' * 50)

for row in rows:
    print(f"{' | '.join(row)}")

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to an Excel file
output_file = "output_scrape_data.xlsx"
df.to_excel(output_file, index=False)
