
#Exercise 5 Tienda de mascotas

print ('Welcome to Pet World')

print ('What type of pet do you have:\n 1. Dog\n 2. Cat\n 3. Bunny\n ')
pet = input ('Enter an option: ').strip().lower()


if pet == "dog":
    print ('Recommend Royal Canin')

elif pet == "cat":
    print ('Recommend Donkat')

elif pet == "bunny":
    print ('Recommend Bunny Bonnie')

else:
    print ('I have no recommendations for that type of animal')
