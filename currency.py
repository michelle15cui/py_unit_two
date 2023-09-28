dollars = input("the total money")
hundred_Bills = round(int(dollars) // 100)
print("Hundred bills", hundred_Bills)
fifty_Bills = (int(dollars) % 100) // 50
print("Fifty Bills", fifty_Bills)
twenty_Bills = ((int(dollars) % 100) % 50) // 20
print("Twenty Bills", twenty_Bills)
ten_Bills = (((int(dollars) % 100) % 50) % 20) //10
print("Ten Bills", ten_Bills)
five_Bills = ((((int(dollars) % 100) % 50) % 20) % 10) //5
print("Five Bills", five_Bills)
one_Bills = (((((int(dollars) % 100) % 50) % 20) % 10) % 5) //1
print("One Bills", one_Bills)
