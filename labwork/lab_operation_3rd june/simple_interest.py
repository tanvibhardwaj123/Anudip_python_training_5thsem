 #Wap to calculate simple interest and validate the data if necessary
principle = float(input("enter the principle amount"))
Time = float(input("enter the time "))
Rate = float(input("enter the Rate "))
if(principle<0):
    exit("principle not negative")
if(Time<0):
    exit("Time cannot be Negative")
if(Rate<0):
    exit("Rate cannot be Negative")
Simple_Interest = (principle*Time*Rate)/100 
print("Simple Interest is",Simple_Interest)

