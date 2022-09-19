from operator import truediv
import pandas as pd
import numpy as np
import sys

print('''
_____  _    _ ___________ _____  
|  __ \| |  | |___  /_   _|  __ \ 
| |__) | |__| |  / /  | | | |__) |
|  ___/|  __  | / /   | | |  ___/ 
| |    | |  | |/ /__ _| |_| |     
|_|    |_|  |_/_____|_____|_|     

Search for City / Barangay Zip codes
Note: Only Metro Manila is implemented''')


def make_line(): # Makes it pretty
    print('=' * 80)
    
    
def showUserMenu(): # Shows selection of city or barangay
    make_line()
    print(f'''Search function: 
        (1) City
        (2) Barangay''')
    make_line()


def searchFor(df, userAnswer): # Search # UserAnswer 1 = Metro Manila, 2 = Province
    userMenu = input('Select: ')
    if userAnswer == '1':
        col1Name = 'City'
    else:
        col1Name = 'Province'
    if userMenu == '1': # Search for City list zip codes
        cityPick = input('Input City: ')
        df = df[df[col1Name].str.contains(cityPick, na=False, case=False)] # na=False removes blank passages in the file if any
        make_line()
        if df.empty:
            print("No results to show based on your search.")
        else: 
            print(df)
        make_line()
    elif userMenu == '2': # Search for Barangay / District direct zip codes
        brgyPick = input('Input Barangay: ')
        df = df[df['Barangay'].str.contains(brgyPick, na=False, case=False)] # na=False removes blank passages in the file if any
        make_line()
        if df.empty:
            print("No results to show based on your search.")
        else: 
            print(df)
        make_line()
        
while True:
    make_line()
    print(f'''Choose Type:
            (1) Metro Manila
            (2) Regional
            ''')
    userAnswer = input('Answer: ')
    if userAnswer == '1':
        file_name = 'zips/MetroManilaZipCodes.xlsx'
        df = pd.read_excel(io=file_name, sheet_name='MM',) # Currently only reads the sheet 'MM' - Metro Manila
        df['ZIP Code'] = df['ZIP Code'].astype(int) # Converts excel values to INT for the zip code column
        # Remove blank rows1
        df['ZIP Code'].replace('', np.nan, inplace=True)
        df['City'].replace('', np.nan, inplace=True)
        df['Barangay'].replace('', np.nan, inplace=True)
        df.dropna(inplace=True)
    else:
        file_name = 'zips/provinceZip.xlsx'
        df = pd.read_excel(io=file_name) # Currently only reads the sheet 'MM' - Metro Manila    
        # Remove blank rows
        df['ZIP Code'].replace('', np.nan, inplace=True)
        df['Province'].replace('', np.nan, inplace=True)
        df['Barangay'].replace('', np.nan, inplace=True)
        df.dropna(inplace=True)
        df['ZIP Code'] = df['ZIP Code'].astype(int) # Converts excel values to INT for the zip code column

    showUserMenu()
    searchFor(df, userAnswer)
    make_line()
    endProgram = input("End program?(y/n) ")
    if endProgram == 'y':
        sys.exit()