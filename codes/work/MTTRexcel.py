import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'excel.csv'     #File path to file INPUT DATA
excel_file_2 = 'second_csv'

fisrt_excel_file = pd.read_excel(excel_file_1, sheet_name='firstSheet')    #read data in to python script- creating data frame (tabular data structure which pana uses to store data)
second_excel_file = pd.read_excel(excel_file_2)     #not specifying sheet name gives default- default is to read in the first sheet
print(second_excel_file)                       #will print datastructre similar to excel spreadshet
print(second_excel_file['IP Addresses'])        #this can be used to preint single column in excell sheet
print(fisrt_excel_file.columns)                 #see all columns in workbook


#COMBINING ALL DATA
excel_all = pd.concat(excel_file_1, excel_file_2)       #this combines all excel sheets into one
print(excel_all)

#calculations

result = excel_all.groupby(['IP Address']).mean()  #this takes all data w/ group by funstion to average out the data
average = result.loc[:"IP Address":"user name"]    #this takes the average results of 2 collumns and store it in a var
print(average)

#Graphing w/ plot()

average.plot(kind='bar')  #kind is bar graph
plt.show()

#output data to new excell workbook

result.to_excel("newExcelFile.xlsx")



# More functions to use with excel
import os
import pandas as pd

excel_sheet_1 = "excel.xlxs"
excel_sheet_2 = "excel2.xlxs"

data1 = pd.read_excel(excel_sheet_1)
data2 = pd.read_excel(excel_sheet_2)

print(data1.columns)
print(data2.columns)

#pull out data from single column that are true in each file
print(data1["IP Address"].isin(data2["IP Addresses"]))                   # true or false results (if exist in both docs
similar = data1.loc[(data1["IP Address"].isin(data2["IP Addresses"]))]  #this will print out the results that are similar
print(similar)

#pull data out that is false (data that does match in both docs but is on excel.xlsx ) use a ~
similar = data1.loc[~(data1["IP Address"].isin(data2["IP Addresses"]))]
print(similar)