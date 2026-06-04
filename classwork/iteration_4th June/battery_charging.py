#Program to display battery charging level
#Battery starts charging from 20%
#Increase charging level by 10% until it reaches 100%
#Display "Full Charge" when charging is complete

charging_level=20
electricity_status=True

#---------------------------------------------------
#charging battery

while(charging_level<=100):

    if(electricity_status):
        print("Battery Charging Level =",charging_level,"%")
        charging_level+=10

    else:
        break

#---------------------------------------------------
#displaying charging status

print("Full Charge")
