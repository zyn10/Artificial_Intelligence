#Cinema Hall
print("***Welcome to Cinema Hall***")
print("\nPlease Select your Movie")
print("\nPress 1 for Hollywood")
print("\nPress 2 for Bollywood")
print("\nPress 3 for Lollywood")
choice1=int(input("Choice :"))
choice2="no movie"
print(choice1)
if choice1 == 1:
    print("Enter the name Favourite Movies from this genre");
    print("\nSpiderman")
    print("\nTitanic")
    print("\nSnipers")
    choice2 = input("Choice :")
elif choice1 == 2:
    print("Enter the name Favourite Movies from this genre");
    print("\n3 idiots")
    print("\nTiger")
    print("\nHacked")
    choice2 = input("Choice :")
elif choice1 == 3:
    print("Enter the name Favourite Movies from this genre");
    print("\nWrong number")
    print("\nActor in law")
    print("\nPowercut")
    choice2 = input("Choice :")
print("Thankyou for booking with us")
print("Your ticket is booked for" ,choice2)

