lst = []
lst2=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    n = int(input())
    lst.append(n)
print(lst)
n2 = int(input("Enter number of elements : "))
for i in range(0, n2):
    ele = int(input())
    lst2.append(n)
print(lst2)
s=lst+lst2
print(s)
a=sorted(s)
print(a)
