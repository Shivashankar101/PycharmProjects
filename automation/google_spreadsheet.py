import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheet.google.com/feeds"]


creds = ServiceAccountCredentials.from_json_keyfile_name('My Project Automation-aee13e76bf37.json', scope)
client = gspread.authorize(creds)

my_sheet = client.open('login_data').sheet1

data_on_sheet = my_sheet.get_all_values()

print(data_on_sheet)
