import math
# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ").strip()
if name == "":
    print("name is required.")
else:
    print("accepted")
    
previous = input("Enter previous meter reading: ").strip()
try:
    previous_reading = float(previous)
    print("Your previous reading is:", previous_reading)
except ValueError:
    print("Enter a valid reading")
if previous <= "0":
    print("previous reading must be greater than 0:")
else: 
    print("accepted")
    
current = input("Enter current meter reading: ")
try:
    current_reading = float(current)
    print("Your current reading is:", current_reading)
except ValueError:
    print("Enter a valid reading")
if current == "0":
    print ("current meter reading is required")
elif current <= previous:
    print("current reading must be higher than previous reading")

else: 
    print("accepted")
    
consumption = current_reading - previous_reading
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading

