print ("Welcome to Sports Store")

expensive = 0

for i in range(6):
  price = int(input(f"Enter the price of the product {i+1}: ").strip())

  if price > 100000:
      expensive += 1


print("Products that cost more than 100000: ", expensive)
