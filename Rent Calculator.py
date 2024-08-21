
rent = int(input("Enter your hostel rent = "))
food = int(input("Enter the ammount of food ordered = "))
electricity_spend = int(input ("Enter your Total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit =" ))
persons = int(input('Enter the number of persons living in room'))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) // persons

print ("Each per will pay : ", output)
