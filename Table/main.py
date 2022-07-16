n = int(input("Enter your number for starting table : "))
e = int(input("Enter your number for end of the table :"))
for i in range(n,e+1):
    with open(f"Table of {i}",'a') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")