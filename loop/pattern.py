num = 10
i = 1
while i <= 10:
    print("\U0001f600"*i)
    i += 1

for i in range(num+1):
    print("*"*i)

i = 0
while i <= 10:
    for j in range(i):
        print("*",sep="",end="")
    print("",sep="",end="\n")
    i += 1