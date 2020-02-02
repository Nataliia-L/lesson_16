# Попросите пользователя ввести имя файла. 
# Поддерживаемые расширения - txt, log, py. 
# Если введено неподдерживаемое расширение, кидать исключение. 
# Если введенный файл не существует, кидать исключение. Подсчитать количество слов в файле.

import os
def verify_file ():
    global file_name
    file_name = input ('Please, enter name: ')
    if file_name.endswith ('.txt'):
        print ('Great! The file_name is: ', file_name)
    elif file_name.endswith ('.log'):
        print ('Great! The file_name is: ', file_name)
    elif file_name.endswith ('.py'):
        print ('Great! The file_name is: ', file_name)
    else:
        raise Exception ('Sorry! The name is incorect.')
    
    ex = os.path.exists (file_name)
    if ex==False:
        raise Exception ('Sorry! Your file does not exist!')
        print ('Congrats! Your file exists!')
    else:
        print ('Congrats! Your file exists!')
    
def calc_words ():
    verify_file ()
    print ('The number of words in the file name: ', len (file_name.split('.')))


calc_words ()
