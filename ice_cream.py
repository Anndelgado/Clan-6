#Exercise 1 Heladeria

print ('Welcome to ice cream land\n')

v = 0
s = 0
ch = 0

for i in range (0,5,1):
    print ('Choose a flavour:\n 1. Vanilla\n 2. Strawberry\n 3. Chocolate\n ')
    choice = input('\nEnter an option: ').strip()

    if (choice == '1'):
        v +=1

    elif (choice == '2'):
        s +=1
    
    elif (choice == '3'):
        ch +=1


print("\nTotal ice creams sold:")
print ('Amount of vanilla: ',v)
print ('Amount of Strawberry: ',s)
print ('Amount of vChocolate: ',ch)
