def binary_search(low, high, arr, x):
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half, note that we don't subtract by 1 in the latter case because in the tight case
        # where there are 2 elements left, having "-1" will mess up the algorithm
        elif arr[mid] > x:
            high = mid
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return False

# I present both methods (while and recursive) for better reference
def binary_search_recursive(a, b, arr, x):
    m = (a+b)//2
    # seed case
    if arr[m] == x:
        # you found it, good!
        return m
    elif a == b:
        # if a and b are equal and the mid element still doesn't match, *family feud buzzer sound*
        return -1
    if arr[m] > x:
        return binary_search_recursive(a, m, arr, x)
    if arr[m] < x:
        return binary_search_recursive(m + 1, b, arr, x)
    
