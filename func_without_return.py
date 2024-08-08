
def my_details(line: str) -> None:
    # 0 1 2 3 4 -- len 5 // 2 == 2
    #     *
    # 0 1 2 3 -- len 4 // 2 == 2
    #   * *
    print(f"{line[0]} {line[len(line) // 2]} {line[-1]}")

def print_zugi(numbers: list[int]) -> None:
    for num in numbers:
        if num % 2 == 0:
            print("even", end=",")
        else:
            print("odd", end=",")
    print()

