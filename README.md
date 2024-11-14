# propertyscrape

Download Python: 

Go to the official Python website: python.org.
Download the latest version of Python compatible with your operating system (Windows, macOS, Linux).
Make sure to check the box that says "Add Python to PATH" during installation.
Verify Installation:

Open a command prompt (Windows) or terminal (macOS/Linux).
Type python --version on windows, python3 --version on mac and press Enter. You should see the Python version installed if successful.

Step 2: Install Required Libraries
Open Terminal or Command Prompt:

For Windows, you can search for cmd in the Start menu.
For macOS, use Terminal from Launchpad.
For Linux, use your preferred terminal application.
Install the Libraries:

Type the following command and press Enter:
pip install requests beautifulsoup4 pandas openpyxl

Step 3: Prepare the Python Script
Create a New Python File:

Open a text editor (like Notepad on Windows, TextEdit on macOS, or any code editor such as VS Code).
Copy the Python script provided in the pythonscrapebyaccountnumber file
Paste and Save the Script with a .py extension

for example, property_scraper.py. 
Make sure you remember the location where you saved the file.

Edit the Property ID:

Within the code, modify the value of property_id with the ID of the property you want to scrape, e.g.: property_id = '00000602857000000'  # Replace this with the desired property ID

Run the Script:

Type the following command depending if you are windows or mac and press Enter:
python property_scraper.py    (windows)
python3 property_scraper.py    (mac)


Check for Output:

If the script runs successfully, it will scrape the data and create or update an Excel file named property_data.xlsx in the same directory as your script.
You might see a message saying "Data has been written to Excel successfully."

Step 5: Open the Excel File
Open Excel:
Locate the property_data.xlsx file in the directory where your script is saved.
Open the file using Microsoft Excel, Google Sheets, or any compatible software to view your scraped data.

Each time you run the script, it will add the new scraped data to the excel file. 

