import os
import pandas as pd
import math

#just a check to see if docker is running the program
print('The app has stated running... It may take up to 10 minutes to see the result ...') 

directory = './ExcelFiles/'
results = []
fields = ['Settlement Point Name', 'Settlement Point Price'] # we only care about these two fileds for now
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        excelFile = pd.ExcelFile(f) # open file
        for sheet in excelFile.sheet_names: # iterate over sheets
            dataframe = excelFile.parse(sheet, usecols = fields)
            dataframe = dataframe.dropna() # drop rows where name or price is missing
            avgPrice = dataframe[dataframe['Settlement Point Name'] == 'HB_WEST']['Settlement Point Price'].mean() # caclulate mean of price for HB_WEST
            if(not(math.isnan(avgPrice)) and avgPrice >= 100):
                month = sheet.split('_')[0] # name of sheet. Some sheets are like Dec_1 and this line would eliminate that _1 at the end
                year = filename.split('_')[1].split('.')[0] # the first split would give us year.xlsx and the second split would give us the year
                result = "{fmonth}-{fyear}:{favgPrice: .2f}".format(fmonth = month, fyear = year, favgPrice = avgPrice) # month-year:avgPrice
                results.append(result)
            
print(results)