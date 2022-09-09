import pandas as pd


file_name = 'zips/MetroManilaZipCodes.xlsx'



print('''
      Search function: 
      
      (1) City
      (2) Barangay
      ''')

userMenu = input('Select: ')



df = pd.read_excel(io=file_name, sheet_name='MM')
df['ZIP Code'] = df['ZIP Code'].astype(int)

if userMenu == '1':
    cityPick = input('Input City: ')
    df = df[df['City'].str.contains(cityPick, na=False, case=False)]
    print(df)
elif userMenu == '2':
    brgyPick = input('Input Barangay: ')
    df = df[df['Barangay'].str.contains(brgyPick, na=False, case=False)]
    print(df)