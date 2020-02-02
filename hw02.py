#Просить пользователя ввести данные о себе - имя, дату рождения, профессию. 
#При вводе имени, проверять, что введено имя и фамилия, через пробел. 
#Если нет, кидать исключение с нужным текстом. 
#При вводе даты рождения, просить вводить по отдельности - год, месяц и число. 
#Если при вводе какого-то параметра введены символы, отличные от цифр, кидать исключение с нужным текстом. 
#Если год больше 2000 - кидать ошибку. 
#Если месяц больше 12, кидать ошибку. Если число больше 31, кидать ошибку.
#Сохранять данные в файл с названием {name}.txt, в формате : {name};{bith date};{profession}\n 


name = input ('Please, enter your full name: ')
num_words = len (name.split (' '))
if num_words != 2:
    raise Exception ('Please, enter correct name!')
else:
    print ('Hello, ', name.title())
    
    
date_of_birth = input ('Please, enter the date of birth: ')
if date_of_birth.isdecimal ()==False:
    raise Exception ('Please, enter correct date of birth!')
if int(date_of_birth) > 31:
     raise Exception ('The date of birthday is more than 31')

month_of_birth = input ('Please, enter the month of birth: ')
if month_of_birth.isdecimal ()==False:
    raise Exception ('Please, enter correct month of birth!')
if int(month_of_birth) > 12:
     raise Exception ('The month of birthday is more than 12')

year_of_birth = input ('Please, enter the year of birth: ')
if year_of_birth.isdecimal ()==False:
    raise Exception ('Please, enter correct year of birth!')
if int(year_of_birth) > 2000:
    raise Exception ('The year of birthday is more than 2000')

birthday = date_of_birth, month_of_birth, year_of_birth
data = ('.'.join (birthday))
print ('Your birthday is: ', data)

profession = input ('Please, enter your profession: ')
print ('Your profession is: ', profession)

line ={'name': name, 'data': data, 'profession': profession}
print ('Text in file: ', line)

f = open ('info.txt', 'w')
f.write (str(line) + '\n')
f.close ()
