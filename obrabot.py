import pandas as pd

file_path = r"... .xlsx" #путь к директории
df = pd.read_excel(file_path)

columns_to_extract = ['Id', 'Username', 'Телефон']  #искомые колонки в файлах .xlsx
extracted_columns = df[columns_to_extract]

print(extracted_columns)
extracted_columns.to_csv('1columns.csv', index=False) #выводит файл .csv с найденной информацией
