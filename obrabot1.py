import pandas as pd
import os

directory_path = r'...' #путь к директории

columns_to_extract = ['Id', 'Username', 'Телефон']  #искомые колонки в файлах .xlsx
all_extracted_data = pd.DataFrame()

for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):  
        file_path = os.path.join(directory_path, filename)
        
        try:
            df = pd.read_excel(file_path, engine='openpyxl' if filename.endswith('.xlsx') else 'xlrd')
        except Exception as e:
            print(f"erorr {filename}: {e}")
            continue
        
        df.columns = df.columns.str.strip()
        
        missing_columns = [col for col in columns_to_extract if col not in df.columns]
        if missing_columns:
            print(f"in {filename} erorr: {missing_columns}")
        else:
            extracted_columns = df[columns_to_extract]
            
            all_extracted_data = pd.concat([all_extracted_data, extracted_columns], ignore_index=True)

all_extracted_data.to_csv('allcolumns1.csv', index=False)
print("all in 'allcolumns1.csv'") #выводит файл .csv с найденной информацией 
