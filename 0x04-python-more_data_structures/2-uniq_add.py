#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(map(lambda x: x if my_list.count(x) > 1 else x, my_list))
    new = sum(new)
    return new
