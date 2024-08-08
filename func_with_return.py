def my_headline(line: str) -> str:
    result: str = line.upper() + "!"
    return result

def concat_list2(nested_list: list[list[int]]) -> list[int]:
    # [ [1,2,3], [4, 5] ]
    result: []
    for inner_list in nested_list:
        result.extend(inner_list)  # [1,2,3,4,5]
    return result


def concat_list(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    """
    Concatenate three lists into one.

    This function makes 1 long int list out of 3 int lists

    :parameter
    list1 (list[int]): the first list
    list2 (list[int]): the second list
    list3 (list[int]): the third list

    :returns
    list[int]: concatenated list
    """
    [ [1,2,3], [4, 5]]

    #result = list1 + list2 + list3
    result: list[int] = list1.copy()
    result.extend(list2)
    result.extend(list3)
    return result

