# Number Pattern 1
# n = 5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     print()



#Pattern 2
n = 9
# for i in range(1, n + 1):
#     ch = ord('A')
#     for j in range(1, i + 1):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()


n = 5
for i in range(n,0,-1):
    for j in range(1,i,1):
        print("#",end="")
    print()



#Pattern 4

n = 6
for i in range(n,0,-1):
    for j in range(1,i,1):
        print(j,end="")
    print()



#pattern 5

n = 5
for i in range(1, n + 1):
    # Print spaces
    for space in range(n - i):
        print(" ", end="")  
    # Print increasing numbers
    for num in range(1, i + 1):
        print("*", end="")   
    # Print decreasing numbers
    for num in range(i - 1, 0, -1):
        print("*", end="")
    print()