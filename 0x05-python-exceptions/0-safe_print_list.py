#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        p_elements = 0
        
        try:
            
            for i in range(x):
                print("{}".format(my_list[i]),end="")
                p_elements += 1
                
        except IndexError:
            pass
        finally:
            print()
            return p_elements
