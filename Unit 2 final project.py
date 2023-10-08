
users_Name=input("What is your name? ")
print("Hi", users_Name, "my name is chatbox. ")

place=input("Where are you from? ")
print("I know", place, "it's a very beautiful place! ")

fav_Number=input("What is your favorite number? ")
times=int(fav_Number)/6
print("Your favorite number is", times, "times than mine! ")

fav_Car=input("What is your favorite car? ")
print("Wow, I've always wanted a", fav_Car, "as well")

car_Cost=input("How much does your dream car cost? ")
print(car_Cost, "?! that's really expensive.")

loan_Years=input("How many years you would take a loan out to pay for the car? ")

rate=input("What annual interest rate you expects to get for the car? (the entered value may be between 0 and 20%) ")
monthly_Rate=float(rate)/12

n=int(loan_Years)*12
carCost=(float(rate)*int(car_Cost))/(1-(1+float(rate))**(-n))
total_Cost=carCost*int(loan_Years)

print("If you bought a", fav_Car, "you would have a monthly payment of", carCost, "a total payment of", total_Cost, ". Hopefully that is freindly to your budget!")
print("I hope you can make the purchase!")
print(users_Name, "Bye, I hope you can have a good day!")





