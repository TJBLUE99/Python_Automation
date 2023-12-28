# import openpyxl
import os
import pandas as pd
import datetime as dt
from random import randint
path = os.getcwd()
files = os.listdir(path)

#function to generate current date
def generateCurrentDate():
        currentdate = dt.datetime.now().strftime("%d-%m-%Y");
        return currentdate

#finding xlsx files present in directory
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
if(files_xlsx):
        mergeddf = pd.DataFrame()
        for file in files_xlsx:
            data = pd.read_excel(os.path.join(path, file))
            mergeddf = pd.concat([mergeddf,data], ignore_index = True)
        print(mergeddf)
        filtered_data = mergeddf[mergeddf.eq(generateCurrentDate()).any(axis = 1)]
        print(filtered_data)
        print("Writing filtered data to new file")
        filtered_data.to_excel('result-'+ dt.datetime.now().strftime(("%Y-%m-%d")) +'-'+  str(randint(0,1000)) +'.xlsx' , index=False)
        print("File written successfully")
else: 
        print('No excel file present')
        
####################################################################################################
# df = pd.read_excel("Book2.xlsx");
# df2 = pd.read_excel("Book3.xlsx");
# print("concating the files...")
# df3 = pd.concat([df,df2]);
# print("filtering data based on current date...")
# filter_data = df3[df3.eq(generateCurrentDate()).any(axis=1)]
# print(filter_data)
# print("Writing data to excel...")
# filter_data.to_excel('final_output.xlsx', index=False);
# print("File successfull created")

######################################################################################################
# currentdate = dt.datetime.now().strftime("%d-%m-%Y")
# wb = openpyxl.load_workbook('Book2.xlsx')
# sheet = wb.active
# totalrows = sheet.max_row
# totalcolumns = sheet.max_column
#iterate through all the excel and find the record with current date
# for row in sheet.iter_rows(min_row = 1, min_col = 1, max_row=totalrows, max_col = totalcolumns):
#     for cell in row:
#         if cell.value == currentdate:
#             print(sheet.cell(row=cell.row,column=cell.column))

