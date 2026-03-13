print ("Welcome to Dance Moms")

clss = int(input("Number of class attendances: ").strip().lower())

if 0<= clss < 5:
    print ("low attendance")

elif 5<= clss <=8:
    print ("average attendance")

else:
    print ("hihg attendance")
