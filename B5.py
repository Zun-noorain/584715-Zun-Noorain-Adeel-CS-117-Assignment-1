
# B5: Resistor Tolerance Sorting

count_1_percent = 0
count_5_percent = 0
count_reject = 0
 
resistance = float(input("Enter measured resistance (0 to stop): "))
 
while resistance != 0:
    if 99.0 <= resistance <= 101.0:
        count_1_percent += 1
    elif 95.0 <= resistance <= 105.0:
        count_5_percent += 1
    else:
        count_reject += 1
    resistance = float(input("Enter measured resistance (0 to stop): "))
 
print("1% tolerance:", count_1_percent)
print("5% tolerance:", count_5_percent)
print("Reject:", count_reject)
