import pandas as pd

print('''
_____  _    _ ___________ _____  
|  __ \| |  | |___  /_   _|  __ \ 
| |__) | |__| |  / /  | | | |__) |
|  ___/|  __  | / /   | | |  ___/ 
| |    | |  | |/ /__ _| |_| |     
|_|    |_|  |_/_____|_____|_|     

Search for City / Barangay Zip codes
Note: Only Metro Manila is implemented''')


def make_line():
    print('=' * 80)
    
    
def showUserMenu():
    make_line()
    print(f'''Search function: 
        (1) City
        (2) Barangay''')
    make_line()


def searchFor(df):
    userMenu = input('Select: ')
    if userMenu == '1': # Search for City list zip codes
        cityPick = input('Input City: ')
        df = df[df['City'].str.contains(cityPick, na=False, case=False)]
        make_line()
        print(df)
        make_line()
    elif userMenu == '2': # Search for Barangay / District direct zip codes
        brgyPick = input('Input Barangay: ')
        df = df[df['Barangay'].str.contains(brgyPick, na=False, case=False)]
        make_line()
        print(df)
        make_line()
        
        
file_name = 'zips/MetroManilaZipCodes.xlsx'
df = pd.read_excel(io=file_name, sheet_name='MM')
df['ZIP Code'] = df['ZIP Code'].astype(int)
        
showUserMenu()
searchFor(df)