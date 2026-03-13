#Exercise 2 Gimnasio


print ('Welcome Gym Big Guy')

age = int(input ('Enter age of client: ').strip())

if age >=0 and age <12:
  print ('Cannot enter')

elif age >= 13 and age < 18:
  print ('Youth class')

elif age >= 18 and age < 59:
  print ('General class')

elif age >= 59 and age < 100:
  print ('Senior class')

else:
  print ('Age dosent exit')

