n = 5 

for i in range(6):  
    for j in range(6):  
        if j <= n - i:  
            print(" ", end="")
        else:  
            print("*", end="")
    print()