#ques16
for i in range(1,4):
    for j in range(i):
        print(i-j,end=" ")
    print()

#ques 17
for i in range(7):
    for j in range(i):
        print("*",end=" ")
    print()

#ques 18
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()
for j in range(4):
    for j in range(1,i-j):
        print("*",end=" ")
    print()
    
#ques 19
for i in range(1,11):
    if i <10:
        print(" ",end="")
    print(f"{i}|",end="")
    for j in range(1,11):
        print(i*j,end="\t")
    print()
    
