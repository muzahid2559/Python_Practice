# Linear Search:

def linear_search(some_list,value):
    for i in range(len(some_list)):
        if some_list[i] == value:
            return "Found"
    if i == len(some_list)-1:
        return "Not Found"


my = [1,5,8,7]
b = linear_search(my,8)
print(b)