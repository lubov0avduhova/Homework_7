import pandas
from tkinter.filedialog import askdirectory



def import_file_xlsx():
    file_path = askdirectory()
    return pandas.read_excel(file_path) 

def export_file_xlsx(file):
    return file.to_excel('New_DataBase.xlsx', index = False)

def import_file_csv():
    file_path = askdirectory()
    return pandas.read_csv(file_path)

def export_file_csv(file):
    return file.to_csv('New_DataBase.csv', index = False)
