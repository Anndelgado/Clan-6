
#Exercise 3 Cafetería

print ('Welcome to Coffe Landia')

coffee = 4000
tea = 3500
juice = 5000

print ('Choose a drink:\n 1. Coffee.\n 2. Tea.\n 3. Juice.\n')
drink = input ("What drink do you want?: ").strip().lower()
amoung = int (input ("How many of that do you want: ").strip())

if drink == "coffee":
    total = amoung *  coffee

elif drink == "tea":
    total = amoung * tea

elif drink == "juice":
    total = amoung * juice

else:
    print("Try again!")
    total = 0

print ('The total of your bill is: ',total)

