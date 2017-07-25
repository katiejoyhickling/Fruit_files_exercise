""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    fruit_file = open(filename)

    fruit_file_string = fruit_file.read()
    fruit_file.close()
    fruit_file_list = fruit_file_string.strip().split('\n')


 
    return fruit_file_list

    


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    list_in_common = []
    for item in lst1:
        if item in lst2:
            list_in_common.append(item)

    return list_in_common


# Call your functions at the bottom, after they've been defined.
fruit_list_1 = open_and_read_file("fruits_1.txt")
fruit_list_2 = open_and_read_file ("fruits_2.txt")
common_list = compare(fruit_list_1, fruit_list_2)
print common_list
common_string = " , "
common_string_joined = common_string.join(common_list)
print "There are these fruits in common: " + common_string_joined

