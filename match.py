import os
import csv
import fnmatch 
from shutil import copyfile
#В файле database.csv есть 4 колонки(ниже)
#объявление переменных
decoded_course_name='decoded_course_name'
decoded_univer_name='decoded_univer_name'
encoded_univer_name='encoded_univer_name'
encoded_course_name='encoded_course_name' 
result_dir='result/'
data_dir='data/'

#Функция нахождения файла в папке
def find(pattern, path):
    result = ''
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result+=os.path.join(root, name)
				
    return result         

#Находит файл, переводит его имя в нормальный вид
def csv_dict_reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		#!!!Обязательно _ для однозначного декодирования
		line_to_find='*'+line[encoded_univer_name]+'*'+line[encoded_course_name]+'_*.csv'
		line_to_replace=result_dir+line[decoded_univer_name]+' '+line[decoded_course_name]+'.csv'
        
		found_line=find(line_to_find,os.getcwd()+'/'+data_dir)
		if os.path.exists(found_line):
			print(found_line+'\n')
			copyfile(found_line,line_to_replace)
		found_line=""
		line_to_find=""
#main
if not os.path.exists(result_dir):
	os.mkdir(result_dir)
with open("database.csv") as f_obj:
	csv_dict_reader(f_obj)
