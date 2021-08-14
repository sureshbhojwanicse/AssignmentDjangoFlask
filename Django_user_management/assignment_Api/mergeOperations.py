import numpy as np
import pandas as pd
import os

class DataOperations():

    def __init__(self):
        import os
        import pandas as pd
        from functools import reduce
        self.os     = os
        self.pd     = pd
        self.reduce = reduce

    def addData(self, file_path):
        file_name = file_path.split('/')[-1].split('.')[0]
        if file_name=='Customer':
            exist_file = self.pd.read_excel('Customer.xlsx')
            new_file = self.pd.read_excel(file_path)
            updated_file = self.pd.concat([exist_file, new_file], axis=0, ignore_index=True)
            updated_file.to_excel('Customer.xlsx', index=False)
        elif file_name=='Loan_Amount_Data':
            exist_file = self.pd.read_excel('Loan_Amount_Data.xlsx')
            new_file = self.pd.read_excel(file_path)
            updated_file = self.pd.concat([exist_file, new_file], axis=0, ignore_index=True)
            updated_file.to_excel('Loan_Amount_Data.xlsx', index=False)
        elif file_name=='Customer_Office_Data':
            exist_file = self.pd.read_excel('Customer_Office_Data.xlsx')
            new_file = self.pd.read_excel(file_path)
            updated_file = self.pd.concat([exist_file, new_file], axis=0, ignore_index=True)
            updated_file.to_excel('Customer_Office_Data.xlsx', index=False)
        elif file_name=='Customer_Home_Address_Data':
            exist_file = self.pd.read_excel('Customer_Home_Address_Data.xlsx')
            new_file = self.pd.read_excel(file_path)
            updated_file = self.pd.concat([exist_file, new_file], axis=0, ignore_index=True)
            updated_file.to_excel('Customer_Home_Address_Data.xlsx', index=False)
        elif file_name=='Branch_Data':
            exist_file = self.pd.read_excel('Branch_Data.xlsx')
            new_file = self.pd.read_excel(file_path)
            updated_file = self.pd.concat([exist_file, new_file], axis=0, ignore_index=True)
            updated_file.to_excel('Branch_Data.xlsx', index=False)

    def joinData(self, folder_path="/home/ubuntu/new/Django_user_management/assignment_Api/", matching_column_name="Customer Id"):
        all_dataframes = []

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files)
        for file_name in files:
            
            if file_name.split(".")[-1]=='xlsx':
                print(file_name.split(".")[-1])
                print(file_name)
                df = self.pd.read_excel(file_name)
                all_dataframes.append(df)
                df_merged = self.reduce(lambda  left,right: self.pd.merge(left,right,on=[matching_column_name],how='outer'), all_dataframes).fillna(0)
                 
        return df_merged