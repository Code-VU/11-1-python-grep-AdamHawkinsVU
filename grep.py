import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    
    count = 0

    str_expression= str(regular_expression)

    compare_file= 'mbox-long.txt'

    file_handle= open(compare_file)

    for line in file_handle:
        #line = line.rstrip()
        list_of_items_found = re.findall(str_expression, line)
        if list_of_items_found != []:
            count += 1

    print ('mbox.txt had ' + str(count) + ' lines that matched ' + str_expression) 

if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()