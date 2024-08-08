import random

random_num = []
for i in range(50):
    random_num.append(random.randint(1, 100))

random_num = [random.randint(1, 100) for i in range(50)]

bigger_50 = list(filter(lambda x: x > 50, random_num))

#   50  51 52 52 54 55   [56] EOF
a = [1, 2, 3, 4, 30, 20]
filter_lazy = filter(lambda x: x > 10, a)
# filter_lazy {f-lambda, #50}
a.append(40)

# filter_lazy {f-lambda, #50}
# while filter_p != end_of_list
#    next
print(list(filter_lazy))

# filter_lazy {f-lambda, #56}
# while filter_p != end_of_list
#    next
print(list(filter_lazy))
