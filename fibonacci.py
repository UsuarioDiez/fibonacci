def fibonacci(n,narr):
    if (n==0):
        nv=0
    elif (n==1):
        nv=1
    else:
        nv=narr[n-1]+narr[n-2]
    return nv
import time


# def fibonacci(n):
#     if (n==0):
#         nv=0
#     elif (n==1):
#         nv=1
#     else:
#         nv=fibonacci(n-1)+fibonacci(n-2)
#     return nv





length=int(input('Give me the size of the fibonacci\n'))

print('==============================================')

for j in range(15):
    narr = []
    start=time.time()
    for i in range(length):
       narr.append(fibonacci(i,narr))
       # print(narr[i])
    end=time.time()
    total=end-start
    print(total)
