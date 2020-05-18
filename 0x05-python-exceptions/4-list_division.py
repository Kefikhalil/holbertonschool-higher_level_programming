#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    new_result = 0

    for idx in range(list_length):
        try:
            new_result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(new_result)
            new_result = 0
    return new_list
