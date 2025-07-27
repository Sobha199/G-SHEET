import gspread

gc = gspread.service_account(filename="service_account.json")
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1265kUfjiWYuh5fsSwbU5HdA7soyn6qcfRc-4xAozbjk/edit")
worksheet = sh.sheet1
print(worksheet.get_all_records())
