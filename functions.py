ages = [6, 18, 12, 45, 3, 65, 13, 36, 5, 87]

def say_helo():
    print('čau!')

def say_my_age():
    print(f'Man ir {age} gadi')

def is_age_legal(age):
    if age < 18:
        return False
    else:
        return True

for age in ages:
    if is_age_legal(age) == True:
        print(f'{age} is legal')
    else:
        print(f'{age} is non-legal')


#for age in ages:
    #if age >= 18:
     #   print(f'{age} is legal')
    #else:
   #     print(f'{age} is not legal')

#for age in ages:
   # if is_age_legal(age) == 'Yes':
    #    print(f'{age} is legal')
   # else:
    #    print(f'{age} is non-legal')



#for age in ages:
 #   if is_age_legal(age) == 'Yes':
#        print(f'{age} is legal')
 #   else:
 #       print(f'{age} is non-legal')