print ("Welcome to parkin home\n")


time = int(input("How many hours was your car here?: ").strip())

hour = 5000
add = 3000 

if time == 2:
    total = hour + add

else:
    total = hour + (add * (time-1))


print ("The total of your bill is: ", total)

