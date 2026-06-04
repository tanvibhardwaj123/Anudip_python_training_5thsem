#Wap to calculate Electricity Bill

#input units consumed
units = int(input("Enter units consumed: "))

#validate units
if(units < 0):
    exit("Units cannot be negative")

#---------------------------------------------------

#calculate bill
if(units <= 100):
    bill = units * 5

elif(units <= 200):
    bill = units * 7

else:
    bill = units * 10

#---------------------------------------------------

#determine consumption category
if(units <= 100):
    category = "Low Consumption"

elif(units <= 200):
    category = "Medium Consumption"

else:
    category = "High Consumption"

#---------------------------------------------------

#display bill details
print("Units Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)
