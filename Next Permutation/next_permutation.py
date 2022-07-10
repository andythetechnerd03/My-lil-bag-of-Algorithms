# Next permutation in lexicographic order

def next_permutation(s):
    n = len(s)
    """Loop from right to left to check if the element preceding is larger, if it's not then stop"""
    j = n - 2
    while s[j] > s[j+1]:
        j -= 1
    """Find the smallest number that is larger than j looping from the right (guarantee that the first element is 
    smallest then interchange j with k"""
    k = n - 1
    while s[j] > s[k]:
        k -= 1
    s[j], s[k] = s[k], s[j]
    """Reverse the part from the j+1 to n"""
    r = n - 1
    t = j + 1
    while r > t:
        s[r], s[t] = s[t], s[r]
        r -= 1
        t += 1
    result = "".join(s)
    return result

if __name__ == "__main__":
    n = input()
    s = [i for i in n]
    print(next_permutation(s))
    
