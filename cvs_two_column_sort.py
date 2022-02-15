import pandas as pd
import glob
import os

directory = './women'
all_files = glob.glob(os.path.join(directory, "*.csv"))
matched_columns = ["Matched product ", "ROAS"]

def extractor(csv_sheet):
    df = pd.read_csv(csv_sheet, usecols=matched_columns)
    unique_list_value(df.values.tolist())

def unique_list_value(lst):
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    write_to_file(sorted_lst)
    
def write_to_file(keyterms):
    print(keyterms)
    file = open('keyterm.txt','a+') 
    total = 0;
    for term in keyterms:
        if(int(term[1]) > 0):
            file.write(term[0] + " || " + str(term[1]) + "\n")
            total += 1
    file.write("-------------------\n")
    file.write("Totals to: " + str(total) + " \n")
    file.write("-------------------\n")
    file.close() 


for csv_sheet in all_files:
    extractor(csv_sheet)
