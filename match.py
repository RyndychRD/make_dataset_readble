import os
import csv
import fnmatch 
from shutil import copyfile

decoded_course_name='decoded_course_name'
decoded_univer_name='decoded_univer_name'
encoded_univer_name='encoded_univer_name'
encoded_course_name='encoded_course_name' 
result_dir='result/'
data_dir='data/'

def find(pattern, path):
    result = ''
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result+=os.path.join(root, name)
    return result         

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        line_to_find='*'+line[encoded_univer_name]+'*'+line[encoded_course_name]+'*.csv'
        
        line_to_replace=result_dir+line[decoded_univer_name]+' '+line[decoded_course_name]+'.csv'
        
        found_line=find(line_to_find,os.getcwd()+'/'+data_dir)
        print(found_line)
        if  os.path.exists(found_line):
            copyfile(found_line,line_to_replace)
            with open(line_to_replace,'rb') as F:
                text=F.read()
                text=text.decode("cp1251")
                text = text.encode("ascii","ignore")
                   
        
#main
if not os.path.exists(result_dir):
            os.mkdir(result_dir)
with open("database.csv") as f_obj:
    csv_dict_reader(f_obj)
