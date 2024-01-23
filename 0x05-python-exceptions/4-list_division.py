#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            division_result = 0
            # Check if both elements are numbers
            if not isinstance(dividend, (int, float)):
                if isinstance(divisor, (int, float)):
                    raise TypeError("wrong type")
            # Perform division if divisor is not zero
            if divisor != 0:
                division_result = dividend / divisor
            else:
                raise ZeroDivisionError("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError as e:
            print(e)
        finally:
            result.append(division_result)
    return result
