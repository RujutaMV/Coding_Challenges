def find_max(lst):
    """
    Find maximum number in a list without using built-in function    
    :param lst: 
    :return: int
    """
    max = lst[0]  
    for num in lst:
        for i in lst:
            if num < i:
                break
        else:
            max = num
    return max

print(find_max([1,3,6,9,4]))            # O(n²)

def find_max(lst):
    """
    Find maximum number in a list without using built-in function    
    :param lst: 
    :return: int
    """
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

print(find_max([1,3,6,9,4]))          # O(n)

def find_max(lst):
    return max(lst)

print(find_max([1,3,6,9,4]))          # O(n)          
