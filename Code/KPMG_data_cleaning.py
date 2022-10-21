import pandas as pd
import openpyxl
import matplotlib as plot
path = "..\\Data\\KPMG_VI_New_raw_data_update_final.xlsx"
NewCustomerList = pd.read_excel(path, sheet_name="NewCustomerList")
Transactions = pd.read_excel(path, sheet_name="Transactions")
CustomerDemographic = pd.read_excel(path, sheet_name="CustomerDemographic")
CustomerAddress = pd.read_excel(path, sheet_name="CustomerAddress")

# This is to check the basic info for each sheet
# print(NewCustomerList.head(5))
# print("======================")
# print(Transactions.head(5))
# print("======================")
print(CustomerDemographic.head(5))
# print("======================")
# print(CustomerAddress.head(5))

# print(NewCustomerList.info)
