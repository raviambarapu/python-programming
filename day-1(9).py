t=int(input("enter the n0:"))
e=[3,5,2,0]
l=[0,2,4,4]
x=[0,0,0,0]
for i in range(0,t):
    x[i]=x[i-1]+e[i]-l[i]
    print(x[i])
print("max guests:",max(x))
