even_num=[]
square = []
cube=[]
for i in range(100):
    if i %2 ==0:
        even_num.append(i)

for num in even_num:
    square.append(num**2)

for a in even_num:
    cube.append(a**3)
print(cube)