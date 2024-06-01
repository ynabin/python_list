cp = float(input("enter the value"))
sp = float(input("enter the value"))
if cp==sp:
    print("No profit No loss")
else:
    if sp>cp:
        print("Profit of", sp-cp)
    else:
        print("loss of", cp-sp)
        