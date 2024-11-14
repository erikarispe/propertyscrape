#You must copy this code and save it to a file with a .py extension
#you will change the property_id value to the account number you want to scrape



import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL of the page to scrape
property_id = '00000602857000000'
url = f'https://www.dallascad.org/AcctDetailCom.aspx?ID={property_id}#Legal'

# Perform a GET request to fetch the HTML content
page = requests.get(url)

# Check if the request was successful
if page.status_code != 200:
    print(f"Failed to retrieve webpage: {page.status_code}")
else:
    # Parse the HTML content
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract required data
    address = soup.find('span', id='PropAddr1_lblPropAddr')
    address_found = address.text.strip() if address else "Address not found"

    deed_transfer_date = soup.find('span', id='LegalDesc1_lblSaleDate')
    deed_transfer_date_found = deed_transfer_date.text.strip() if deed_transfer_date else "Deed transfer date not found"

    owner_section = soup.find('span', id='lblOwner')
    owner_found = owner_section.next_sibling.strip() if owner_section else "Owner not found"

    # Extract Total Area
    total_area_display = "Total area not found"
    
    # Locate the improvements table
    improvements_table = soup.find('span', string=lambda t: t and 'Improvements (Current 2025)' in t).find_next('table')

    if improvements_table:
        # Locating the row containing the "Total Area" data
        for row in improvements_table.find_all('tr'):
            if 'Total Area:' in row.text:
                total_area_display = row.find_all('td')[1].text.strip()  # Get the relevant cell
                break

    # Extract zoning from the "Land" section
    zoning_found = "Zoning info not found"
    land_table = soup.find('table', id='Land1_dgLand')
    if land_table:
        zoning_row = land_table.find_all('tr')
        if len(zoning_row) > 1:
            zoning_cell = zoning_row[1].find_all('td')[2]
            zoning_found = zoning_cell.text.strip() if zoning_cell else zoning_found

    # Extract land area
    land_area_span = soup.find('span', id='Land1_dgLand__ctl2_Label1')
    land_area_found = land_area_span.text.strip() if land_area_span else "Land area not found"

    # Prepare data to append to Excel
    data = {
        'Address': [address_found],
        'Deed Transfer Date': [deed_transfer_date_found],
        'Owner': [owner_found],
        'Total Area': [total_area_display],
        'Zoning': [zoning_found],
        'Land Area': [land_area_found]
    }

    # Define the Excel file name
    excel_file = 'property_data.xlsx'

    # Check if the file exists
    if os.path.exists(excel_file):
        # Load the existing Excel file and append the new data to it
        df_existing = pd.read_excel(excel_file)
        df_new = pd.DataFrame(data)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(excel_file, index=False)
    else:
        # Create a new Excel file with headers
        df_new = pd.DataFrame(data)
        df_new.to_excel(excel_file, index=False)

    print("Data has been written to Excel successfully.")
