from fileinput import filename
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

Search for City / Barangay Zip codes''')


def make_line(): # Makes it pretty
    print('=' * 80)
    
    
def showUserMenu(): # Shows selection of city or barangay
    make_line()
    print(f'''Search function: 
        (1) City
        (2) Barangay''')
    make_line()


def searchFor(df, userAnswer): # Search # UserAnswer 1 = Metro Manila, 2 = Province
    
    while True:
        try:
            userMenu = int(input('Select: '))
            if userMenu == 1 or userMenu ==2:
                break
            else:
                print("Not a valid number, please try again")
        except ValueError:
            print("Not a valid answer, please try again")
    
    while True:
        try:
            if userAnswer == 1:
                col1Name = 'City'
                break
            else:
                col1Name = 'Province'
                break
        except ValueError:
            print("ValueError")
            
    if userMenu == 1: # Search for City list zip codes
        cityPick = input('Input City: ')
        df = df[df[col1Name].str.contains(cityPick, na=False, case=False)] # na=False removes blank passages in the file if any
        make_line()
        if df.empty:
            print("No results to show based on your search.")
        else: 
            print(df)
            outputFile(df)
        make_line()
    elif userMenu == 2: # Search for Barangay / District direct zip codes
        brgyPick = input('Input Barangay: ')
        df = df[df['Barangay'].str.contains(brgyPick, na=False, case=False)] # na=False removes blank passages in the file if any
        make_line()
        if df.empty:
            print("No results to show based on your search.")
        else: 
            print(df)
            outputFile(df)
        make_line()

def outputFile(df):
    """
    Output file to excel funciton
    
    Args:
        df (_type_): Valid Pandas dataframe
    """
    while True:
        askOutput = input('Do you want to output results as .xlsx? (y/n)')

        if askOutput.lower() == 'y':
            while True:
                fileName = input("Enter the file name: ")
                if fileName == '':
                    print("You have to enter something.")
                else:
                    break

            df.to_excel(f'{fileName}.xlsx', index=False)
            print(f"Saved as {fileName} successful")
            
            break
        elif askOutput.lower() == 'n':
            break
        else:
            print("Please give a valid answer.")

        
while True:
    make_line()
    print(f'''Choose Type:
            (1) Metro Manila
            (2) Regional
            ''')
    userAnswer = 0
    
    while userAnswer != 1 or userAnswer != 2:
        try:
            userAnswer = int(input('Answer: '))
            if userAnswer == 1 or userAnswer == 2:
               break
            else:
                print("Please select within the range of the menu")
        except ValueError:
            print("That is not a valid answer, try again")
        
   
    if userAnswer == 1:
        file_name = 'zips/MetroManilaZipCodes.xlsx'
        df = pd.read_excel(io=file_name, sheet_name='MM',) 
        df['ZIP Code'] = df['ZIP Code'].astype(int) # Converts excel values to INT for the zip code column
        # Remove blank rows1
        df['ZIP Code'].replace('', np.nan, inplace=True)
        df['City'].replace('', np.nan, inplace=True)
        df['Barangay'].replace('', np.nan, inplace=True)
        df.dropna(inplace=True)
    else:
        file_name = 'zips/provinceZip.xlsx'
        df = pd.read_excel(io=file_name)    
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