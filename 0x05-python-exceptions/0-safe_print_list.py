#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements in a list
    """
    items = 0

    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except IndexError:
            break
        else:
            items += 1
    print()
    return (items)
