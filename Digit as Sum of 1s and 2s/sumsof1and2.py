def 1s_and_2s(n):
    result = [[1],[11,2]]
    for i in range(2,n+1):
        temp = []
        for j in result[i-2]:
            temp.append(10*j + 2)
        for k in result[i-1]:
            temp.append(10*k + 1)
        result.append(temp)
    return result[n-1]
  
  if __name__ == '__main__':
    a = int(input())
    result = 1s_and_2s(n)
    print(" ".joined(result))
