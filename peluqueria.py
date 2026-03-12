print ("Welcome to you hair salon")

hour = int(input("What time does the client arrive?: ").strip())

if 6<= hour <=11:
    print ("The client arrive in the morning shift.")

elif 12<= hour <=17:
    print ("The client arrive in the afternoon shift.")

elif 18<= hour <=22:
    print ("The client arrive in the night shift.")

else:
    print ("The client arrived out of the shift.")

    