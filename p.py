# number=[print(i,j) for i in  range(5) for j in range(3)]
# print(number)


# Mypy هو مدقق اختياري من النوع الثابت لبايثون يهدف إلى الجمع بين مزايا الكتابة الديناميكية (أو "البط") والكتابة الثابتة
# Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or 'duck') typing and static typing



# from unittest import result


# def mysum(x:int,y:int) ->int:
#     result= x+y
#     return result

# v = mysum(10,12)
# print(v)    #run for labriry mypy


# from turtle import title


# names = ["moahmed", "ali", "mahmoud","salam"]
# new_names=[]

# for name in names:
#     new_names.append(name.title())

# print(new_names)

# وتكون فاضية list يقوم بالطباعة قبل ال for قبل  print عند عمل   
# number=[(i,j) for i in range(5) for j in range(3)]
# print(number)


#even number
# even =[i for i in range(1,101) if i%2==0]
# print(even)


#if with else 
# even =[i if i%2==0 else 0 for i in range(1,101)]
# print(even)

'''
-Loop
    -Fast
    -pythonic


-list comperhension
    -pythonic
    -easy to undrestand
    -takes time load

'''

# لمعرفة في اي لفه يتم التنفيذ
'''
names=["mohamed", "ali", "mahmoud", "ahmed"]
for index, name in enumerate(names,start=1):#لجعلها تبداء من 1 
    if index ==2:#لجعل كل 2 مع بعض 
        print("--------")
    print(f"{index}:{name}")
'''

'''
#functools
    3 things important
        1- map
        2- filter
        3- reduc
'''

#Using map 
'''
names = ["moahmed", "ali", "mahmoud","ahmed"]

def mytitle(x):
    return x.title()

new_names = map(mytitle,names)
new_names2=map(lambda x:x.title(),names) #للتعامل مع دالة بسيطه

print(list(new_names2))
print(list(new_names))# listنقوم باعدتها الى 
'''



#using filter
'''
number=[20,100,80,25,12,18]

def bigger(x):
    if x>50:
        return True
    else:
        return False
my_number = filter(bigger,number)
print(list(my_number))
'''
'''
#using reduc

from functools import reduce

number=[20,100,25,80,18,12]
def mysum(x,y):
    return x+y

resulte=reduce(mysum,number)
print(resulte)

'''
'''
#لمعرفة طريقة عمل الدالة 
import functools

print(dir(functools))
'''
def mysum(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def minus(x,y):
    print(x-y)

def main():
    print('''
            Welcome  in our game
            choose game number:
                1 : sum
                2 : mul
                3 : minus
    ''')
    user_choice = int(input('Enter Your Number: '))
    if user_choice ==1:
            x=int(input('Enter Your Number: '))
            y=int(input('Enter Your Number: '))
            mysum(x,y)
    elif user_choice == 2:
        x=int(input('Enter Your Number: '))
        y=int(input('Enter Your Number: '))
        mul(x,y)
    elif user_choice==3:
        x=int(input('Eenter Your Number: '))
        y=int(input('Eenter Your Number: '))
        minus(x,y)
if __name__ == "__main__":
    main()