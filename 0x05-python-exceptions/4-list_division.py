#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element in 2 lists
    """
    result_arr = []
    for j in range(list_length):
        try:
            result = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_arr.append(result)

    return (result_arr)
