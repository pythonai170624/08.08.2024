import funcs
import random

random.randint(40, 70)

# def mul(a: int = 1, b: int = 1) -> int:
#     return a * b
#
# print(mul(10))
#
# funcs.foo()

def add(x: int, y: int) -> int:
    return x + y

def min(x: int, y: int) -> int:
    return x - y

def mul(x: int, y: int) -> int:
    return x * y

def div(x: int, y: int) -> int:
    return x / y

print(add(8, 9))
add_result = add(8, 9)  # 17
print(min(8, 9))
min_result = min(8, 9)  # -1

my_list = [1, 2]
my_list_rev = [my_list[1], my_list[0]]

print(my_list_rev)
temp = my_list[0]
my_list[0] = my_list[1]
my_list[1] = temp
print(my_list)

a = 1
b = 2
a, b = b, a  # [b, a]
print(a, b)
c, d = [8, 9]
print(c, d)

dictionary = {'name': 'Israel', 'pop': 9.3}
print(dictionary.items())

list1 = [('name', 'Israel'), ('pop', 9.3)]
for k, v in list1:
    print(k, '=', v)

for i in [1,2,3,4,5]:
    print(i, end=",")

for i, j, z in [[1, 2, 3], [3, 4, 6], [5, 6, 7]]:
    print(i, j, z)
for i in [[1, 2], [3, 4], [5, 6]]:
    print(i)

my_list: list[int] = [1, 2, 3, 40, 50]
filter(lambda x: x > 8, my_list)

my_list = [10, 20, 30, 40, 50]
#print(my_list.pop(0))
#x = my_list.pop(0)
#del my_list[0]
#print(my_list.remove(10))
x = my_list.remove(10)
print(x)
print(my_list)

item_array = ["apple", "banana", "cherry", "date", "elderberry"]
item_array.append("grapes")
item_array.append("mango")
item_array.sort()
item_array.sort(reverse=True)

number_array = [10, 25, 30, 45, 50]
for i in range(len(number_array)):
    print(f"{i} = {number_array[i]}")

for i, num in enumerate(number_array):
    print(f"{i} = {num}")

print(list(enumerate(number_array)))

number_array = [12, 25, 30, 40, 50]
def divide_by_4(x: int) -> bool:
    if x % 4 == 0:
        return True
    else:
        return False

print(list(filter(divide_by_4, number_array)))
print(list(filter(lambda numx: numx % 4 == 0, number_array)))
print(list(filter(lambda numx: not numx % 4, number_array)))

from datetime import datetime, timedelta
print(datetime.now())
print((datetime.now() + timedelta(days=1)).strftime("%H:%M:%S.%f %Y-%m-%d "))
print((datetime.now() + timedelta(days=1)).strftime("%H:%M:%S.%f [DAY] %Y-%B-%d "))

try:
    raise Exception("wrong password")
except:
    print('---wrong password---')

a = [1, 2, 3]
print(a[4])

try:
    print(a[4])
except:
    print('saved by the try-except')

print('continue...')

