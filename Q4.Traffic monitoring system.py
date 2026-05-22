 #A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit.
speed_limit =100
vehical_speed = int(input("Enter the speed of the vehical:"))
if vehical_speed > speed_limit:
    print("Vehical exceeded the speed limit.")
else:
    print("Vehical is within the speed limit")

#Output 1
#Enter the speed of the vehical:120
#Vehical exceeded the speed limit.

#Output 2
#Enter the speed of the vehical:70
#Vehical is within the speed limit