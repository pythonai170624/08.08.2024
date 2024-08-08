import func_with_return as fwr

head1: str = fwr.my_headline("python has concurred the world")
print(head1)

res_con: list[int] = fwr.concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(res_con)
print('len', len(res_con))

help(fwr.concat_list)