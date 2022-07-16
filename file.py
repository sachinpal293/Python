list = [1,2,3]
with open("sample.txt",'a') as f:
    for i in list:
        f.write(f"{i}")
