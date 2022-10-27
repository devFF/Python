def simple_numbers(n):
    answer = []
    for i in range(2, n+1):
        for j in range(2,i):
            print(i,j)
            if i % j == 0:
                break
        else:
            answer.append(i)
    return answer


answer = simple_numbers(n=10)
print(answer)
