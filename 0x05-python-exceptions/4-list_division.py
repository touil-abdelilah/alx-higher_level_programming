#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            # Check if both elements are numbers
            if not (isinstance(dividend, (int, float)) and isinstance(divisor, (int, float))):
                raise TypeError("wrong type")
            # Perform division if divisor is not zero
            if divisor != 0:
                division_result = dividend / divisor
            else:
                raise ZeroDivisionError("division by 0")
        except IndexError:
            print("out of range")
            division_result = 0
        except TypeError as e:
            print(e)
            division_result = 0
        except ZeroDivisionError as e:
            print(e)
            division_result = 0
        finally:
            result.append(division_result)
    return result
