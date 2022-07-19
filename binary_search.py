# code your iterative algorithm here

def binary_search(data, el):
    first = 0
    last = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1

    return found

def recursive_bsearch(data, el):
    if len(data) == 0:
        return False

    else: 
        mid = len(data)//2

        if data[mid] == el:
            return True
        else: 
            if el < data[mid]:
                return recursive_bsearch(data[:mid], el)
            else: 
                return recursive_bsearch(data[mid+1], el)

def binary_recursive(data, el):
    if (len(data) == 0):
        return False

    mid = len(data)//2

    print(mid, " ", data[mid])

    if (data[mid] == el):
        print("match")
        return True
    else:
        if (el < data[mid]):
            print("Calling with ", data[:mid])
            return binary_recursive(data[:mid],el)
        else:
            print("Calling2 with ", data[mid+1:])
            return binary_recursive(data[mid+1:],el)
    return False


test_list = [ 3, 5, 7, 8, 9, 11, 15, 17, 22, 25]

print(binary_search(test_list, 13))

test_list2 = [1,3,5,6,7,9,11,23,55]

print(binary_recursive(test_list2, 55))
