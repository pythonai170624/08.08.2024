
# for i in range(10):
#     print(i)

result = []
for i in range(1, 11):
    if i % 3 != 0:
        result.append(i)
print(result)

# comp = [what-to-add? for-loop [<if> condition]]
result = [i for i in range(1, 11) if i % 3 != 0]
print('result', result)

# comp    = [what-to-add? for-loop [<if> condition]]
list_comp = [i for i in range(10)]
print('list_comp', list_comp)
print('list_comp one-line', [i for i in range(10)])
print('list_comp conditions', [i for i in range(10) if i % 3 == 0])

# lambda
start_list_comp = [i for i in range(10)]
filtered = list(filter(lambda x: x % 3 == 0, start_list_comp))
print(filtered)
#mapped = filter(list(map(lambda x: x ** 2, start_list_comp)))
#print(mapped)
def ribua(x) -> int:
    return x ** 2
print('list_comp one-line', [i for i in range(10)])
print('list_comp one-line', [ribua(i) for i in range(10)])
# print('list_comp one-line', [(lambda x: x ** 2)(i) for i in range(10)])

cities_in_japan = [
    "Tokyo",
    "Yokohama",
    "Osaka",
    "Nagoya",
    "Sapporo",
    "Kyoto",
    "Fukuoka",
    "Kobe",
    "Kawasaki",
    "Saitama"]

result = []
for city in cities_in_japan:
    result.append(city[0])
print(result)
#             [append | for loop                  | if ...]
result_comp = [city[0] for city in cities_in_japan if city[0].lower() != 'S']
print('result_comp', result_comp)
