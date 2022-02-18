def add(a,b):
    sum=a+b
    return sum
result= add(3,4)
print(result)

def sum_array(c):
    result=0
    for d in c: 
        result += d
    return result

array_sum = sum_array([1,2,3,4,5,6,7])
print(array_sum)